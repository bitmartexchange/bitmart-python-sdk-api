import logging
import time

from bitmart.lib.cloud_consts import SPOT_PUBLIC_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.spot_socket_client import SpotSocketClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    logging.info(message)


my_client = SpotSocketClient(stream_url=SPOT_PUBLIC_WS_URL,
                             on_message=message_handler)

# Subscribe to a single symbol stream
my_client.subscribe(args="spot/depth5:BTC_USDT")

# Subscribe to multiple symbol streams
my_client.subscribe(args=["spot/depth20:BTC_USDT", "spot/depth50:BTC_USDT"])

# Send the original subscription message
my_client.send({"op": "subscribe", "args": ["spot/depth5:BTC_USDT"]})

time.sleep(5)

# Unsubscribe
my_client.unsubscribe(args="spot/depth5:BTC_USDT")

my_client.send({"op": "unsubscribe", "args": ["spot/depth50:BTC_USDT"]})

# Stop
# my_client.stop()
