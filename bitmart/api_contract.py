from .cloud_client import CloudClient
from .cloud_consts import *


class APIContract(CloudClient):

    def __init__(self, api_key, secret_key, memo,  url: str = API_URL, timeout: tuple = TIMEOUT):
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout)

    # basic API
    # GET https://api-cloud.bitmart.com/contract/v1/tickers
    def get_ticker(self, contract_symbol):
        param = {'contract_symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_TICKER_URL, param)