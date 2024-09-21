import logging
import time

from bitmart.api_spot import APISpot
from bitmart.lib.cloud_utils import config_logging
from tests import data as data

# spot api
config_logging(logging, logging.DEBUG)
spotAPI = APISpot(
    url=data.url, api_key=data.api_key, secret_key=data.secret_key, memo=data.memo, logger=logging)


def test_get_currencies():
    """Test GET https://api-cloud.bitmart.com/spot/v1/currencie"""
    assert spotAPI.get_currencies()[0]['code'] == 1000


def test_get_symbols():
    """Test GET https://api-cloud.bitmart.com/spot/v1/symbol"""
    assert spotAPI.get_symbols()[0]['code'] == 1000


def test_get_symbol_detail():
    """Test GET https://api-cloud.bitmart.com/spot/v1/symbols/details"""
    assert spotAPI.get_symbol_detail()[0]['code'] == 1000


def test_get_v3_tickers():
    """Test GET https://api-cloud.bitmart.com/spot/v2/ticker"""
    assert spotAPI.get_v3_tickers()[0]['code'] == 1000


def test_get_v3_ticker():
    """Test GET https://api-cloud.bitmart.com/spot/v1/ticker_detail"""
    assert spotAPI.get_v3_ticker(symbol='BTC_USDT')[0]['code'] == 1000


def test_get_v3_latest_kline():
    """Test GET https://api-cloud.bitmart.com/spot/quotation/v3/lite-klines"""
    before = int(time.time())
    after = before - 3600
    assert spotAPI.get_v3_latest_kline(symbol='BTC_USDT', before=before, after=after, step=60, limit=5)[0][
               'code'] == 1000


def test_get_v3_history_kline():
    """Test GET https://api-cloud.bitmart.com/spot/quotation/v3/klines"""
    before = int(time.time())
    after = before - 3600
    assert spotAPI.get_v3_history_kline(symbol='BTC_USDT', before=before, after=after, step=60, limit=5)[0][
               'code'] == 1000


def test_get_v3_depth():
    """Test GET https://api-cloud.bitmart.com/spot/quotation/v3/books"""
    assert spotAPI.get_v3_depth(symbol='BTC_USDT')[0]['code'] == 1000
    assert spotAPI.get_v3_depth(symbol='BTC_USDT', limit=1)[0]['code'] == 1000


def test_get_v3_trades():
    """Test GET https://api-cloud.bitmart.com/spot/v1/symbols/trades"""
    assert spotAPI.get_v3_trades(symbol='BTC_USDT', limit=1)[0]['code'] == 1000


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
    """Test POST https://api-cloud.bitmart.com/spot/v4/batch_orders"""
    order_params = [{"symbol": "BTC_USDT", "side": "buy", "type": "limit", "size": "0.01", "price": "8800"},
                    {"symbol": "BTC_USDT", "side": "buy", "type": "limit", "size": "0.01", "price": "8800"}]
    assert spotAPI.post_batch_orders(symbol='BTC_USDT', order_params=order_params)[0]['code'] == 1000


def test_post_cancel_order_by_orderid():
    """Test POST https://api-cloud.bitmart.com/spot/v3/cancel_order"""
    assert spotAPI.post_cancel_order_by_orderid(symbol='BTC_USDT', order_id='2147617164')[0]['code'] == 1000


def test_post_cancel_order_by_clientid():
    """Test POST https://api-cloud.bitmart.com/spot/v3/cancel_order"""
    assert spotAPI.post_cancel_order_by_clientid(symbol='BTC_USDT', client_order_id='ID125783')[0]['code'] == 1000


def test_post_cancel_orders():
    """Test POST https://api-cloud.bitmart.com/spot/v4/cancel_orders"""
    assert spotAPI.post_cancel_orders(symbol='BTC_USDT', order_ids=['sdfdsf4343', 'sdfdsa123'])[0]['code'] == 1000
    assert spotAPI.post_cancel_orders()[0]['code'] == 1000


def test_v4_query_order_by_id():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/order"""
    assert spotAPI.v4_query_order_by_id(order_id='118100034543076010', query_state='open')[0]['code'] == 1000


def test_v4_query_order_by_order_client_id():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/client-order"""
    assert spotAPI.v4_query_order_by_order_client_id(client_order_id='118100034543076010', query_state='open')[0][
               'code'] == 1000


def test_v4_query_open_orders():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/open-orders"""
    assert spotAPI.v4_query_open_orders()[0]['code'] == 1000
    assert spotAPI.v4_query_open_orders(symbol='BTC_USDT')[0]['code'] == 1000


def test_v4_query_account_orders():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/history-orders"""
    assert spotAPI.v4_query_account_orders()[0]['code'] == 1000
    assert spotAPI.v4_query_account_orders(symbol='BTC_USDT')[0]['code'] == 1000


def test_v4_query_account_trade_list():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/trades"""
    assert spotAPI.v4_query_account_trade_list()[0]['code'] == 1000
    assert spotAPI.v4_query_account_trade_list(symbol='BTC_USDT')[0]['code'] == 1000


def test_v4_query_order_trade_list():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/order-trades"""
    assert spotAPI.v4_query_order_trade_list(order_id='118100034543076010')[0]['code'] == 1000
