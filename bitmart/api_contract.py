from .cloud_client import CloudClient
from .cloud_consts import *


class APIContract(CloudClient):

    def __init__(self, api_key, secret_key, memo, url: str = API_URL, timeout: tuple = TIMEOUT):
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout)

    # basic API
    # GET https://api-cloud.bitmart.com/contract/v1/tickers
    def get_ticker(self, contract_symbol):
        param = {'contract_symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_TICKER_URL, param)

    # GET https://api-cloud.bitmart.com/contract/public/details
    def get_details(self, contract_symbol):
        param = {'symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_DETAILS_URL, param)

    # GET https://api-cloud.bitmart.com/contract/public/depth
    def get_depth(self, contract_symbol):
        param = {'symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_DEPTH_URL, param)

    # GET https://api-cloud.bitmart.com/contract/public/open-interest
    def get_open_interest(self, contract_symbol):
        param = {'symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_OPEN_INTEREST_URL, param)

    # GET https://api-cloud.bitmart.com/contract/public/funding-rate
    def get_funding_rate(self, contract_symbol):
        param = {'symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_FUNDING_RATE_URL, param)

    # GET https://api-cloud.bitmart.com/contract/public/kline
    def get_kline(self, contract_symbol: str, step: int, start_time: int, end_time: int):
        param = {
            'symbol': contract_symbol,
            'step': step,
            'start_time': start_time,
            'end_time': end_time
        }
        return self._request_with_params(GET, API_CONTRACT_KLINE_URL, param)

    # private

    # GET https://api-cloud.bitmart.com/contract/private/assets-detail
    def get_assets_detail(self):
        return self._request_without_params(GET, API_CONTRACT_ASSETS_DETAIL_URL, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/contract/private/order
    def get_order(self, contract_symbol: str, order_id: str):
        param = {
            'symbol': contract_symbol,
            'order_id': order_id,
        }
        return self._request_with_params(GET, API_CONTRACT_ORDER_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/contract/private/order-history
    def get_order_history(self, contract_symbol: str, start_time: int, end_time: int):
        param = {
            'symbol': contract_symbol,
            'start_time': start_time,
            'end_time': end_time,
        }
        return self._request_with_params(GET, API_CONTRACT_ORDER_HISTORY_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/contract/private/position
    def get_position(self, contract_symbol: str):
        param = {
            'symbol': contract_symbol,
        }
        return self._request_with_params(GET, API_CONTRACT_POSITION_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/contract/private/trades
    def get_trades(self, contract_symbol: str, start_time: int, end_time: int):
        param = {
            'symbol': contract_symbol,
            'start_time': start_time,
            'end_time': end_time,
        }
        return self._request_with_params(GET, API_CONTRACT_TRADES_URL, param, Auth.KEYED)

    # POST https://api-cloud.bitmart.com/contract/private/submit-order
    def post_submit_order(self, contract_symbol: str, type: str, side: int, leverage: str, open_type: str, price: str,
                          size: int):
        param = {
            'symbol': contract_symbol,
            'type': type,
            'side': side,
            'leverage': leverage,
            'open_type': open_type,
            'price': price,
            'size': size
        }
        return self._request_with_params(POST, API_CONTRACT_SUBMIT_ORDER_URL, param, Auth.SIGNED)

    # POST https://api-cloud.bitmart.com/contract/private/cancel-order
    def post_cancel_order(self, contract_symbol: str, order_id: str):
        param = {
            'symbol': contract_symbol,
            'order_id': order_id,
        }
        return self._request_with_params(POST, API_CONTRACT_CANCEL_ORDER_URL, param, Auth.SIGNED)

    # POST https://api-cloud.bitmart.com/contract/private/cancel-orders
    def post_cancel_orders(self, contract_symbol: str):
        param = {
            'symbol': contract_symbol,
        }
        return self._request_with_params(POST, API_CONTRACT_CANCEL_ORDERS_URL, param, Auth.SIGNED)
