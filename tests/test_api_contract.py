import logging
import time

from bitmart.api_contract import APIContract
from bitmart.lib import cloud_consts
from bitmart.lib.cloud_utils import config_logging
from tests import data as data

# contract api
config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)
contractAPI = APIContract(api_key=data.api_key, secret_key=data.secret_key, memo=data.memo, url=data.url, logger=logger)


# contractAPI = APIContract(timeout=(2,10))


def test_get_details():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/details"""
    assert contractAPI.get_details(contract_symbol='ETHUSDT')[0]['code'] == 1000


def test_get_depth():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/depth"""
    assert contractAPI.get_depth(contract_symbol='ETHUSDT')[0]['code'] == 1000


def test_get_open_interest():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/open-interest"""
    assert contractAPI.get_open_interest(contract_symbol='ETHUSDT')[0]['code'] == 1000


def test_get_funding_rate():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/funding-rate"""
    assert contractAPI.get_funding_rate(contract_symbol='ETHUSDT')[0]['code'] == 1000


def test_get_kline():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/kline"""
    end_time = int(time.time())
    start_time = end_time - 3600
    assert contractAPI.get_kline(contract_symbol='ETHUSDT', step=5, start_time=start_time, end_time=end_time)[0][
               'code'] == 1000


def test_get_mark_price_kline():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/markprice-kline"""
    end_time = int(time.time())
    start_time = end_time - 3600
    assert \
        contractAPI.get_mark_price_kline(contract_symbol='ETHUSDT', step=5, start_time=start_time, end_time=end_time)[
            0][
            'code'] == 1000


def test_get_fund_rate_history():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/funding-rate-history"""
    assert contractAPI.get_fund_rate_history(contract_symbol='ETHUSDT', limit=10)[0][
               'code'] == 1000


# private

def test_get_trade_fee_rate():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/trade-fee-rate"""
    assert contractAPI.get_trade_fee_rate(contract_symbol='BTCUSDT')[0][
               'code'] == 1000


def test_get_assets_detail():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/assets-detail"""
    assert contractAPI.get_assets_detail()[0][
               'code'] == 1000


def test_get_order():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/order"""
    assert contractAPI.get_order(contract_symbol='BTCUSDT', order_id='220609666322019')[0][
               'code'] == 1000


def test_get_order_history():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/order-history"""
    assert contractAPI.get_order_history(contract_symbol='BTCUSDT', start_time=1662368173, end_time=1662368179)[0][
               'code'] == 1000


def test_get_open_order():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/get-open-orders"""
    assert contractAPI.get_open_order(contract_symbol='BTCUSDT', type='limit', order_state='all', limit=5)[0][
               'code'] == 1000


def test_get_current_plan_order():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/current-plan-order"""
    assert contractAPI.get_current_plan_order()[0][
               'code'] == 1000

    assert contractAPI.get_current_plan_order(contract_symbol='BTCUSDT')[0][
               'code'] == 1000


def test_get_position():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/position"""
    assert contractAPI.get_position(contract_symbol='BTCUSDT')[0][
               'code'] == 1000


def test_get_trades():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/trades"""
    trades = contractAPI.get_trades(contract_symbol='BTCUSDT', start_time=1662368173, end_time=1662368179)
    assert trades[0]['code'] == 1000


def test_get_transaction_history():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/transaction-history"""
    trades = contractAPI.get_transaction_history(contract_symbol='BTCUSDT', start_time=1662368173, end_time=1662368179)
    assert trades[0]['code'] == 1000


def test_get_transfer_list():
    """Test POST https://api-cloud-v2.bitmart.com/account/v1/transfer-contract-list"""
    trades = contractAPI.get_transfer_list(page=1, limit=10)
    assert trades[0]['code'] == 1000


def test_post_submit_order():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/submit-order"""
    response = contractAPI.post_submit_order(contract_symbol='BTCUSDT', side=1, type='limit', leverage='20',
                                             open_type='isolated',
                                             size=1, price='78000', mode=1, stp_mode=2)
    print(response)
    assert response[0]['code'] == 1000


def test_post_modify_limit_order():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/modify-limit-order"""
    response = contractAPI.post_modify_limit_order(contract_symbol='BTCUSDT', order_id=62970000003, price='77000')
    assert response[0]['code'] == 1000


def test_post_cancel_order():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/cancel-order"""
    assert \
        contractAPI.post_cancel_order(contract_symbol='ETHUSDT', order_id='220906179559421')[0][
            'code'] == 1000

    assert \
        contractAPI.post_cancel_order(contract_symbol='ETHUSDT')[0][
            'code'] == 1000

    assert \
        contractAPI.post_cancel_order(contract_symbol='ETHUSDT', client_order_id='220906179559421')[0][
            'code'] == 1000


def test_post_cancel_orders():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/cancel-orders"""
    assert \
        contractAPI.post_cancel_orders(contract_symbol='ETHUSDT')[0][
            'code'] == 1000


def test_post_submit_plan_order():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/submit-plan-order"""
    assert \
        contractAPI.post_submit_plan_order(contract_symbol='BTCUSDT', type='limit', side=4, leverage='1',
                                           open_type='isolated', mode=1, size=10, trigger_price='3000',
                                           price_type=1, price_way=1, executive_price='2800')[0][
            'code'] == 1000


def test_post_cancel_plan_order():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/cancel-plan-order"""
    assert \
        contractAPI.post_cancel_plan_order(contract_symbol='BTCUSDT')[0][
            'code'] == 1000

    assert \
        contractAPI.post_cancel_plan_order(contract_symbol='BTCUSDT', order_id='230602272118231')[0][
            'code'] == 1000

    assert \
        contractAPI.post_cancel_plan_order(contract_symbol='BTCUSDT', client_order_id='230602272118231')[0][
            'code'] == 1000


def test_post_transfer():
    """Test POST https://api-cloud-v2.bitmart.com/account/v1/transfer-contract"""
    assert \
        contractAPI.post_transfer(currency='USDT', amount='10', type='spot_to_contract')[0][
            'code'] == 1000


def test_post_submit_leverage():
    """POST https://api-cloud-v2.bitmart.com/contract/private/submit-leverage"""
    assert \
        contractAPI.post_submit_leverage(contract_symbol='BTCUSDT', open_type='cross', leverage="1")[0][
            'code'] == 1000


def test_post_submit_tp_or_sl_order():
    """POST https://api-cloud-v2.bitmart.com/contract/private/submit-tp-sl-order"""
    assert \
        contractAPI.post_submit_tp_sl_order(
            contract_symbol='BTCUSDT',
            side=2,
            type="take_profit",
            size=10,
            trigger_price="2000",
            executive_price="1450",
            price_type=1,
            plan_category=1,
            client_order_id="12314323424",
            category="limit"
        )[0]['code'] == 1000


def test_post_modify_plan_order():
    """POST https://api-cloud-v2.bitmart.com/contract/private/modify-plan-order"""
    assert \
        contractAPI.post_modify_plan_order(
            contract_symbol='BTCUSDT',
            trigger_price="2000",
            executive_price="1450",
            price_type=1,
            type="limit"
        )[0]['code'] == 1000


def test_post_modify_preset_plan_order():
    """POST https://api-cloud-v2.bitmart.com/contract/private/modify-preset-plan-order"""
    assert \
        contractAPI.post_modify_preset_plan_order(
            contract_symbol='BTCUSDT',
            order_id="12314323424",
            preset_take_profit_price="2000",
            preset_stop_loss_price="1450",
            preset_take_profit_price_type=1,
            preset_stop_loss_price_type=1,
        )[0]['code'] == 1000


def test_post_modify_tp_sl_order():
    """POST https://api-cloud-v2.bitmart.com/contract/private/modify-tp-sl-order"""
    assert \
        contractAPI.post_modify_tp_sl_order(
            contract_symbol='BTCUSDT',
            order_id="12314323424",
            trigger_price="2000",
            executive_price="2100",
            price_type=2,
            plan_category=2,
            category="limit",
        )[0]['code'] == 1000


def test_post_submit_trail_order():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/submit-trail-order"""
    response = contractAPI.post_submit_trail_order(contract_symbol='BTCUSDT', side=4, leverage='20',
                                                   open_type='cross', size=10, activation_price='20000',
                                                   callback_rate='1', activation_price_type=1)
    assert response[0]['code'] == 1000


def test_post_cancel_trail_order():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/cancel-trail-order"""
    assert \
        contractAPI.post_cancel_trail_order(contract_symbol='ETHUSDT')[0][
            'code'] == 1000
