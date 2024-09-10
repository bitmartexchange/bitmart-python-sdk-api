import warnings

from bitmart.lib.cloud_client import CloudClient
from bitmart.lib.cloud_consts import *


class APISpot(CloudClient):

    def __init__(self, api_key: str = "", secret_key: str = "", memo: str = "", url: str = API_URL,
                 timeout: tuple = TIMEOUT, headers=None, logger=None):
        """
        Create api key from https://www.bitmart.com/api-config/en-US
        :param api_key: your access key
        :param secret_key: your secret key
        :param memo: your memo
        :param url: https://api-cloud.bitmart.com
        :param timeout: (2, 10)
        """
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout, headers, logger)

    # basic API
    def get_currencies(self):
        """
        Get a list of all cryptocurrencies on the platform

        GET https://api-cloud.bitmart.com/spot/v1/currencies
        :return:
        """
        return self._request_without_params(GET, API_SPOT_CURRENCIES_URL)

    def get_symbols(self):
        """
        Get a list of all trading pairs on the platform

        GET https://api-cloud.bitmart.com/spot/v1/symbols
        :return:
        """
        return self._request_without_params(GET, API_SPOT_SYMBOLS_URL)

    def get_symbol_detail(self):
        """
        Get a detailed list of all trading pairs on the platform

        GET https://api-cloud.bitmart.com/spot/v1/symbols/details
        :return:
        """
        return self._request_without_params(GET, API_SPOT_SYMBOLS_DETAILS_URL)

    def get_v3_tickers(self):
        """
        Get the quotations of all trading pairs, including: snapshot information of the latest transaction price, first bid price, first ask price and 24-hour trading volume.
            Note that the interface is not real-time data, if you need real-time data, please use websocket to subscribe Ticker channel

        GET https://api-cloud.bitmart.com/spot/quotation/v3/tickers
        :return:
        """
        return self._request_without_params(GET, API_SPOT_V3_TICKERS_URL)

    def get_v3_ticker(self, symbol: str):
        """
        Applicable to query the aggregated market price of a certain trading pair,
            and return the latest ticker information.
        Note that the interface is not real-time data, if you need real-time data,
         please use websocket to subscribe Ticker channel

        GET https://api-cloud.bitmart.com/spot/quotation/v3/ticker
        :param symbol: Trading pair (e.g. BMX_USDT)
        :return:
        """
        return self._request_with_params(GET, API_SPOT_V3_TICKER_URL, {'symbol': symbol})

    def get_v3_latest_kline(self, symbol: str, before=None, after=None, step=None, limit=None):
        """
        Query the latest K-line and return a maximum of 1000 data.
        Note that the latest K-line of the interface is not real-time data.
        If you want real-time data, please use websocket to subscribe to K-line channel


        GET https://api-cloud.bitmart.com/spot/quotation/v3/lite-klines

        :param symbol: Trading pair (e.g. BMX_USDT)
        :param before: Query timestamp (unit: second), query the data before this time
        :param after: Query timestamp (unit: second), query the data after this time
        :param step: k-line step, value [1, 3, 5, 15, 30, 45, 60, 120, 180, 240, 1440, 10080, 43200] unit: minute, default 1
        :param limit: Return number, the maximum value is 200, default is 100
        :return:
        """
        param = {
            'symbol': symbol,
        }

        if before:
            param['before'] = before

        if after:
            param['after'] = after

        if step:
            param['step'] = step

        if limit:
            param['limit'] = limit

        return self._request_with_params(GET, API_SPOT_V3_LATEST_KLINE_URL, param)

    def get_v3_history_kline(self, symbol: str, before=None, after=None, step=None, limit=None):
        """
        Get History K-Line (V3)

        Get k-line data within a specified time range of a specified trading pair.
        Note that the interface is not real-time data, if you need real-time data,
        please use websocket to subscribe KLine channel


        GET https://api-cloud.bitmart.com/spot/quotation/v3/klines

        :param symbol: Trading pair (e.g. BMX_USDT)
        :param before: Query timestamp (unit: second), query the data before this time
        :param after: Query timestamp (unit: second), query the data after this time
        :param step: k-line step, value [1, 3, 5, 15, 30, 45, 60, 120, 180, 240, 1440, 10080, 43200] unit: minute, default 1
        :param limit: Return number, the maximum value is 200, default is 100
        :return:
        """
        param = {
            'symbol': symbol,
        }

        if before:
            param['before'] = before

        if after:
            param['after'] = after

        if step:
            param['step'] = step

        if limit:
            param['limit'] = limit

        return self._request_with_params(GET, API_SPOT_V3_HISTORY_KLINE_URL, param)

    def get_v3_depth(self, symbol: str, limit=None):
        """
        Get full depth of trading pairs.
        Note that the interface is not real-time data, if you need real-time data,
         please use websocket to subscribe Depth channel



        GET https://api-cloud.bitmart.com/spot/quotation/v3/books

        :param symbol: Trading pair (e.g. BMX_USDT)
        :param limit: Order book depth per side. Maximum 50, e.g. 50 bids + 50 asks.
                        Default returns to 35 depth data, e.g. 35 bids + 35 asks.
        :return:
        """
        param = {
            'symbol': symbol
        }

        if limit:
            param['limit'] = limit

        return self._request_with_params(GET, API_SPOT_V3_BOOKS_URL, param)

    def get_v3_trades(self, symbol: str, limit=None):
        """
        Get the latest trade records of the specified trading pair.
            Note that the interface is not real-time data,
            if you need real-time data, please use websocket to subscribe Trade channel

        GET https://api-cloud.bitmart.com/spot/quotation/v3/trades

        :param symbol: Trading pair (e.g. BMX_USDT)
        :param limit: Number of returned items, maximum is 50, default 50
        :return:
        """
        param = {
            'symbol': symbol,
        }

        if limit:
            param['limit'] = limit
        return self._request_with_params(GET, API_SPOT_V3_TRADES_URL, param)

    # trade API

    def get_wallet(self):
        """Get Spot Wallet Balance (KEYED)
        Get the user's wallet balance for all currencies

        GET https://api-cloud.bitmart.com/spot/v1/wallet

        :return:
        """
        return self._request_without_params(GET, API_SPOT_WALLET_URL, Auth.KEYED)

    def post_submit_order(self, symbol: str, side: str, type: str, client_order_id='', size='', price='', notional=''):
        """
        Send in a new order.

        POST https://api-cloud.bitmart.com/spot/v2/submit_order
        :param symbol: Trading pair (e.g. BTC_USDT)
        :param side: -buy=Buy order -sell=Sell orde
        :param type: Order type -limit=Limit order -market=Market order -limit_maker=PostOnly order -ioc=IOC order
        :param client_order_id: Client-defined OrderId(A combination of numbers and letters, less than 32 bits)
        :param size: Quantity sold, required when selling at market price size
        :param price: Price
        :param notional: Quantity bought, required when buying at market price notional
        :return:
        """
        param = {
            'symbol': symbol,
            'side': side,
            'type': type
        }

        if client_order_id:
            param['client_order_id'] = client_order_id

        if size:
            param['size'] = size

        if price:
            param['price'] = price

        if notional:
            param['notional'] = notional

        return self._request_with_params(POST, API_SPOT_SUBMIT_ORDER_URL, param, Auth.SIGNED)

    def place_margin_order(self, symbol: str, side: str, type: str, client_order_id='', size='', price='',
                           notional=''):
        """
        Applicable for margin order placement

        POST https://api-cloud.bitmart.com/spot/v1/margin/submit_order

        :param symbol: Trading pair (e.g. BTC_USDT)
        :param side: -buy=Buy order  -sell=Sell order
        :param type: order type -limit=Limit order -market=Market order -limit_maker=PostOnly order -ioc=IOC order
        :param client_order_id: Client-defined OrderId(A combination of numbers and letters, less than 32 bits)
        :param size: Quantity sold, required when selling at market price size
        :param price: Price
        :param notional: Quantity bought, required when buying at market price notional
        :return:
        """
        param = {
            'symbol': symbol,
            'side': side,
            'type': type
        }

        if client_order_id:
            param['clientOrderId'] = client_order_id

        if size:
            param['size'] = size

        if price:
            param['price'] = price

        if notional:
            param['notional'] = notional

        return self._request_with_params(POST, API_SPOT_MARGIN_ORDER_URL, param, Auth.SIGNED)

    def post_cancel_order_by_orderid(self, symbol: str, order_id: str):
        """
        Applicable to the cancellation of a specified unfinished order

        POST https://api-cloud.bitmart.com/spot/v3/cancel_order

        :param symbol: Trading pair (e.g. BMX_USDT)
        :param order_id: Order ID
        :return:
        """
        param = {
            'symbol': symbol,
            'order_id': order_id
        }
        return self._request_with_params(POST, API_SPOT_CANCEL_ORDER_URL, param, Auth.SIGNED)

    def post_cancel_order_by_clientid(self, symbol: str, client_order_id: str):
        """
        Applicable to the cancellation of a specified unfinished order

        POST https://api-cloud.bitmart.com/spot/v3/cancel_order

        :param symbol: Trading pair (e.g. BMX_USDT)
        :param client_order_id: Client-defined Order ID
        :return:
        """
        param = {
            'symbol': symbol,
            'client_order_id': client_order_id
        }
        return self._request_with_params(POST, API_SPOT_CANCEL_ORDER_URL, param, Auth.SIGNED)

    def post_batch_orders(self, symbol: str, order_params: list, recv_window=None):
        """
        Batch order

        POST https://api-cloud.bitmart.com/spot/v4/batch_orders

        :param symbol: Trading pair (e.g. BTC_USDT)
        :param order_params: Order parameters, the number of transactions cannot exceed 10
        :param recv_window: Trade time limit, allowed range (0,60000], default: 5000 milliseconds
        :return:
        """
        param = {
            'symbol': symbol,
            'orderParams': order_params
        }

        if recv_window:
            param['recvWindow'] = recv_window

        return self._request_with_params(POST, API_SPOT_SUBMIT_BATCH_ORDERS_URL, param, Auth.SIGNED)

    def post_cancel_orders(self, symbol=None, order_ids: list = None, client_order_ids: list = None, recv_window=None):
        """
        Cancel all outstanding orders in the specified side for a trading pair

        POST https://api-cloud.bitmart.com/spot/v4/cancel_orders

        :param symbol: Trading pair (e.g. BTC_USDT)
        :param order_ids: Order Id List (Either orderIds or clientOrderIds must be provided)
        :param client_order_ids: Client-defined OrderId List (Either orderIds or clientOrderIds must be provided)
        :param recv_window: Trade time limit, allowed range (0,60000], default: 5000 milliseconds
        :return:
        """

        param = {
            'symbol': symbol
        }

        if order_ids:
            param['orderIds'] = order_ids

        if client_order_ids:
            param['clientOrderIds'] = client_order_ids

        if recv_window:
            param['recvWindow'] = recv_window

        return self._request_with_params(POST, API_SPOT_CANCEL_ORDERS_URL, param, Auth.SIGNED)

    def post_cancel_all_order(self, symbol=None, side=None):
        """
        Cancel all outstanding orders in the specified side for a trading pair

        POST https://api-cloud.bitmart.com/spot/v4/cancel_all

        :param symbol: Trading pair (e.g. BTC_USDT)
        :param side: Order side -buy -sell
        :return:
        """

        param = {}

        if symbol:
            param['symbol'] = symbol

        if side:
            param['side'] = side

        return self._request_with_params(POST, API_SPOT_CANCEL_ALL_ORDER_URL, param, Auth.SIGNED)

    def v4_query_order_by_id(self, order_id: str, query_state: str, recv_window=None):
        """
        Query a single order by orderId

        POST https://api-cloud.bitmart.com/spot/v4/query/order

        :param order_id: Order id
        :param query_state: Query Type
                    - open=Query order state [new, partially_filled]
                    - history=Query order state [filled, canceled, partially_canceled])
        :param recv_window: Trade time limit, allowed range (0,60000], default: 5000 milliseconds
        :return:
        """
        param = {
            'orderId': order_id
        }

        if query_state:
            param['queryState'] = query_state

        if recv_window:
            param['recvWindow'] = recv_window

        return self._request_with_params(POST, API_SPOT_V4_QUERY_ORDER_BY_ID_URL, param, Auth.SIGNED)

    def v4_query_order_by_order_client_id(self, client_order_id: str, query_state: str, recv_window=None):
        """
        Query a single order by clientOrderId.

        POST https://api-cloud.bitmart.com/spot/v4/query/client-order

        :param client_order_id: User-defined order id
        :param query_state: Query Type
                    - open=Query order state [new, partially_filled]
                    - history=Query order state [filled, canceled, partially_canceled])
        :param recv_window: Trade time limit, allowed range (0,60000], default: 5000 milliseconds
        :return:
        """
        param = {
            'clientOrderId': client_order_id
        }

        if query_state:
            param['queryState'] = query_state

        if recv_window:
            param['recvWindow'] = recv_window

        return self._request_with_params(POST, API_SPOT_V4_QUERY_ORDER_BY_CLIENT_ID_URL, param, Auth.SIGNED)

    def v4_query_open_orders(self, symbol=None, order_mode=None, start_time=None, end_time=None, limit=None,
                             recv_window=None):
        """
        Query the current opening order list of the account, only including state=[new, partially_filled] orders

        POST https://api-cloud.bitmart.com/spot/v4/query/open-orders

        :param symbol: Trading pair (e.g. BTC_USDT)
        :param order_mode: Order mode
                            - spot=spot trade
                            - iso_margin=isolated margin trade
        :param start_time: Start time in milliseconds, (e.g. 1681701557927)
        :param end_time: End time in milliseconds, (e.g. 1681701557927)
        :param limit: Number of queries, allowed range [1,200], default 200
        :param recv_window: Trade time limit, allowed range (0,60000], default: 5000 milliseconds
        :return:
        """
        param = {
        }

        if symbol:
            param['symbol'] = symbol

        if order_mode:
            param['orderMode'] = order_mode

        if start_time:
            param['startTime'] = start_time

        if end_time:
            param['endTime'] = end_time

        if limit:
            param['limit'] = limit

        if recv_window:
            param['recvWindow'] = recv_window

        return self._request_with_params(POST, API_SPOT_V4_QUERY_OPEN_ORDERS_URL, param, Auth.SIGNED)

    def v4_query_account_orders(self, symbol=None, order_mode=None, start_time=None, end_time=None, limit=None,
                                recv_window=None):
        """
        Query the account history order list, only including state=[filled, canceled, partially_canceled] orders

        POST https://api-cloud.bitmart.com/spot/v4/query/history-orders

        :param symbol: Trading pair (e.g. BTC_USDT)
        :param order_mode: Order mode
                            - spot=spot trade
                            - iso_margin=isolated margin trade
        :param start_time: Start time in milliseconds, (e.g. 1681701557927)
        :param end_time: End time in milliseconds, (e.g. 1681701557927)
        :param limit: Number of queries, allowed range [1,200], default 200
        :param recv_window: Trade time limit, allowed range (0,60000], default: 5000 milliseconds
        :return:
        """
        param = {
        }

        if symbol:
            param['symbol'] = symbol

        if order_mode:
            param['orderMode'] = order_mode

        if start_time:
            param['startTime'] = start_time

        if end_time:
            param['endTime'] = end_time

        if limit:
            param['limit'] = limit

        if recv_window:
            param['recvWindow'] = recv_window

        return self._request_with_params(POST, API_SPOT_V4_QUERY_HISTORY_ORDERS_URL, param, Auth.SIGNED)

    def v4_query_account_trade_list(self, symbol=None, order_mode=None, start_time=None, end_time=None, limit=None,
                                    recv_window=None):
        """
        Query all transaction records of the account

        POST https://api-cloud.bitmart.com/spot/v4/query/trades

        :param symbol: Trading pair (e.g. BTC_USDT)
        :param order_mode: Order mode
                            - spot=spot trade
                            - iso_margin=isolated margin trade
        :param start_time: Start time in milliseconds, (e.g. 1681701557927)
        :param end_time: End time in milliseconds, (e.g. 1681701557927)
        :param limit: Number of queries, allowed range [1,200], default 200
        :param recv_window: Trade time limit, allowed range (0,60000], default: 5000 milliseconds
        :return:
        """
        param = {
        }

        if symbol:
            param['symbol'] = symbol

        if order_mode:
            param['orderMode'] = order_mode

        if start_time:
            param['startTime'] = start_time

        if end_time:
            param['endTime'] = end_time

        if limit:
            param['limit'] = limit

        if recv_window:
            param['recvWindow'] = recv_window

        return self._request_with_params(POST, API_SPOT_V4_QUERY_TRADES_URL, param, Auth.SIGNED)

    def v4_query_order_trade_list(self, order_id: str, recv_window=None):
        """
        Query all transaction records of a single order

        POST https://api-cloud.bitmart.com/spot/v4/query/order-trades

        :param order_id: Order id
        :param recv_window: Trade time limit, allowed range (0,60000], default: 5000 milliseconds
        :return:
        """
        param = {
            'orderId': order_id
        }

        if recv_window:
            param['recvWindow'] = recv_window

        return self._request_with_params(POST, API_SPOT_V4_QUERY_ORDER_TRADES_URL, param, Auth.SIGNED)
