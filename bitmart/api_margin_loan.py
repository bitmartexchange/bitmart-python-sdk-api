from .cloud_client import CloudClient
from .cloud_consts import *


class APIMarginLoan(CloudClient):

    def __init__(self, api_key, secret_key, memo, url: str = API_URL, timeout: tuple = TIMEOUT):
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout)

    # POST https://api-cloud.bitmart.com/spot/v1/margin/isolated/borrow
    def margin_borrow_isolated(self, symbol: str, currency: str, amount: str):
        param = {
            'symbol': symbol,
            'currency': currency,
            'amount': amount
        }
        return self._request_with_params(POST, API_MARGIN_BORROW_ISOLATED_URL, param, Auth.SIGNED)

    # POST https://api-cloud.bitmart.com/spot/v1/margin/isolated/repay
    def margin_repay_isolated(self, symbol: str, currency: str, amount: str):
        param = {
            'symbol': symbol,
            'currency': currency,
            'amount': amount
        }
        return self._request_with_params(POST, API_MARGIN_REPAY_ISOLATED_URL, param, Auth.SIGNED)

    # GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/borrow_record
    def borrow_record_isolated(self, symbol: str, borrow_id='', N=50):
        param = {
            'symbol': symbol,
            'borrow_id': borrow_id,
            'N': N
        }
        return self._request_with_params(GET, API_BORROW_RECORD_ISOLATED_URL, param, Auth.KEYED)

    def borrow_record_isolated_with_time(self, symbol: str, start_time: int, end_time: int, borrow_id='', N=50):
        param = {
            'symbol': symbol,
            'borrow_id': borrow_id,
            'start_time': start_time,
            'end_time': end_time,
            'N': N
        }
        return self._request_with_params(GET, API_BORROW_RECORD_ISOLATED_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/repay_record
    def repayment_record_isolated(self, symbol: str, repay_id='', currency='', N=50):
        param = {
            'symbol': symbol,
            'repay_id': repay_id,
            'currency': currency,
            'N': N
        }
        return self._request_with_params(GET, API_REPAYMENT_RECORD_ISOLATED_URL, param, Auth.KEYED)

    def repayment_record_isolated_with_time(self, symbol: str, start_time: int, end_time: int,
                                            repay_id='', currency='', N=50):
        param = {
            'symbol': symbol,
            'repay_id': repay_id,
            'currency': currency,
            'start_time': start_time,
            'end_time': end_time,
            'N': N
        }
        return self._request_with_params(GET, API_REPAYMENT_RECORD_ISOLATED_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/pairs
    def trading_pair_borrowing_rate_and_amount(self, symbol=''):
        param = {
            'symbol': symbol
        }
        return self._request_with_params(GET, API_TRADING_PAIR_BORROWING_RATE_AND_AMOUNT_URL, param, Auth.KEYED)
