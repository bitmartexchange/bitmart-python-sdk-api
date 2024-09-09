import threading

import json
import logging
import time

from bitmart.lib import cloud_utils
from bitmart.lib.cloud_consts import SPOT_PUBLIC_WS_URL
from bitmart.lib.cloud_utils import single_stream
from bitmart.websocket.socket_manager import SocketManager


class SpotSocketClient:
    """
    Socket client for BitMart's Spot trading.
    """
    def __init__(
            self,
            stream_url=SPOT_PUBLIC_WS_URL,
            on_message=None,
            on_open=None,
            on_close=None,
            on_error=None,
            on_ping=None,
            on_pong=None,
            logger=None,
            timeout=None,
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
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            on_ping=on_ping,
            on_pong=on_pong,
            logger=logger,
            timeout=timeout,
        )
        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.API_MEMO = api_memo

        # start the thread
        self.socket_manager.start()
        self.logger.debug("BitMart Spot WebSocket Client started.")

        # Start the ping timer
        self.ping_interval = ping_interval
        self.start_send_ping()

    def start_send_ping(self):
        self.ping()
        ping_timer = threading.Timer(self.ping_interval, self.start_send_ping)
        ping_timer.start()

    def send(self, message: dict):
        self.socket_manager.send_message(json.dumps(message))

    def subscribe(self, args):
        if single_stream(args):
            args = [args]
        json_msg = json.dumps({"op": "subscribe", "args": args})
        self.socket_manager.send_message(json_msg)

    def unsubscribe(self, args):
        if single_stream(args):
            args = [args]
        json_msg = json.dumps({"op": "unsubscribe", "args": args})
        self.socket_manager.send_message(json_msg)

    def login(self):
        if not self.API_KEY:
            raise ValueError("Invalid API KEY")
        if not self.API_SECRET_KEY:
            raise ValueError("Invalid API SECRET KEY")
        if not self.API_MEMO:
            raise ValueError("Invalid API MEMO")
        timestamp = cloud_utils.get_timestamp()
        sign = cloud_utils.sign(cloud_utils.pre_substring(
            timestamp, self.API_MEMO, 'bitmart.WebSocket'), self.API_SECRET_KEY)
        self.socket_manager.send_message(json.dumps({"op": "login", "args": [self.API_KEY, timestamp, sign]}))
        time.sleep(5)

    def ping(self):
        self.socket_manager.ping()

    def stop(self):
        self.socket_manager.close()
        self.socket_manager.join()
