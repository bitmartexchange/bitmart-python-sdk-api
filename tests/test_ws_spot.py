from bitmart import cloud_consts
from bitmart.cloud_consts import WS_USER_SPOT_ORDER
from bitmart.cloud_ws_client import CloudWSClient
from bitmart.ws_spot import create_channel, create_spot_subscribe_params
from tests import data as data


class WSTest(CloudWSClient):

    def on_message(self, message):
        print('[ReceiveServerMessage]--------------------------->')
        # print(f'[ReceiveServerMessage]-------->{message}')


def test_spot_subscribe_without_login():
    """
        Test spot subscribe with key
        pytest --capture=no
    """
    ws = WSTest(data.ws_url, "", "", "")
    ws.set_debug(True)
    channels = [
        # Only support public channel
        # create_channel(cloud_consts.WS_PUBLIC_SPOT_TICKER, 'BTC_USDT')
        # create_channel(cloud_consts.WS_PUBLIC_SPOT_KLINE_1M, 'BTC_USDT')
        create_channel(cloud_consts.WS_PUBLIC_SPOT_DEPTH5, 'BTC_USDT')
        # create_channel(cloud_consts.WS_PUBLIC_SPOT_TRADE, 'BTC_USDT')
    ]

    ws.spot_subscribe_without_login(create_spot_subscribe_params(channels))


def test_spot_subscribe_with_login():
    """
        Test spot subscribe with key
        pytest --capture=no
    """
    channels = [
        # Only support private channel
        create_channel(WS_USER_SPOT_ORDER, 'BTC_USDT')
    ]

    ws = WSTest(url=data.ws_url_user, api_key=data.api_key, memo=data.memo, secret_key=data.secret_key)
    ws.set_debug(True)
    ws.spot_subscribe_with_login(create_spot_subscribe_params(channels))
