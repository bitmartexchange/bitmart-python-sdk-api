from .cloud_client import CloudClient
from .cloud_consts import *


class APIBroker(CloudClient):

    def __init__(self, api_key, secret_key, memo, url: str = API_URL, timeout: tuple = TIMEOUT):
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout)

    # GET https://api-cloud.bitmart.com/spot/v1/broker/rebate
    def broker_rebates(self):
        return self._request_without_params(GET, API_BROKER_REBATE, Auth.KEYED)

    def broker_rebates_by_timestamp(self, start_time: int, end_time: int):
        param = {
            'start_time': start_time,
            'end_time': end_time
        }
        return self._request_with_params(GET, API_BROKER_REBATE, param, Auth.KEYED)
