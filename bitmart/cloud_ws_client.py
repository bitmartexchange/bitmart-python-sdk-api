import asyncio


from bitmart.cloud_consts import WS_URL
from bitmart.ws_spot import spot_subscribe_with_login, spot_subscribe_without_login


class CloudWSClient(object):

    def __init__(self, url: str = WS_URL, api_key: str = '', secret_key: str = '', memo: str = ''):
        """
        :param url: Request Domain URL.
        :param api_key: Get from bitmart API page.
        :param secret_key: Get from bitmart API page.
        :param memo: Get from bitmart API page.
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

    def spot_subscribe_with_login(self, param):
        """
        Subscribe
        :param param: Private channels. eg. {"op": "subscribe", "args": ["spot/user/order:BMX_BTC", "spot/user/order:ETH_BTC"]}
        :return:
        """
        asyncio.get_event_loop().run_until_complete(spot_subscribe_with_login(self.on_message, self.URL, self.API_KEY, self.MEMO, self.SECRET_KEY, self.DEBUG, self.TIME_OUT, param))

    def spot_subscribe_without_login(self, param):
        """
        Subscribe
        :param param: Public channels. eg. {"op": "subscribe", "args": ["spot/ticker:BMX_BTC", "spot/user/ticker:ETH_BTC"]}
        :return:
        """
        asyncio.get_event_loop().run_until_complete(spot_subscribe_without_login(self.on_message, self.URL, self.DEBUG, self.TIME_OUT, param))