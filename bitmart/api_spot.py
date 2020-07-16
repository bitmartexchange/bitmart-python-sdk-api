from .cloud_client import CloudClient
from .cloud_consts import *


class APISpot(CloudClient):

    def __init__(self, api_key, secret_key, memo, url=API_URL):
        CloudClient.__init__(self, api_key, secret_key, memo, url)

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
    def get_symbol_book(self, symbol: str, precision: int):
        param = {
            'symbol': symbol
        }
        if precision:
            param['precision'] = precision
        return self._request_with_params(GET, API_SPOT_SYMBOLS_BOOK_URL, param)

    # GET https://api-cloud.bitmart.com/spot/v1/symbols/trades
    def get_symbol_trades(self, symbol: str):
        param = {
            'symbol': symbol
        }
        return self._request_with_params(GET, API_SPOT_SYMBOLS_TRADES_URL, param)

    # trade API

    # GET https://api-cloud.bitmart.com/spot/v1/wallet
    def get_wallet(self):
        return self._request_without_params(GET, API_SPOT_WALLET_URL, Auth.KEYED)

    # POST https://api-cloud.bitmart.com/spot/v1/submit_order
    def post_submit_limit_buy_order(self, symbol: str, size='', price=''):
        param = {
            'symbol': symbol,
            'side': 'buy',
            'type': 'limit',
            'size': size,
            'price': price
        }
        return self._request_with_params(POST, API_SPOT_SUBMIT_ORDER_URL, param, Auth.SIGNED)

    def post_submit_limit_sell_order(self, symbol: str, size='', price=''):
        param = {
            'symbol': symbol,
            'side': 'sell',
            'type': 'limit',
            'size': size,
            'price': price
        }
        return self._request_with_params(POST, API_SPOT_SUBMIT_ORDER_URL, param, Auth.SIGNED)

    def post_submit_market_sell_order(self, symbol: str, size=''):
        param = {
            'symbol': symbol,
            'side': 'sell',
            'type': 'market',
            'size': size
        }
        return self._request_with_params(POST, API_SPOT_SUBMIT_ORDER_URL, param, Auth.SIGNED)

    def post_submit_market_buy_order(self, symbol: str, notional=''):
        param = {
            'symbol': symbol,
            'side': 'buy',
            'type': 'market',
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
