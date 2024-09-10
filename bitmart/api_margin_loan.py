from bitmart.lib.cloud_client import CloudClient
from bitmart.lib.cloud_consts import *


class APIMarginLoan(CloudClient):

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

    def margin_borrow_isolated(self, symbol: str, currency: str, amount: str):
        """Margin Borrow (Isolated) (SIGNED)
        Applicable to isolated margin account borrowing operations

        POST https://api-cloud.bitmart.com/spot/v1/margin/isolated/borrow

        :param symbol: Trading pair (e.g. BMX_USDT)
        :param currency: Borrowing currency, selected according to the borrowing trading pair(like BTC or USDT)
        :param amount: Amount of borrowing (precision: 8 decimal places)
        :return:
        """
        param = {
            'symbol': symbol,
            'currency': currency,
            'amount': amount
        }
        return self._request_with_params(POST, API_MARGIN_BORROW_ISOLATED_URL, param, Auth.SIGNED)

    def margin_repay_isolated(self, symbol: str, currency: str, amount: str):
        """Margin Repay (Isolated) (SIGNED)
        Applicable to isolated margin account repayment operations

        POST https://api-cloud.bitmart.com/spot/v1/margin/isolated/repay

        :param symbol: Trading pair (e.g. BMX_USDT)
        :param currency: Repayment currency, selected according to the borrowing trading pair(like BTC or USDT)
        :param amount: Amount of repayments (precision: 8 decimal places)
        :return:
        """
        param = {
            'symbol': symbol,
            'currency': currency,
            'amount': amount
        }
        return self._request_with_params(POST, API_MARGIN_REPAY_ISOLATED_URL, param, Auth.SIGNED)

    def borrow_record_isolated(self, symbol: str, borrow_id=None, start_time=None, end_time=None, n=None):
        """Get Borrow Record(Isolated) (KEYED)
        Applicable to the inquiry of borrowing records of an isolated margin account

        GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/borrow_record

        :param symbol: Trading pair (e.g. BMX_USDT)
        :param borrow_id: Borrow order id
        :param start_time: Query start time: Timestamp
        :param end_time: Query end time: Timestamp
        :param n: Query record size, allowed range[1-100]. Default is 50
        :return:
        """
        param = {
            'symbol': symbol
        }

        if borrow_id:
            param['borrow_id'] = borrow_id

        if n:
            param['N'] = n

        if start_time:
            param['start_time'] = start_time

        if end_time:
            param['end_time'] = end_time

        return self._request_with_params(GET, API_BORROW_RECORD_ISOLATED_URL, param, Auth.KEYED)

    def repayment_record_isolated(self, symbol: str, repay_id=None, currency=None, start_time=None, end_time=None, n=None):
        """Get Repayment Record(Isolated) (KEYED)
        Applicable to the inquiry of repayment records of isolated margin account

        GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/repay_record

        :param symbol: Trading pair (e.g. BMX_USDT)
        :param repay_id: Repayment ID
        :param currency: Currency
        :param start_time: Query start time: Timestamp
        :param end_time: Query end time: Timestamp
        :param n: Query record size, allowed range[1-100]. Default is 50
        :return:
        """
        param = {
            'symbol': symbol
        }

        if repay_id:
            param['repay_id'] = repay_id

        if currency:
            param['currency'] = currency

        if n:
            param['N'] = n

        if start_time:
            param['start_time'] = start_time

        if end_time:
            param['end_time'] = end_time
        return self._request_with_params(GET, API_REPAYMENT_RECORD_ISOLATED_URL, param, Auth.KEYED)

    def trading_pair_borrowing_rate_and_amount(self, symbol=None):
        """Get Trading Pair Borrowing Rate and Amount (KEYED)
        Applicable for checking the borrowing rate and borrowing amount of trading pairs

        GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/pairs

        :param symbol: It can be multiple-choice; if not filled in, then return all, like BTC_USDT, ETH_USDT
        :return:
        """
        param = {}

        if symbol:
            param['symbol'] = symbol

        return self._request_with_params(GET, API_TRADING_PAIR_BORROWING_RATE_AND_AMOUNT_URL, param, Auth.KEYED)
