import asyncio
import warnings

from bitmart.lib.cloud_consts import FUTURES_PUBLIC_WS_URL
from bitmart.ws_contract import contract_subscribe_with_login, contract_subscribe_without_login


class CloudWSContractClient(object):

    def __init__(self, url: str = FUTURES_PUBLIC_WS_URL, api_key: str = '', secret_key: str = '', memo: str = ''):
        """
        Create api key from https://www.bitmart.com/api-config/en-US
        :param url: Websocket Domain URL.
        :param api_key: your access key
        :param secret_key: your secret key
        :param memo: your memo
        """
        self.API_KEY = api_key
        self.SECRET_KEY = secret_key
        self.MEMO = memo
        self.URL = url
        self.TIME_OUT = 10
        self.DEBUG = False

    def set_time_out(self, timeout):
        """
        Setting connection timeout, read timeout
        :param timeout: second
        :return:
        """
        self.TIME_OUT = timeout

    def set_debug(self, debug):
        """
        Setting print log
        :param debug: Ture print log | False not print log
        :return:
        """
        self.DEBUG = debug

    def on_message(self, message):
        """
        Receive message
        :param message: Server return message
        :return:
        """
        print(f'[on_message]-------->{message}')

    def contract_subscribe_with_login(self, param):
        """
        Subscribe
        :param param: Private channels. eg. {"action": "subscribe", "args": ["futures/position:BTCUSDT"]}
        :return:
        """
        warnings.warn("contract_subscribe_with_login is deprecated, see examples/websocket/futures/websocket_stream/", DeprecationWarning)
        asyncio.get_event_loop().run_until_complete(contract_subscribe_with_login(self.on_message, self.URL, self.API_KEY, self.MEMO, self.SECRET_KEY, self.DEBUG, self.TIME_OUT, param))

    def contract_subscribe_without_login(self, param):
        """
        Subscribe
        :param param: Public channels. eg. {"action": "subscribe", "args": ["futures/kline1m:BTCUSDT"]}
        :return:
        """
        warnings.warn("contract_subscribe_without_login is deprecated, see examples/websocket/futures/websocket_stream/", DeprecationWarning)

        asyncio.get_event_loop().run_until_complete(contract_subscribe_without_login(self.on_message, self.URL, self.DEBUG, self.TIME_OUT, param))