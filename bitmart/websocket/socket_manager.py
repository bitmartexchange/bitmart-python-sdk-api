import logging
import threading
import time

from websocket import (
    ABNF,
    create_connection,
    WebSocketException,
    WebSocketConnectionClosedException,
    WebSocketTimeoutException,
)

from bitmart.lib.cloud_utils import inflate


class SocketManager(threading.Thread):
    def __init__(
        self,
        stream_url,
        on_receive=None,
        on_open=None,
        on_close=None,
        on_error=None,
        on_ping=None,
        on_pong=None,
        on_reconnect=None,
        logger=None,
        timeout=None,
    ):
        threading.Thread.__init__(self)
        if not logger:
            logger = logging.getLogger(__name__)
        self.logger = logger
        self.ws = None
        self.stream_url = stream_url
        self.on_receive = on_receive
        self.on_open = on_open
        self.on_close = on_close
        self.on_ping = on_ping
        self.on_pong = on_pong
        self.on_error = on_error
        self.on_reconnect = on_reconnect
        self.retryReconnectTimes = 5
        self.timeout = timeout
        self.is_close = False

        self.create_ws_connection()

    def create_ws_connection(self):
        self.logger.debug(
            f"WebSocket Client Connection to: {self.stream_url}",
        )

        self.ws = create_connection(
            self.stream_url, timeout=self.timeout
        )
        self.logger.debug(
            f"WebSocket Client has been established: {self.stream_url}",
        )
        self._callback(self.on_open)

    def reconnect(self):
        self.retryReconnectTimes -= 1
        if self.retryReconnectTimes < 0:
            self.logger.error(f"Reconnection failed: Retry Max 5 times")
            return

        if self.ws:
            self.ws.close()

        time.sleep(5 - self.retryReconnectTimes)  # Optional delay before attempting to reconnect

        try:
            self.create_ws_connection()  # Try to create a new connection
            self.retryReconnectTimes = 5
        except WebSocketException as e:
            self.logger.error(f"Reconnection failed: {e}")
            self.reconnect()  # Recursive reconnection attempt on failure

    def run(self):
        self.read_data()

    def send_message(self, message):
        if self.ws.connected:
            self.logger.debug("Sending message to BitMart WebSocket Server: %s", message)
            self.ws.send(message)

    def ping(self, message):
        if self.ws.connected:
            self.ws.send(message)
            return True
        return False

    def read_data(self):
        while not self.is_close:
            try:
                op_code, frame = self.ws.recv_data_frame(True)
            except WebSocketException as e:
                if isinstance(e, WebSocketConnectionClosedException):
                    self.logger.error("Lost websocket connection")
                elif isinstance(e, WebSocketTimeoutException):
                    self.logger.error("Websocket connection timeout")
                else:
                    self.logger.error("Websocket exception: {}".format(e))
                self._callback(self.on_close, "Close Reason: {}".format(e))
                self.on_reconnect()
                continue
            except Exception as e:
                self.logger.error("Exception in read_data: {}".format(e))
                raise e

            self._handle_data(op_code, frame)

            if op_code == ABNF.OPCODE_CLOSE:
                self.logger.warning(
                    "CLOSE frame received, closing websocket connection"
                )
                self._callback(self.on_close, "CLOSE frame received, closing websocket connection")
                break

    def _handle_data(self, op_code, frame):
        if op_code == ABNF.OPCODE_TEXT:
            data = frame.data.decode("utf-8")
            self.on_receive(data)
        elif op_code == ABNF.OPCODE_BINARY:
            data = inflate(frame.data)
            self.on_receive(data)
        elif op_code == ABNF.OPCODE_PING:
            self._callback(self.on_ping, frame.data)
            self.ws.pong("")
            self.logger.debug("Received Ping; PONG frame sent back")
        elif op_code == ABNF.OPCODE_PONG:
            self.logger.debug("Received PONG frame")
            self._callback(self.on_pong)

    def close(self):
        if not self.ws.connected:
            self.logger.warning("Websocket already closed")
        else:
            reason = "Normal closure"
            status_code = 1000
            truncated_reason = reason[:123]
            reason_bytes = truncated_reason.encode("utf-8")
            self.ws.send_close(status_code, reason_bytes)
        self._callback(self.on_close, f"WebSocket closed.")
        self.is_close = True
        return

    def _callback(self, callback, *args):
        if callback:
            try:
                callback(self, *args)
            except Exception as e:
                self.logger.error("Error from callback {}: {}".format(callback, e))
                if self.on_error:
                    self.on_error(self, e)
