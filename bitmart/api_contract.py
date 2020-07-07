from .cloud_client import CloudClient
from .cloud_consts import *


class APIContract(CloudClient):

    def __init__(self, api_key, secret_key, memo, url=API_URL):
        CloudClient.__init__(self, api_key, secret_key, memo, url)

    # basic API
    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/contracts
    def get_contracts(self):
        param = {'exchange': 'bitmart'}
        return self._request_with_params(GET, API_CONTRACT_CURRENCIES_URL, param)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/pnls
    def get_pnls(self, contractId: int):
        param = {'contractID': contractId}
        return self._request_with_params(GET, API_CONTRACT_PNLS_URL, param)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/indexes
    def get_indexes(self):
        return self._request_without_params(GET, API_CONTRACT_INDEXES_URL)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/tickers
    def get_tickers(self, contractId: int):
        param = {}
        if contractId:
            param = {'contractID': contractId}
        return self._request_with_params(GET, API_CONTRACT_TICKERS_URL, param)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/quote
    def get_quote(self, contractId: int, startTime: int, endTime: int, unit: int, resolution: str):
        param = {'contractID': contractId, 'startTime': startTime, 'endTime': endTime, 'unit': unit, 'resolution': resolution}
        return self._request_with_params(GET, API_CONTRACT_QUOTE_URL, param)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/indexquote
    def get_index_quote(self, indexId: int, startTime, endTime, unit, resolution):
        param = {'indexID': indexId, 'startTime': startTime, 'endTime': endTime, 'unit': unit, 'resolution': resolution}
        return self._request_with_params(GET, API_CONTRACT_INDEX_QUOTE_URL, param)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/trades
    def get_trades(self, contractId: int):
        param = {'contractID': contractId}
        return self._request_with_params(GET, API_CONTRACT_TRADES_URL, param)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/depth
    def get_depth(self, contractId: int, count: int):
        param = {'contractID': contractId}
        if count:
            param['count'] = count
        return self._request_with_params(GET, API_CONTRACT_DEPTH_URL, param)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/fundingrate
    def get_funding_rate(self, contractId: int):
        param = {'contractID': contractId}
        return self._request_with_params(GET, API_CONTRACT_FUNDING_RATE_URL, param)

    # Order API
    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userOrders
    def get_user_orders(self, contractId: int, status, offset, size):
        param = {'contractID': contractId, 'status': status}
        if offset and size:
            param['offset'] = offset
            param['size'] = size
        return self._request_with_params(GET, API_CONTRACT_USER_ORDERS_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userOrderInfo
    def get_user_order_info(self, contractId: int, orderId: int):
        param = {'contractID': contractId, 'orderID': orderId}
        return self._request_with_params(GET, API_CONTRACT_USER_ORDER_INFO_URL, param, Auth.KEYED)

    # POST https://api-cloud.bitmart.com/contract/v1/ifcontract/submitOrder
    def post_submit_order(self, contractId: int, category: int, way: int, openType: int, leverage: int, customId, price, vol):
        param = {
            'contract_id': contractId,
            'category': category,
            'way': way,
            'open_type': openType,
            'leverage': leverage,
            'custom_id': customId,
            'price': price,
            'vol': vol
        }
        return self._request_with_params(POST, API_CONTRACT_USER_SUBMIT_ORDER_URL, param, Auth.SIGNED)

    # POST https://api-cloud.bitmart.com/contract/v1/ifcontract/batchOrders
    def post_submit_batch_order(self, orders):
        param = {'orders': orders}
        return self._request_with_params(POST, API_CONTRACT_USER_BATCH_ORDERS_URL, param, Auth.SIGNED)

    # POST https://api-cloud.bitmart.com/contract/v1/ifcontract/cancelOrders
    def post_cancel_order(self, contractId: int, orders):
        param = {'contractID': contractId, 'orders': orders}
        return self._request_with_params(POST, API_CONTRACT_CANCEL_ORDERS_URL, param, Auth.SIGNED)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userTrades
    def get_user_trades(self, contractId: int, offset: int, size: int):
        param = {'contractID': contractId}
        if offset:
            param['offset'] = offset
        if size:
            param['size'] = size
        return self._request_with_params(GET, API_CONTRACT_USER_TRADES_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/orderTrades
    def get_order_trades(self, contractId: int, orderId: int):
        param = {'contractID': contractId, 'orderID': orderId}
        return self._request_with_params(GET, API_CONTRACT_USER_TRADES_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/accounts
    def get_accounts(self, coinCode):
        param = {'coinCode': coinCode}
        return self._request_with_params(GET, API_CONTRACT_ACCOUNTS_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userPositions
    def get_user_positions(self, contractId: int):
        param = {'contractID': contractId}
        return self._request_with_params(GET, API_CONTRACT_USER_POSITIONS_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userLiqRecords
    def get_user_liq_records(self, contractId: int, orderId: int):
        param = {'contractID': contractId, 'orderID': orderId}
        return self._request_with_params(GET, API_CONTRACT_USER_LIQ_RECORDS_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/contract/v1/ifcontract/positionFee
    def get_position_fee(self, contractId: int, positionId: int):
        param = {'contractID': contractId, 'positionID': positionId}
        return self._request_with_params(GET, API_CONTRACT_POSITION_FEE_URL, param, Auth.KEYED)

    # POST https://api-cloud.bitmart.com/contract/v1/ifcontract/marginOper
    def post_margin_oper(self, contractId: int, positionId: int, vol: int, operType: int):
        param = {'contract_id': contractId, 'position_id': positionId, 'vol': vol, 'oper_type': operType}
        return self._request_with_params(POST, API_CONTRACT_MARGIN_OPER_URL, param, Auth.SIGNED)
