import logging
from examples.config import API_KEY, SECRET_KEY, MEMO
import time

from bitmart.lib.cloud_consts import FUTURES_PRIVATE_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.futures_socket_client import FuturesSocketClient

config_logging(logging, logging.DEBUG)


def open_handler(ws):
    logging.info("open")
    ws.send_message('message')


def message_handler(message):
    logging.info(message)


def close_handler(_, message):
    logging.info(message)


my_client = FuturesSocketClient(stream_url=FUTURES_PRIVATE_WS_URL,
                                on_open=open_handler,
                                on_message=message_handler,
                                on_close=close_handler,
                                reconnection=True,
                                api_memo=MEMO,
                                api_key=API_KEY,
                                api_secret_key=SECRET_KEY
                                )
my_client.login()

my_client.subscribe(args="futures/asset:USDT")


# my_client.subscribe(args="futures/ticker")

# time.sleep(30)

