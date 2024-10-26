import logging
import time

from bitmart.lib.cloud_consts import SPOT_PUBLIC_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.spot_socket_client import SpotSocketClient

config_logging(logging, logging.INFO)


def message_handler(message):
    logging.info(f"message_handler: {message}")


my_client = SpotSocketClient(stream_url=SPOT_PUBLIC_WS_URL,
                             on_message=message_handler)

# Subscribe to a single symbol stream
my_client.subscribe(args="spot/kline1m:BTC_USDT")

# Subscribe to multiple symbol streams
my_client.subscribe(args=["spot/kline5m:BTC_USDT", "spot/kline15m:BTC_USDT"])

# Send the original subscription message
my_client.send({"op": "subscribe", "args": ["spot/kline1D:BTC_USDT"]})

time.sleep(5)

# Unsubscribe
my_client.unsubscribe(args="spot/kline1m:BTC_USDT")

my_client.send({"op": "unsubscribe", "args": ["spot/kline15m:BTC_USDT"]})

# Stop
# my_client.stop()
