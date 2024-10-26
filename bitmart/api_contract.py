from bitmart.lib.cloud_client import CloudClient
from bitmart.lib.cloud_consts import *


class APIContract(CloudClient):

    def __init__(self, api_key: str = "", secret_key: str = "", memo: str = "", url: str = API_V2_URL,
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
    def get_details(self, contract_symbol: str = None):
        """Get Contract Details
        Applicable to query contract details

        GET /contract/public/details

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {}
        if contract_symbol:
            param['symbol'] = contract_symbol
        return self._request_with_params(GET, API_CONTRACT_DETAILS_URL, param)

    def get_depth(self, contract_symbol):
        """Get Market Depth
        Get full depth of trading pairs.
        GET /contract/public/depth

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {'symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_DEPTH_URL, param)

    def get_open_interest(self, contract_symbol):
        """Get Futures Open Interest
        Applicable for querying the open interest and open interest value data of the specified contract

        GET /contract/public/open-interest

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {'symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_OPEN_INTEREST_URL, param)

    def get_funding_rate(self, contract_symbol):
        """Get Current Funding Rate
        Applicable for checking the current funding rate of a specified contract

        GET /contract/public/funding-rate

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {'symbol': contract_symbol}
        return self._request_with_params(GET, API_CONTRACT_FUNDING_RATE_URL, param)

    def get_kline(self, contract_symbol: str, step: int, start_time: int, end_time: int):
        """Get K-line
        Applicable for querying K-line data

        GET /contract/public/kline


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

    def get_trade_fee_rate(self, contract_symbol: str):
        """Get Trade Fee Rate (KEYED)
        Applicable for querying trade fee rate

        GET /contract/private/trade-fee-rate

        :return:
        """
        param = {
            'symbol': contract_symbol,
        }
        return self._request_with_params(GET, API_CONTRACT_TRADE_FEE_RATE_URL, param, Auth.KEYED)

    def get_assets_detail(self):
        """Get Contract Assets (KEYED)
        Applicable for querying user contract asset details

        GET /contract/private/assets-detail

        :return:
        """
        return self._request_without_params(GET, API_CONTRACT_ASSETS_DETAIL_URL, Auth.KEYED)

    def get_order(self, contract_symbol: str, order_id: str):
        """Get Order Detail (KEYED)
        Applicable for querying contract order detail

        GET /contract/private/order

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

        GET /contract/private/order-history

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

    def get_open_order(self, contract_symbol: str = None, type=None, order_state=None, limit=None):
        """Get All Open Orders (KEYED)
        Applicable for querying contract all open orders

        GET /contract/private/get-open-orders

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
        param = {}

        if contract_symbol:
            param['symbol'] = contract_symbol

        if type:
            param['type'] = type

        if order_state:
            param['order_state'] = order_state

        if limit:
            param['limit'] = limit
        return self._request_with_params(GET, API_CONTRACT_OPEN_ORDER_URL, param, Auth.KEYED)

    def get_current_plan_order(self,
                               contract_symbol: str = None,
                               type: str = None,
                               limit: int = None,
                               plan_type: str = None):
        """Get All Current Plan Orders (KEYED)
        Applicable for querying contract all plan orders

        GET /contract/private/current-plan-order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param type: Order type
                        -limit
                        - market
        :param limit: The number of returned results, with a maximum of 100 and a default of 100
        :param plan_type: Plan order type default all
                    -plan
                    - profit_loss
        :return:
        """
        param = {}

        if contract_symbol:
            param['symbol'] = contract_symbol

        if type:
            param['type'] = type

        if limit:
            param['limit'] = limit
        if plan_type:
            param['plan_type'] = plan_type
        return self._request_with_params(GET, API_CONTRACT_CURRENT_PLAN_ORDER_URL, param, Auth.KEYED)

    def get_position(self, contract_symbol: str = None):
        """Get Current Position (KEYED)
        Applicable for checking the position details a specified contract

        GET /contract/private/position


        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {}

        if contract_symbol:
            param['symbol'] = contract_symbol
        return self._request_with_params(GET, API_CONTRACT_POSITION_URL, param, Auth.KEYED)

    def get_position_risk(self, contract_symbol: str = None):
        """Get Current Position Risk Details(KEYED)
        Applicable for checking the position risk details a specified contract

        GET /contract/private/position-risk

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {}

        if contract_symbol:
            param['symbol'] = contract_symbol
        return self._request_with_params(GET, API_CONTRACT_POSITION_RISK_URL, param, Auth.KEYED)

    def get_trades(self, contract_symbol: str, start_time: int = None, end_time: int = None):
        """Get Order Trade (KEYED)
        Applicable for querying contract order trade detail

        GET /contract/private/trades

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param start_time: Start time, default is the last 7 days
        :param end_time: End time, default is the last 7 days
        :return:
        """
        param = {
            'symbol': contract_symbol,
        }

        if start_time:
            param['start_time'] = start_time
        if end_time:
            param['end_time'] = end_time

        return self._request_with_params(GET, API_CONTRACT_TRADES_URL, param, Auth.KEYED)

    def get_transfer_list(self, page: int, limit: int, currency=None, time_start=None, time_end=None, recv_window=None):
        """Get Transfer List (SIGNED)
        Query futures account transfer records

        POST /account/v1/transfer-contract-list


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

    def post_submit_order(self, contract_symbol: str, client_order_id: str = None,
                          type: str = None, side: int = None, leverage: str = None, open_type: str = None,
                          mode: int = None, price: str = None, size: int = None,
                          activation_price: str = None, callback_rate: str = None, activation_price_type: int = None,
                          preset_take_profit_price_type: int = None, preset_stop_loss_price_type: int = None,
                          preset_take_profit_price: str = None, preset_stop_loss_price: str = None
                          ):
        """Submit Order (SIGNED)
        Applicable for placing contract orders

        POST /contract/private/submit-order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param client_order_id: Client-defined OrderId(A combination of numbers and letters, less than 32 bits)
        :param type: Order type
                    -limit(default)
                    -market
                    -trailing
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
        :param price: Order price, required at limit order
        :param size: Order size. Size refers to the order amount in the unit of contracts
        :param activation_price: Activation price, required at trailing order
        :param callback_rate: Callback rate, required at trailing order, min 0.1, max 5 where 1 for 1%
        :param activation_price_type	: Activation price type, required at trailing order
                                            -1=last_price
                                            -2=fair_price
        :param preset_take_profit_price_type: Pre-set TP price type
                                            -1=last_price(default)
                                            -2=fair_price
        :param preset_stop_loss_price_type: Pre-set SL price type
                                            -1=last_price(default)
                                            -2=fair_price
        :param preset_take_profit_price: Pre-set TP price
        :param preset_stop_loss_price: Pre-set SL price
        :return:
        """
        param = {
            'symbol': contract_symbol,
        }

        if client_order_id:
            param['client_order_id'] = client_order_id
        if type:
            param['type'] = type
        if side:
            param['side'] = side
        if leverage:
            param['leverage'] = leverage
        if open_type:
            param['open_type'] = open_type
        if mode:
            param['mode'] = mode
        if price:
            param['price'] = price
        if size:
            param['size'] = size
        if activation_price:
            param['activation_price'] = activation_price
        if callback_rate:
            param['callback_rate'] = callback_rate
        if activation_price_type:
            param['activation_price_type'] = activation_price_type
        if preset_take_profit_price_type:
            param['preset_take_profit_price_type'] = preset_take_profit_price_type
        if preset_stop_loss_price_type:
            param['preset_stop_loss_price_type'] = preset_stop_loss_price_type
        if preset_take_profit_price:
            param['preset_take_profit_price'] = preset_take_profit_price
        if preset_stop_loss_price:
            param['preset_stop_loss_price'] = preset_stop_loss_price
        return self._request_with_params(POST, API_CONTRACT_SUBMIT_ORDER_URL, param, Auth.SIGNED)

    def post_cancel_order(self,
                          contract_symbol: str,
                          order_id: str = None,
                          client_order_id: str = None):
        """Cancel Order (SIGNED)
        Applicable for canceling a specific contract order

        POST /contract/private/cancel-order


        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param order_id: Order ID
        :param client_order_id: Client-defined OrderId
        :return:
        """
        param = {
            'symbol': contract_symbol,
        }

        if order_id:
            param['order_id'] = order_id
        if client_order_id:
            param['client_order_id'] = client_order_id
        return self._request_with_params(POST, API_CONTRACT_CANCEL_ORDER_URL, param, Auth.SIGNED)

    def post_cancel_orders(self, contract_symbol: str):
        """Cancel All Orders (SIGNED)
        Applicable for batch order cancellation under a particular contract

        POST /contract/private/cancel-orders

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :return:
        """
        param = {
            'symbol': contract_symbol,
        }
        return self._request_with_params(POST, API_CONTRACT_CANCEL_ORDERS_URL, param, Auth.SIGNED)

    def post_submit_plan_order(self, contract_symbol: str, type: str = None, side: int = None, leverage: str = None,
                               open_type: str = None, mode: int = None, size: int = None, trigger_price: str = None,
                               executive_price=None, price_way: int = None, price_type: int = None,
                               plan_category: int = None,
                               preset_take_profit_price_type: int = None, preset_stop_loss_price_type: int = None,
                               preset_take_profit_price: str = None, preset_stop_loss_price: str = None):
        """Submit Plan Order (SIGNED)
        Applicable for placing contract plan orders

        POST /contract/private/submit-plan-order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param type: Order type
                    -limit(default)
                    -market
                    -take_profit
                    -stop_loss
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
        :param executive_price: Order price, required at limit order
        :param trigger_price: Trigger price
        :param price_way: Yes	Price way
                -1=price_way_long
                -2=price_way_short
        :param price_type: Trigger price type
                -1=last_price
                -2=fair_price
        :param price_way: Price way
                            -1=price_way_long
                            -2=price_way_short
        :param price_type: Trigger price type
                            -1=last_price
                            -2=fair_price
        :param plan_category: TP/SL type
                            -1=TP/SL
                            -2=Position TP/SL
        :param preset_take_profit_price_type: Pre-set TP price type
                            -1=last_price(default)
                            -2=fair_price
        :param preset_stop_loss_price_type: Pre-set SL price type
                            -1=last_price(default)
                            -2=fair_price way
        :param preset_take_profit_price: Pre-set TP price
        :param preset_stop_loss_price: Pre-set SL price
        :return:
        """
        param = {
            'symbol': contract_symbol,
        }
        if type:
            param['type'] = type
        if side:
            param['side'] = side
        if leverage:
            param['leverage'] = leverage
        if open_type:
            param['open_type'] = open_type
        if mode:
            param['mode'] = mode
        if size:
            param['size'] = size
        if trigger_price:
            param['trigger_price'] = trigger_price
        if executive_price:
            param['executive_price'] = executive_price
        if price_way:
            param['price_way'] = price_way
        if price_type:
            param['price_type'] = price_type
        if plan_category:
            param['plan_category'] = plan_category
        if preset_take_profit_price_type:
            param['preset_take_profit_price_type'] = preset_take_profit_price_type
        if preset_stop_loss_price_type:
            param['preset_stop_loss_price_type'] = preset_stop_loss_price_type
        if preset_take_profit_price:
            param['preset_take_profit_price'] = preset_take_profit_price
        if preset_stop_loss_price:
            param['preset_stop_loss_price'] = preset_stop_loss_price
        return self._request_with_params(POST, API_CONTRACT_SUBMIT_PLAN_ORDER_URL, param, Auth.SIGNED)

    def post_cancel_plan_order(self, contract_symbol: str,
                               order_id: str = None,
                               client_order_id: str = None):
        """Cancel Plan Order (SIGNED)
        Applicable for canceling a specific contract plan order

        POST /contract/private/cancel-plan-order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param order_id: Order ID
        :param client_order_id: Client Order ID
        :return:
        """
        param = {
            'symbol': contract_symbol,
        }
        if order_id:
            param['order_id'] = order_id
        if client_order_id:
            param['client_order_id'] = client_order_id
        return self._request_with_params(POST, API_CONTRACT_CANCEL_PLAN_ORDER_URL, param, Auth.SIGNED)

    def post_transfer(self, currency: str, amount: str, type: str, recv_window=None):
        """Transfer (SIGNED)
        Transfer between spot account and contract account

        POST /account/v1/transfer-contract

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

    def post_submit_leverage(self, contract_symbol: str, open_type: str, leverage: str = None):
        """Submit Leverage (SIGNED)
        Applicable for adjust contract leverage

        POST /contract/private/submit-leverage

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

    def post_submit_tp_sl_order(self,
                                contract_symbol: str,
                                type: str,
                                side: int,
                                trigger_price: str,
                                executive_price: str,
                                price_type: int,
                                size: int = None,
                                plan_category: int = None,
                                client_order_id: str = None,
                                category: str = None):
        """Submit TP or SL Order (SIGNED)
        Applicable for placing contract TP or SL orders

        POST /contract/private/submit-tp-sl-order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param type: Order type
                        -take_profit
                        -stop_loss
        :param side: Order side
                    -2=buy_close_short
                    -3=sell_close_long
        :param trigger_price: Trigger price
        :param executive_price: Execution price
        :param price_type: Trigger price type
                            -1=last_price
                            -2=fair_price
        :param size: Order size (Number of contracts) Default the size of position
        :param plan_category: TP/SL type
                                -1=TP/SL(default)
                                -2=Position TP/SL
        :param client_order_id: Client order ID
        :param category: Trigger order type, position TP/SL default market
                            -limit
                            -market
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'type': type,
            'side': side,
            'trigger_price': trigger_price,
            'executive_price': executive_price,
            'price_type': price_type,
        }

        if size:
            param['size'] = size

        if plan_category:
            param['plan_category'] = plan_category

        if client_order_id:
            param['client_order_id'] = client_order_id

        if category:
            param['category'] = category

        return self._request_with_params(POST, API_CONTRACT_SUBMIT_TP_SL_ORDER_URL, param, Auth.SIGNED)

    def post_modify_plan_order(self,
                               contract_symbol: str,
                               trigger_price: str,
                               price_type: int,
                               type: str,
                               order_id: str = None,
                               client_order_id: str = None,
                               executive_price: str = None):
        """Modify Plan Order (SIGNED)
        Applicable for modifying contract plan orders


        POST /contract/private/modify-plan-order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param trigger_price: Trigger price
        :param price_type: type
                            -1=last_price
                            -2=fair_price
        :param type: Order type
                    -limit
                    -market
        :param order_id: Order ID(order_id or client_order_id must give one)
        :param client_order_id: Client order ID(order_id or client_order_id must give one)
        :param executive_price: Execution price for plan order, mandatory when type = limit
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'type': type,
            'trigger_price': trigger_price,
            'price_type': price_type,
        }

        if order_id:
            param['order_id'] = order_id

        if client_order_id:
            param['client_order_id'] = client_order_id

        if executive_price:
            param['executive_price'] = executive_price

        return self._request_with_params(POST, API_CONTRACT_MODIFY_PLAN_ORDER_URL, param, Auth.SIGNED)

    def post_modify_preset_plan_order(self,
                                      contract_symbol: str,
                                      order_id: str,
                                      preset_take_profit_price_type: int = None,
                                      preset_stop_loss_price_type: int = None,
                                      preset_take_profit_price: str = None,
                                      preset_stop_loss_price: str = None):
        """Modify Preset Plan Order (SIGNED)
        Applicable for modifying contract preset plan orders

        POST /contract/private/modify-preset-plan-order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param order_id: Order ID
        :param preset_take_profit_price_type: Pre-set TP price type
                                            -1=last_price(default)
                                            -2=fair_price
        :param preset_stop_loss_price_type: Pre-set SL price type
                                            -1=last_price(default)
                                            -2=fair_price
        :param preset_take_profit_price: Pre-set TP price
        :param preset_stop_loss_price: Pre-set SL price
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'order_id': order_id,
        }

        if preset_take_profit_price_type:
            param['preset_take_profit_price_type'] = preset_take_profit_price_type

        if preset_stop_loss_price_type:
            param['preset_stop_loss_price_type'] = preset_stop_loss_price_type

        if preset_take_profit_price:
            param['preset_take_profit_price'] = preset_take_profit_price

        if preset_stop_loss_price:
            param['preset_stop_loss_price'] = preset_stop_loss_price

        return self._request_with_params(POST, API_CONTRACT_MODIFY_PRESET_PLAN_ORDER_URL, param, Auth.SIGNED)

    def post_modify_tp_sl_order(self, contract_symbol: str,
                                trigger_price: str,
                                price_type: int,
                                order_id: str = None,
                                client_order_id: str = None,
                                executive_price: str = None,
                                plan_category: int = None,
                                category: str = None):
        """Modify TP/SL Order (SIGNED)
        Applicable for modifying TP/SL orders

        POST /contract/private/modify-tp-sl-order

        :param contract_symbol: Symbol of the contract(like BTCUSDT)
        :param trigger_price: Trigger price
        :param price_type: type
                            -1=last_price
                            -2=fair_price
        :param order_id: Order ID(order_id or client_order_id must give one)
        :param client_order_id: Client order ID(order_id or client_order_id must give one)
        :param executive_price: Execution price for order, mandatory when plan_category = 1
        :param plan_category: TP/SL type
                            -1=TP/SL
                            -2=Position TP/SL
        :param category: Order type, Position TP/SL default market
                        -limit
                        -market
        :return:
        """
        param = {
            'symbol': contract_symbol,
            'trigger_price': trigger_price,
            'price_type': price_type,
        }

        if order_id:
            param['order_id'] = order_id

        if client_order_id:
            param['client_order_id'] = client_order_id

        if executive_price:
            param['executive_price'] = executive_price

        if plan_category:
            param['plan_category'] = plan_category

        if category:
            param['category'] = category

        return self._request_with_params(POST, API_CONTRACT_MODIFY_TP_SL_ORDER_URL, param, Auth.SIGNED)
