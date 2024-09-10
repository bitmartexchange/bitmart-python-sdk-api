import logging
import time

from bitmart.lib.cloud_consts import FUTURES_PUBLIC_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.futures_socket_client import FuturesSocketClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    logging.info(message)


my_client = FuturesSocketClient(stream_url=FUTURES_PUBLIC_WS_URL,
                                on_message=message_handler)

# Example 1:

# Subscribe to a single symbol stream
my_client.subscribe(args="futures/depth20:BTCUSDT")

time.sleep(2)

# Unsubscribe
my_client.unsubscribe(args="futures/depth20:BTCUSDT")

time.sleep(5)
# Example 2:
# Send the original subscription message
my_client.send({"action": "subscribe", "args": ["futures/depth20:BTCUSDT"]})

time.sleep(2)

# Unsubscribe
my_client.send({"action": "unsubscribe", "args": ["futures/depth20:BTCUSDT"]})

# Stop
# my_client.stop()
