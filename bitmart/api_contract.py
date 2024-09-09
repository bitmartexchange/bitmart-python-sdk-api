from bitmart.lib.cloud_client import CloudClient
from bitmart.lib.cloud_consts import *


class APIContract(CloudClient):

    def __init__(self, api_key: str = "", secret_key: str = "", memo: str = "", url: str = API_URL, timeout: tuple = TIMEOUT, logger=None):
        """
        Create api key from https://www.bitmart.com/api-config/en-US
        :param api_key: your access key
        :param secret_key: your secret key
        :param memo: your memo
        :param url: https://api-cloud.bitmart.com
        :param timeout: (2, 10)
        """
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout, logger)

    # basic API
    def get_details(self, contract_symbol):
        """Get Contract Details
        Applicable to query contract details

        GET https://api-cloud.bitmart.com/contract/public/details

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {'symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_DETAILS_URL, param)

    def get_depth(self, contract_symbol):
        """Get Market Depth
        Get full depth of trading pairs.
        GET https://api-cloud.bitmart.com/contract/public/depth

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {'symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_DEPTH_URL, param)

    def get_open_interest(self, contract_symbol):
        """Get Futures Open Interest
        Applicable for querying the open interest and open interest value data of the specified contract

        GET https://api-cloud.bitmart.com/contract/public/open-interest

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {'symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_OPEN_INTEREST_URL, param)

    def get_funding_rate(self, contract_symbol):
        """Get Current Funding Rate
        Applicable for checking the current funding rate of a specified contract

        GET https://api-cloud.bitmart.com/contract/public/funding-rate

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {'symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_FUNDING_RATE_URL, param)

    def get_kline(self, contract_symbol: str, step: int, start_time: int, end_time: int):
        """Get K-line
        Applicable for querying K-line data

        GET https://api-cloud.bitmart.com/contract/public/kline


        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param step: K-Line step, default is 1 minute. step: 1, 3, 5, 15, 30, 60, 120, 240, 360, 720, 1440, 4320, 10080
        :param start_time: Start time. Timestamps need to be in seconds
        :param end_time: End time. Timestamps need to be in seconds
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'step': step,
            'start_time': start_time,
            'end_time': end_time
        }
        return self._request_with_params(GET, API_CONTRACT_KLINE_URL, param)

    # private

    def get_assets_detail(self):
        """Get Contract Assets (KEYED)
        Applicable for querying user contract asset details

        GET https://api-cloud.bitmart.com/contract/private/assets-detail

        :return:
        """
        return self._request_without_params(GET, API_CONTRACT_ASSETS_DETAIL_URL, Auth.KEYED)

    def get_order(self, contract_symbol: str, order_id: str):
        """Get Order Detail (KEYED)
        Applicable for querying contract order detail

        GET https://api-cloud.bitmart.com/contract/private/order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param order_id: Order ID
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'order_id': order_id,
        }
        return self._request_with_params(GET, API_CONTRACT_ORDER_URL, param, Auth.KEYED)

    def get_order_history(self, contract_symbol: str, start_time: int, end_time: int):
        """Get Order History (KEYED)
        Applicable for querying contract order history

        GET https://api-cloud.bitmart.com/contract/private/order-history

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param start_time: Start time, default is the last 7 days
        :param end_time: End time, default is the last 7 days
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'start_time': start_time,
            'end_time': end_time,
        }
        return self._request_with_params(GET, API_CONTRACT_ORDER_HISTORY_URL, param, Auth.KEYED)

    def get_open_order(self, contract_symbol: str, type=None, order_state=None, limit=None):
        """Get All Open Orders (KEYED)
        Applicable for querying contract all open orders

        GET https://api-cloud.bitmart.com/contract/private/get-open-orders

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param type: Order type
                        -limit
                        - market
        :param order_state: Order state
                        -all(default)
                        - partially_filled
        :param limit: The number of returned results, with a maximum of 100 and a default of 100
        :return:
        """
        param = {
            'symbol': contract_symbol,
        }

        if type:
            param['type'] = type

        if order_state:
            param['order_state'] = order_state

        if limit:
            param['limit'] = limit
        return self._request_with_params(GET, API_CONTRACT_OPEN_ORDER_URL, param, Auth.KEYED)

    def get_position(self, contract_symbol: str):
        """Get Current Position (KEYED)
        Applicable for checking the position details a specified contract

        GET https://api-cloud.bitmart.com/contract/private/position


        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {
            'symbol': contract_symbol,
        }
        return self._request_with_params(GET, API_CONTRACT_POSITION_URL, param, Auth.KEYED)

    def get_trades(self, contract_symbol: str, start_time: int, end_time: int):
        """Get Order Trade (KEYED)
        Applicable for querying contract order trade detail

        GET https://api-cloud.bitmart.com/contract/private/trades

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param start_time: Start time, default is the last 7 days
        :param end_time: End time, default is the last 7 days
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'start_time': start_time,
            'end_time': end_time,
        }
        return self._request_with_params(GET, API_CONTRACT_TRADES_URL, param, Auth.KEYED)

    def get_transfer_list(self, page: int, limit: int, currency=None, time_start=None, time_end=None, recv_window=None):
        """Get Transfer List (SIGNED)
        Query futures account transfer records

        POST https://api-cloud.bitmart.com/account/v1/transfer-contract-list


        :param page: Number of pages, allowed range [1,1000]
        :param limit: Number of queries, allowed range [10,100]
        :param currency: Currency (like USDT)
        :param time_start: Start time in milliseconds, (e.g. 1681701557927)
        :param time_end: End time in milliseconds, (e.g. 1681701557927)
        :param recv_window: Trade time limit, allowed range (0,60000], default: 5000 milliseconds
        :return:
        """
        param = {
            'page': page,
            'limit': limit
        }

        if currency:
            param['currency'] = currency

        if time_start:
            param['time_start'] = time_start

        if time_end:
            param['time_end'] = time_end

        if recv_window:
            param['recvWindow'] = recv_window

        return self._request_with_params(POST, API_CONTRACT_TRANSFER_CONTRACT_LIST_URL, param, Auth.SIGNED)

    def post_submit_order(self, contract_symbol: str, type: str, side: int, leverage: str, open_type: str, price: str,
                          size: int, mode: int):
        """Submit Order (SIGNED)
        Applicable for placing contract orders

        POST https://api-cloud.bitmart.com/contract/private/submit-order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param type: Order type
                    -limit(default)
                    -market
        :param side: Order side
                    -1=buy_open_long
                    -2=buy_close_short
                    -3=sell_close_long
                    -4=sell_open_short
        :param leverage: Order leverage
        :param open_type: Open type, required at close position
                        -cross
                        -isolated
        :param price: Order price, required at limit order
        :param size: Order size. Size refers to the order amount in the unit of contracts
        :param mode: Order mode
                        -1=GTC(default)
                        -2=FOK
                        -3=IOC
                        -4=Maker Only
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'type': type,
            'side': side,
            'leverage': leverage,
            'open_type': open_type,
            'mode': mode,
            'price': price,
            'size': size
        }

        return self._request_with_params(POST, API_CONTRACT_SUBMIT_ORDER_URL, param, Auth.SIGNED)

    def post_cancel_order(self, contract_symbol: str, order_id: str):
        """Cancel Order (SIGNED)
        Applicable for canceling a specific contract order

        POST https://api-cloud.bitmart.com/contract/private/cancel-order


        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param order_id: Order ID
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'order_id': order_id,
        }
        return self._request_with_params(POST, API_CONTRACT_CANCEL_ORDER_URL, param, Auth.SIGNED)

    def post_cancel_orders(self, contract_symbol: str):
        """Cancel All Orders (SIGNED)
        Applicable for batch order cancellation under a particular contract

        POST https://api-cloud.bitmart.com/contract/private/cancel-orders

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {
            'symbol': contract_symbol,
        }
        return self._request_with_params(POST, API_CONTRACT_CANCEL_ORDERS_URL, param, Auth.SIGNED)

    def post_submit_plan_order(self, contract_symbol: str, type: str, side: int, leverage: str, open_type: str,
                               mode:int, size: int, trigger_price: str, price_way: int, price_type: int, executive_price=None):
        """Submit Plan Order (SIGNED)
        Applicable for placing contract plan orders

        POST https://api-cloud.bitmart.com/contract/private/submit-plan-order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param type: Order type
                    -limit(default)
                    -market
        :param side: Order side
                    -1=buy_open_long
                    -2=buy_close_short
                    -3=sell_close_long
                    -4=sell_open_short
        :param leverage: Order leverage
        :param open_type: Open type, required at close position
                        -cross
                        -isolated
        :param mode: Order mode
                    -1=GTC(default)
                    -2=FOK
                    -3=IOC
                    -4=Maker Only
        :param size: Order size. Size refers to the order amount in the unit of contracts
        :param trigger_price: Trigger price
        :param price_way: Yes	Price way
                -1=price_way_long
                -2=price_way_short
        :param price_type: Trigger price type
                -1=last_price
                -2=fair_price
        :param executive_price: Order price, required at limit order
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'type': type,
            'side': side,
            'leverage': leverage,
            'open_type': open_type,
            'mode': mode,
            'size': size,
            'trigger_price': trigger_price,
            'price_way': price_way,
            'price_type': price_type
        }

        if executive_price:
            param['executive_price'] = executive_price
        return self._request_with_params(POST, API_CONTRACT_SUBMIT_PLAN_ORDER_URL, param, Auth.SIGNED)

    def post_cancel_plan_order(self, contract_symbol: str, order_id: str):
        """Cancel Plan Order (SIGNED)
        Applicable for canceling a specific contract plan order

        POST https://api-cloud.bitmart.com/contract/private/cancel-plan-order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param order_id: Order ID
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'order_id': order_id,
        }
        return self._request_with_params(POST, API_CONTRACT_CANCEL_PLAN_ORDER_URL, param, Auth.SIGNED)

    def post_transfer(self, currency: str, amount: str, type: str, recv_window=None):
        """Transfer (SIGNED)
        Transfer between spot account and contract account

        POST https://api-cloud.bitmart.com/account/v1/transfer-contract

        :param currency: Currency (Only USDT is supported)
        :param amount: Transfer amount，allowed range[0.01,10000000000]
        :param type: Transfer type
                            -spot_to_contract
                            -contract_to_spot
        :param recv_window: Trade time limit, allowed range (0,60000], default: 5000 milliseconds
        :return:
        """
        param = {
            'currency': currency,
            'amount': amount,
            'type': type
        }

        if recv_window:
            param['recvWindow'] = recv_window

        return self._request_with_params(POST, API_CONTRACT_TRANSFER_CONTRACT_URL, param, Auth.SIGNED)

    def post_submit_leverage(self, contract_symbol: str, open_type: str, leverage=None):
        """Submit Leverage (SIGNED)
        Applicable for adjust contract leverage

        POST https://api-cloud.bitmart.com/contract/private/submit-leverage

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param open_type: Open type, required at close position
                            -cross
                            -isolated
        :param leverage: Order leverage
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'open_type': open_type,
        }

        if leverage:
            param['leverage'] = leverage

        return self._request_with_params(POST, API_CONTRACT_SUBMIT_LEVERAGE_URL, param, Auth.SIGNED)

