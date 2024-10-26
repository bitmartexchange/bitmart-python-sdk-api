import logging
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
                                api_memo='your_api_memo',
                                api_key='your_api_key',
                                api_secret_key='your_secret_key'
                                )
my_client.login()

my_client.subscribe(args="futures/asset:USDT")


# my_client.subscribe(args="futures/ticker")

# time.sleep(30)

