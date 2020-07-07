from bitmart.api_contract import APIContract
from tests import data as data

# contract api
contractAPI = APIContract(data.api_key, data.secret_key, data.memo, data.url)


def test_get_contracts():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/contracts"""
    assert contractAPI.get_contracts()[0]['code'] == 1000


def test_get_pnls():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/pnls"""
    assert contractAPI.get_pnls(contractId=1)[0]['code'] == 1000


def test_get_indexes():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/indexes"""
    assert contractAPI.get_indexes()[0]['code'] == 1000


def test_get_tickers():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/tickers"""
    assert contractAPI.get_tickers(None)[0]['code'] == 1000
    assert contractAPI.get_tickers(contractId=1)[0]['code'] == 1000


def test_get_quote():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/quote"""
    assert contractAPI.get_quote(contractId=1, startTime=1584343602, endTime=1585343602, unit=5, resolution='M')[0][
               'code'] == 1000


def test_get_index_quote():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/indexquote"""
    assert contractAPI.get_index_quote(indexId=1, startTime=1584343602, endTime=1585343602, unit=1, resolution='H')[0][
               'code'] == 1000


def test_get_trades():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/trades"""
    assert contractAPI.get_trades(contractId=1)[0]['code'] == 1000


def test_get_depth():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/depth"""
    assert contractAPI.get_depth(contractId=1, count=None)[0]['code'] == 1000
    assert contractAPI.get_depth(contractId=1, count=10)[0]['code'] == 1000


def test_get_funding_rate():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/fundingrate"""
    assert contractAPI.get_funding_rate(contractId=2)[0]['code'] == 1000


def test_get_user_orders():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userOrders"""
    assert contractAPI.get_user_orders(contractId=1, status=0, offset=None, size=None)[0]['code'] == 1000


def test_get_user_order_info():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userOrderInfo"""
    assert contractAPI.get_user_order_info(contractId=1, orderId=3816371425)[0]['code'] == 1000


def test_post_submit_order():
    """Test POST https://api-cloud.bitmart.com/contract/v1/ifcontract/submitOrder"""
    assert \
    contractAPI.post_submit_order(contractId=1, category=1, openType=1, way=1, leverage=50, customId=10, price=8885,
                                  vol=10)[0]['code'] == 1000


def test_post_submit_batch_order():
    """Test POST https://api-cloud.bitmart.com/contract/v1/ifcontract/batchOrders"""
    contractId = 1
    category = 1
    way = 1
    openType = 1
    leverage = 10
    customId = 100
    price = 9000
    vol = 1
    orders = [{
        'contract_id': contractId,
        'category': category,
        'way': way,
        'open_type': openType,
        'leverage': leverage,
        'custom_id': customId,
        'price': price,
        'vol': vol
    }, {
        'contract_id': contractId,
        'category': category,
        'way': way,
        'open_type': openType,
        'leverage': leverage,
        'custom_id': customId,
        'price': price,
        'vol': vol
    }]
    assert contractAPI.post_submit_batch_order(orders=orders)[0]['code'] == 1000


def test_post_cancel_order():
    """Test POST https://api-cloud.bitmart.com/contract/v1/ifcontract/cancelOrders"""
    cancel_orders = [
        {
            "contract_id": 1,
            "orders": [
                3844380441,
                3844380442
            ]
        }
    ]
    assert contractAPI.post_cancel_order(contractId=1, cancel_orders=cancel_orders)[0]['code'] == 1000


def test_get_user_trades():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userTrades"""
    assert contractAPI.get_user_trades(contractId=1, offset=None, size=None)[0]['code'] == 1000


def test_get_order_trades():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/orderTrades"""
    assert contractAPI.get_order_trades(contractId=1, orderId=3844380441)[0]['code'] == 1000


def test_get_accounts():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/accounts"""
    assert contractAPI.get_accounts(coinCode='USDT')[0]['code'] == 1000


def test_get_user_positions():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userPositions"""
    assert contractAPI.get_user_positions(contractId=1)[0]['code'] == 1000


def test_get_user_liq_records():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userLiqRecords"""
    assert contractAPI.get_user_liq_records(contractId=1, orderId=3816433968)[0]['code'] == 1000


def test_get_position_fee():
    """Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/positionFee"""
    assert contractAPI.get_position_fee(contractId=1, positionId=2802613453)[0]['code'] == 1000


def test_post_margin_oper():
    """Test POST https://api-cloud.bitmart.com/contract/v1/ifcontract/marginOper"""
    assert contractAPI.post_margin_oper(contractId=1, positionId=2802613453, vol=100, operType=1)[0]['code'] == 1000
