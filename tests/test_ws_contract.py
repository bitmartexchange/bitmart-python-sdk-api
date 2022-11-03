from bitmart import cloud_consts
from bitmart.cloud_consts import WS_USER_CONTRACT_ASSET
from bitmart.cloud_ws_contract_client import CloudWSContractClient
from bitmart.ws_contract import create_channel, create_contract_subscribe_params
from tests import data as data


class WSTest(CloudWSContractClient):

    def on_message(self, message):
        print('[ReceiveServerMessage]--------------------------->')
        # print(f'[ReceiveServerMessage]-------->{message}')


def test_contract_subscribe_without_login():
    """
        Test contract subscribe with key
        pytest --capture=no
    """
    ws = WSTest(data.contract_ws_url, "", "", "")
    ws.set_debug(True)
    channels = [
        # Only support public channel
        cloud_consts.WS_PUBLIC_CONTRACT_TICKER,
        create_channel(cloud_consts.WS_PUBLIC_CONTRACT_DEPTH5, 'BTCUSDT'),
        create_channel(cloud_consts.WS_PUBLIC_CONTRACT_KLINE_1M, 'BTCUSDT'),
    ]

    ws.contract_subscribe_without_login(create_contract_subscribe_params(channels))


def test_contract_subscribe_with_login():
    """
        Test contract subscribe with key
        pytest --capture=no
    """
    channels = [
        # Only support private channel
        create_channel(cloud_consts.WS_USER_CONTRACT_ASSET, 'USDT'),
        cloud_consts.WS_USER_CONTRACT_POSITION,
        cloud_consts.WS_USER_CONTRACT_UNICAST,
    ]

    ws = WSTest(url=data.contract_ws_url_user, api_key=data.api_key, memo=data.memo, secret_key=data.secret_key)
    ws.set_debug(True)
    ws.contract_subscribe_with_login(create_contract_subscribe_params(channels))
