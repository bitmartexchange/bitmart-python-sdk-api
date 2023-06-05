import asyncio


from bitmart.lib.cloud_consts import WS_URL
from bitmart.ws_spot import spot_subscribe_with_login, spot_subscribe_without_login


class CloudWSClient(object):

    def __init__(self, url: str = WS_URL, api_key: str = '', secret_key: str = '', memo: str = ''):
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
        asyncio.run(spot_subscribe_without_login(self.on_message, self.URL, self.DEBUG, self.TIME_OUT, param))

    async def spot_subscribe_without_login_ext(self, params):
        """
        Subscribe
        :param params: Public channels. eg. [{"op": "subscribe", "args": ["spot/ticker:BMX_BTC", "spot/user/ticker:ETH_BTC"]},{"op": "subscribe", "args": ["spot/ticker:BMX_USDT", "spot/user/ticker:ETH_USDT"]}]
        :return:
        """
        task = []
        for param in params:
            task.append(asyncio.create_task(spot_subscribe_without_login(self.on_message, self.URL, self.DEBUG, self.TIME_OUT, param)))

        await asyncio.gather(*task)