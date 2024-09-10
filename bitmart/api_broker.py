from bitmart.lib.cloud_client import CloudClient
from bitmart.lib.cloud_consts import *


class APIBroker(CloudClient):

    def __init__(self, api_key: str = "", secret_key: str = "", memo: str = "", url: str = API_URL, timeout: tuple = TIMEOUT, headers=None, logger=None):
        """
        Create api key from https://www.bitmart.com/api-config/en-US
        :param api_key: your access key
        :param secret_key: your secret key
        :param memo: your memo
        :param url: https://api-cloud.bitmart.com
        :param timeout: (2, 10)
        """
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout, headers, logger)

    # GET https://api-cloud.bitmart.com/spot/v1/broker/rebate
    def broker_rebates(self):
        return self._request_without_params(GET, API_BROKER_REBATE, Auth.KEYED)

    def broker_rebates_by_timestamp(self, start_time: int, end_time: int):
        param = {
            'start_time': start_time,
            'end_time': end_time
        }
        return self._request_with_params(GET, API_BROKER_REBATE, param, Auth.KEYED)
