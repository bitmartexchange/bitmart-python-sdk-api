import threading

import json
import logging
import time

from bitmart.lib import cloud_utils
from bitmart.lib.cloud_consts import FUTURES_PUBLIC_WS_URL
from bitmart.lib.cloud_utils import single_stream
from bitmart.websocket.socket_manager import SocketManager


class FuturesSocketClient:
    """
    Socket client for BitMart's futures trading.
    """

    def __init__(
            self,
            stream_url=FUTURES_PUBLIC_WS_URL,
            on_message=None,
            on_open=None,
            on_close=None,
            on_error=None,
            on_ping=None,
            on_pong=None,
            logger=None,
            timeout=None,
            reconnection=True,
            ping_interval=10,
            api_key=None,
            api_secret_key=None,
            api_memo=None,
    ):
        if not logger:
            logger = logging.getLogger(__name__)
        self.logger = logger
        self.socket_manager = SocketManager(
            stream_url,
            prefix_name="Futures",
            on_receive=self.receive,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            on_ping=on_ping,
            on_pong=on_pong,
            logger=logger,
            timeout=timeout,
            on_reconnect=self.reconnect,
        )
        self.stream_url = stream_url
        self.reconnection = reconnection
        self.reconnectionUseLogin = False
        self.reconnectionChannel = []
        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.API_MEMO = api_memo
        self.on_message = on_message

        # start the thread
        self.socket_manager.start()
        self.logger.debug(f"[{self.socket_manager.name}] Running...")

        # Start the ping timer
        self.ping_interval = ping_interval
        self.start_send_ping()

    def start_send_ping(self):
        self.ping()
        ping_timer = threading.Timer(self.ping_interval, self.start_send_ping)
        ping_timer.start()

    def send(self, message: dict):
        self.__send(json.dumps(message))

    def subscribe(self, args):
        if single_stream(args):
            args = [args]
        json_msg = json.dumps({"action": "subscribe", "args": args})
        self.__send(json_msg)

    def unsubscribe(self, args):
        if single_stream(args):
            args = [args]
        json_msg = json.dumps({"action": "unsubscribe", "args": args})
        self.__send(json_msg)

    def __send(self, json_msg):
        if self.reconnection:
            if json_msg not in self.reconnectionChannel:
                self.reconnectionChannel.append(json_msg)
        self.socket_manager.send_message(json_msg)

    def receive(self, message):
        message_data = json.loads(message)
        # self.logger.debug(f"[{self.socket_manager.name}] Received Text Message: {message_data}")

        if self.reconnectionUseLogin:
            action = message_data.get("action")
            success = message_data.get("success")
            # {'action': 'access', 'success': True}
            # {'action': 'access', 'success': False, 'error': 'access failed: **'}
            if action == "access" and success is False:
                self.logger.error(f"[{self.socket_manager.name}] Connection Stop Reason=>{message_data}")
                self.__close()

        self.on_message(message_data)

    def login(self, timeout=5):
        if not self.API_KEY:
            self.stop()
            raise ValueError("Invalid API KEY")
        if not self.API_SECRET_KEY:
            self.stop()
            raise ValueError("Invalid API SECRET KEY")
        if not self.API_MEMO:
            self.stop()
            raise ValueError("Invalid API MEMO")
        self.reconnectionUseLogin = True
        timestamp = cloud_utils.get_timestamp()
        sign = cloud_utils.sign(cloud_utils.pre_substring(
            timestamp, self.API_MEMO, 'bitmart.WebSocket'), self.API_SECRET_KEY)
        self.socket_manager.send_message(
            json.dumps({"action": "access", "args": [self.API_KEY, timestamp, sign, "web"]}))
        # timeout
        time.sleep(timeout)

    def ping(self):
        if self.socket_manager.ping('{"action":"ping"}'):
            self.logger.debug(f"[{self.socket_manager.name}] Sending Message '\\\\{{\"action\":\"ping\"}}'")

    def stop(self):
        self.__close()
        self.socket_manager.join()

    def __close(self):
        self.reconnection = False
        self.socket_manager.close()

    def reconnect(self):
        if not self.reconnection:
            return

        self.logger.debug(
            f"[{self.socket_manager.name}] Reconnection to: {self.stream_url}",
        )

        # time.sleep(2)
        self.socket_manager.reconnect()
        if self.reconnectionUseLogin:
            self.login()

        for msg in self.reconnectionChannel:
            time.sleep(1)
            self.socket_manager.send_message(msg)
