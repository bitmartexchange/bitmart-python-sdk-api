import logging
import time

from bitmart.lib.cloud_consts import SPOT_PUBLIC_WS_URL, SPOT_PRIVATE_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.spot_socket_client import SpotSocketClient

config_logging(logging, logging.INFO)


def open_handler(_):
    logging.info("open")


def message_handler(message):
    logging.info(message)


def close_handler(_, message):
    logging.info(message)


my_client = SpotSocketClient(stream_url=SPOT_PRIVATE_WS_URL,
                             on_open=open_handler,
                             on_message=message_handler,
                             on_close=close_handler,
                             api_memo='your_api_memo',
                             api_key='your_api_key',
                             api_secret_key='your_secret_key',
                             reconnection=True)

my_client.login(2)

my_client.subscribe(args="spot/user/balance:BALANCE_UPDATE")

# my_client.subscribe(args="spot/kline1m:BTC_USDT")

# time.sleep(30)

# my_client.subscribe(args="spot/ticker:BTC_USDT")
