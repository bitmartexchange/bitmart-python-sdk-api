from .cloud_client import CloudClient
from .cloud_consts import *


class APISpot(CloudClient):

    def __init__(self, api_key, secret_key, memo,  url: str = API_URL, timeout: tuple = TIMEOUT):
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout)

    # basic API
    # GET https://api-cloud.bitmart.com/spot/v1/currencies
    def get_currencies(self):
        return self._request_without_params(GET, API_SPOT_CURRENCIES_URL)

    # GET https://api-cloud.bitmart.com/spot/v1/symbols
    def get_symbols(self):
        return self._request_without_params(GET, API_SPOT_SYMBOLS_URL)

    # GET https://api-cloud.bitmart.com/spot/v1/symbols/details
    def get_symbol_detail(self):
        return self._request_without_params(GET, API_SPOT_SYMBOLS_DETAILS_URL)

    # GET https://api-cloud.bitmart.com/spot/v1/ticker
    def get_ticker(self):
        return self._request_without_params(GET, API_SPOT_TICKER_URL)

    def get_symbol_ticker(self, symbol: str):
        return self._request_with_params(GET, API_SPOT_TICKER_URL, {'symbol': symbol})

    # GET https://api-cloud.bitmart.com/spot/v1/steps
    def get_steps(self):
        return self._request_without_params(GET, API_SPOT_STEPS_URL)

    # GET https://api-cloud.bitmart.com/spot/v1/symbols/kline
    def get_symbol_kline(self, symbol: str, fromTime: int, toTime: int, step: int = 1):
        param = {
            'symbol': symbol,
            'from': fromTime,
            'to': toTime,
            'step': step
        }
        return self._request_with_params(GET, API_SPOT_SYMBOLS_KLINE_URL, param)

    # GET https://api-cloud.bitmart.com/spot/v1/symbols/book
    def get_symbol_book(self, symbol: str, precision: int, size: int):
        param = {
            'symbol': symbol
        }

        if precision:
            param['precision'] = precision

        if size:
            param['size'] = size
        return self._request_with_params(GET, API_SPOT_SYMBOLS_BOOK_URL, param)

    # GET https://api-cloud.bitmart.com/spot/v1/symbols/trades
    def get_symbol_trades(self, symbol: str, N: int = 50):
        param = {
            'symbol': symbol,
            'N': N
        }
        return self._request_with_params(GET, API_SPOT_SYMBOLS_TRADES_URL, param)

    # trade API

    # GET https://api-cloud.bitmart.com/spot/v1/wallet
    def get_wallet(self):
        return self._request_without_params(GET, API_SPOT_WALLET_URL, Auth.KEYED)

    # POST https://api-cloud.bitmart.com/spot/v1/batch_orders
    def post_batch_orders(self, orderParams: list):
        param = {
            'orderParams': orderParams
        }
        return self._request_with_params(POST, API_SPOT_SUBMIT_BATCH_ORDERS_URL, param, Auth.SIGNED)

    # POST https://api-cloud.bitmart.com/spot/v1/submit_order
    def post_submit_order(self, symbol: str, side: str, type: str, size='', price='', notional=''):
        param = {
            'symbol': symbol,
            'side': side,
            'type': type,
            'size': size,
            'price': price,
            'notional': notional
        }
        return self._request_with_params(POST, API_SPOT_SUBMIT_ORDER_URL, param, Auth.SIGNED)

    # POST https://api-cloud.bitmart.com/spot/v2/cancel_order
    def post_cancel_order(self, symbol: str, orderId: int):
        param = {
            'symbol': symbol,
            'order_id': orderId
        }
        return self._request_with_params(POST, API_SPOT_CANCEL_ORDER_URL, param, Auth.SIGNED)

    # POST https://api-cloud.bitmart.com/spot/v1/cancel_orders
    def post_cancel_orders(self, symbol: str, side: str):
        param = {
            'symbol': symbol,
            'side': side
        }
        return self._request_with_params(POST, API_SPOT_CANCEL_ORDERS_URL, param, Auth.SIGNED)

    # GET https://api-cloud.bitmart.com/spot/v1/order_detail
    def get_user_order_detail(self, symbol: str, orderId: int):
        param = {
            'symbol': symbol,
            'order_id': orderId
        }
        return self._request_with_params(GET, API_SPOT_ORDER_DETAIL_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/spot/v1/orders
    def get_user_orders(self, symbol: str, offset: int, limit: int, status: str):
        param = {
            'symbol': symbol,
            'offset': offset,
            'limit': limit,
            'status': status
        }
        return self._request_with_params(GET, API_SPOT_ORDERS_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/spot/v2/orders
    def get_user_orders_v2(self, symbol: str, status: str, N: int):
        param = {
            'symbol': symbol,
            'N': N,
            'status': status
        }
        return self._request_with_params(GET, API_SPOT_ORDERS_V2_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/spot/v1/trades
    def get_user_order_trades(self, symbol: str, orderId: int):
        param = {
            'symbol': symbol,
            'order_id': orderId
        }
        return self._request_with_params(GET, API_SPOT_TRADES_URL, param, Auth.KEYED)

    def get_user_trades(self, symbol: str, offset: int, limit: int):
        param = {
            'symbol': symbol,
            'offset': offset,
            'limit': limit
        }
        return self._request_with_params(GET, API_SPOT_TRADES_URL, param, Auth.KEYED)
