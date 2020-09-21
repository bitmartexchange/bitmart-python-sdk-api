from bitmart.api_spot import APISpot
from tests import data as data

# spot api
spotAPI = APISpot(data.api_key, data.secret_key, data.memo, data.url)


def test_get_currencies():
    """Test GET https://api-cloud.bitmart.com/spot/v1/currencie"""
    assert spotAPI.get_currencies()[0]['code'] == 1000


def test_get_symbols():
    """Test GET https://api-cloud.bitmart.com/spot/v1/symbol"""
    assert spotAPI.get_symbols()[0]['code'] == 1000


def test_get_symbol_detail():
    """Test GET https://api-cloud.bitmart.com/spot/v1/symbols/details"""
    assert spotAPI.get_symbol_detail()[0]['code'] == 1000


def test_get_ticker():
    """Test GET https://api-cloud.bitmart.com/spot/v1/ticke"""
    assert spotAPI.get_ticker()[0]['code'] == 1000
    assert spotAPI.get_symbol_ticker(symbol='BTC_USDT')[0]['code'] == 1000


def test_get_steps():
    """Test GET https://api-cloud.bitmart.com/spot/v1/steps"""
    assert spotAPI.get_steps()[0]['code'] == 1000


def test_get_symbol_kline():
    """Test GET https://api-cloud.bitmart.com/spot/v1/symbols/kline"""
    assert spotAPI.get_symbol_kline(symbol='BTC_USDT', fromTime=1591789435, toTime=1591875835, step=60)[0][
               'code'] == 1000


def test_get_symbol_book():
    """Test GET https://api-cloud.bitmart.com/spot/v1/symbols/book"""
    assert spotAPI.get_symbol_book(symbol='BTC_USDT', precision=None, size=200)[0]['code'] == 1000


def test_get_symbol_trades():
    """Test GET https://api-cloud.bitmart.com/spot/v1/symbols/trades"""
    assert spotAPI.get_symbol_trades(symbol='BTC_USDT')[0]['code'] == 1000


def test_get_wallet():
    """Test GET https://api-cloud.bitmart.com/spot/v1/walle"""
    assert spotAPI.get_wallet()[0]['code'] == 1000


def test_post_submit_limit_buy_order():
    """Test POST https://api-cloud.bitmart.com/spot/v1/submit_order"""
    assert spotAPI.post_submit_limit_buy_order(symbol='BTC_USDT', size='0.01', price='8800')[0]['code'] == 1000


def test_post_submit_limit_sell_order():
    """Test POST https://api-cloud.bitmart.com/spot/v1/submit_order"""
    assert spotAPI.post_submit_limit_sell_order(symbol='BTC_USDT', size='0.01', price='8800')[0]['code'] == 1000


def test_post_submit_market_buy_order():
    """Test POST https://api-cloud.bitmart.com/spot/v1/submit_order"""
    assert spotAPI.post_submit_market_buy_order(symbol='BTC_USDT', notional='2')[0]['code'] == 1000


def test_post_submit_market_sell_order():
    """Test POST https://api-cloud.bitmart.com/spot/v1/submit_order"""
    assert spotAPI.post_submit_market_sell_order(symbol='BTC_USDT', size='10')[0]['code'] == 1000


def test_post_cancel_order():
    """Test POST https://api-cloud.bitmart.com/spot/v2/cancel_orde"""
    assert spotAPI.post_cancel_order(symbol='BTC_USDT', orderId=2147617164)[0]['code'] == 1000


def test_get_user_order_detail():
    """Test GET https://api-cloud.bitmart.com/spot/v1/order_detail"""
    assert spotAPI.get_user_order_detail(symbol='BTC_USDT', orderId=2147617164)[0]['code'] == 1000


def test_get_user_orders():
    """Test GET https://api-cloud.bitmart.com/spot/v1/orders"""
    assert spotAPI.get_user_orders(symbol='BTC_USDT', offset=1, limit=100, status="2")[0]['code'] == 1000


def test_get_user_order_trades():
    """Test GET https://api-cloud.bitmart.com/spot/v1/trade"""
    assert spotAPI.get_user_order_trades(symbol='BTC_USDT', orderId=2147617164)[0]['code'] == 1000


def test_get_user_trades():
    """Test GET https://api-cloud.bitmart.com/spot/v1/trade"""
    assert spotAPI.get_user_trades(symbol='BTC_USDT', offset=1, limit=10)[0]['code'] == 1000
