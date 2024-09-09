import logging

from bitmart.lib.cloud_consts import SPOT_PRIVATE_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.spot_socket_client import SpotSocketClient

config_logging(logging, logging.INFO)


def message_handler(_, message):
    logging.info(message)


my_client = SpotSocketClient(stream_url=SPOT_PRIVATE_WS_URL,
                             on_message=message_handler,
                             api_key="your_api_key",
                             api_secret_key="your_secret_key",
                             api_memo="your_api_memo")

# Login
my_client.login(timeout=5)

# Subscribe to a single symbol stream
my_client.subscribe(args="spot/user/balance:BALANCE_UPDATE")

# Stop
# my_client.stop()
