import logging
import time

from bitmart.lib.cloud_consts import SPOT_PUBLIC_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.lib.cloud_ws_client import CloudWSClient
from bitmart.ws_spot import create_spot_subscribe_params

config_logging(logging, logging.DEBUG)


class WSTest(CloudWSClient):

    def on_message(self, message):
        print('[ReceiveServerMessage]--------------------------->')
        # print(f'[ReceiveServerMessage]-------->{message}')


ws = WSTest(SPOT_PUBLIC_WS_URL)
ws.set_debug(True)
channels = [
    'spot/ticker:BTC_USDT'
]

ws.spot_subscribe_without_login(create_spot_subscribe_params(channels))

time.sleep(60)
