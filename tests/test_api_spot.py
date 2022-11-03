import time

from bitmart.api_spot import APISpot
from tests import data as data

# spot api
spotAPI = APISpot(data.api_key, data.secret_key, data.memo, data.url, timeout=data.timeout)


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
    """Test GET https://api-cloud.bitmart.com/spot/v2/ticker"""
    assert spotAPI.get_ticker()[0]['code'] == 1000


def test_get_ticker_detail():
    """Test GET https://api-cloud.bitmart.com/spot/v1/ticker_detail"""
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
    assert spotAPI.get_symbol_trades(symbol='BTC_USDT', N=1)[0]['code'] == 1000


def test_get_wallet():
    """Test GET https://api-cloud.bitmart.com/spot/v1/walle"""
    assert spotAPI.get_wallet()[0]['code'] == 1000


def test_post_submit_order():
    """Test POST https://api-cloud.bitmart.com/spot/v2/submit_order"""
    assert spotAPI.post_submit_order(symbol='BTC_USDT', side='buy', type='limit', size='0.01', price='8800')[0][
               'code'] == 1000


def test_margin_order():
    """Test POST https://api-cloud.bitmart.com/spot/v1/margin/submit_order"""
    assert spotAPI.place_margin_order(symbol='BTC_USDT', side='buy', type='limit', size='0.01', price='8800')[0][
               'code'] == 1000


def test_post_batch_orders():
    """Test POST https://api-cloud.bitmart.com/spot/v2/batch_orders"""
    order_params = [{"symbol": "BTC_USDT", "side": "buy", "type": "limit", "size": "0.01", "price": "8800"},
                    {"symbol": "BTC_USDT", "side": "buy", "type": "limit", "size": "0.01", "price": "8800"}]
    assert spotAPI.post_batch_orders(order_params=order_params)[0]['code'] == 1000


def test_post_cancel_order_by_orderid():
    """Test POST https://api-cloud.bitmart.com/spot/v3/cancel_order"""
    assert spotAPI.post_cancel_order_by_orderid(symbol='BTC_USDT', order_id='2147617164')[0]['code'] == 1000


def test_post_cancel_order_by_clientid():
    """Test POST https://api-cloud.bitmart.com/spot/v3/cancel_order"""
    assert spotAPI.post_cancel_order_by_clientid(symbol='BTC_USDT', client_order_id='ID125783')[0]['code'] == 1000


def test_post_cancel_orders():
    """Test POST https://api-cloud.bitmart.com/spot/v1/cancel_orders"""
    assert spotAPI.post_cancel_orders(symbol='BTC_USDT', side='buy')[0]['code'] == 1000


def test_get_user_order_detail():
    """Test GET https://api-cloud.bitmart.com/spot/v2/order_detail"""
    assert spotAPI.get_user_order_detail(order_id='2147617164')[0]['code'] == 1000


def test_get_user_orders_v2():
    """Test GET https://api-cloud.bitmart.com/spot/v3/orders"""
    assert spotAPI.get_user_orders(symbol='BTC_USDT', status="10")[0]['code'] == 1000


def test_get_user_orders_v2_by_time():
    """Test GET https://api-cloud.bitmart.com/spot/v3/orders"""
    assert spotAPI.get_user_orders_by_time(symbol='BTC_USDT', order_mode='spot', status='10', N=10,
                                           start_time=int(round(time.time() * 1000)) - 1000 * 60 * 60 * 24 * 7,
                                           end_time=int(round(time.time() * 1000)))[0]['code'] == 1000


def test_get_user_order_trades():
    """Test GET https://api-cloud.bitmart.com/spot/v2/trade"""
    assert spotAPI.get_user_order_trades(symbol='BTC_USDT', order_mode='spot', order_id='2147617164')[0]['code'] == 1000


def test_get_user_trades():
    """Test GET https://api-cloud.bitmart.com/spot/v2/trade"""
    assert spotAPI.get_user_trades(symbol='BTC_USDT', order_mode='spot')[0]['code'] == 1000


def test_get_user_trades_by_time():
    """Test GET https://api-cloud.bitmart.com/spot/v2/trade"""
    assert spotAPI.get_user_trades_by_time(symbol='BTC_USDT', order_mode='spot', N=10,
                                           start_time=int(round(time.time() * 1000)) - 1000 * 60 * 60 * 24 * 7,
                                           end_time=int(round(time.time() * 1000)))[0]['code'] == 1000
