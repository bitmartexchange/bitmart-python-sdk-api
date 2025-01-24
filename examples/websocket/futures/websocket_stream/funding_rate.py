import logging
import time

from bitmart.lib.cloud_consts import FUTURES_PUBLIC_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.futures_socket_client import FuturesSocketClient

config_logging(logging, logging.INFO)


def message_handler(message):
    logging.info(f"message_handler: {message}")


my_client = FuturesSocketClient(stream_url=FUTURES_PUBLIC_WS_URL,
                                on_message=message_handler)

# Send the original subscription message
my_client.send({"action": "subscribe", "args": ["futures/fundingRate:BTCUSDT"]})


# Stop
# my_client.stop()
