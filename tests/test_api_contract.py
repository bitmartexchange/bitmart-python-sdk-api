from bitmart.api_contract import APIContract
from tests import data as data

# contract api
contractAPI = APIContract(data.api_key, data.secret_key, data.memo, data.url)
# contractAPI = APIContract(timeout=(2,10))


def test_get_details():
    """Test GET https://api-cloud.bitmart.com/contract/public/details"""
    assert contractAPI.get_details(contract_symbol='ETHUSDT')[0]['code'] == 1000


def test_get_depth():
    """Test GET https://api-cloud.bitmart.com/contract/public/depth"""
    assert contractAPI.get_depth(contract_symbol='ETHUSDT')[0]['code'] == 1000


def test_get_open_interest():
    """Test GET https://api-cloud.bitmart.com/contract/public/open-interest"""
    assert contractAPI.get_open_interest(contract_symbol='ETHUSDT')[0]['code'] == 1000


def test_get_funding_rate():
    """Test GET https://api-cloud.bitmart.com/contract/public/funding-rate"""
    assert contractAPI.get_funding_rate(contract_symbol='ETHUSDT')[0]['code'] == 1000


def test_get_kline():
    """Test GET https://api-cloud.bitmart.com/contract/public/kline"""
    assert contractAPI.get_kline(contract_symbol='ETHUSDT', step=5, start_time=1662518172, end_time=1662518172)[0][
               'code'] == 1000


# private
def test_get_assets_detail():
    """Test GET https://api-cloud.bitmart.com/contract/private/assets-detail"""
    assert contractAPI.get_assets_detail()[0][
               'code'] == 1000


def test_get_order():
    """Test GET https://api-cloud.bitmart.com/contract/private/order"""
    assert contractAPI.get_order(contract_symbol='BTCUSDT', order_id='220609666322019')[0][
               'code'] == 1000


def test_get_order_history():
    """Test GET https://api-cloud.bitmart.com/contract/private/order-history"""
    assert contractAPI.get_order_history(contract_symbol='BTCUSDT', start_time=1662368173, end_time=1662368179)[0][
               'code'] == 1000


def test_get_position():
    """Test GET https://api-cloud.bitmart.com/contract/private/position"""
    assert contractAPI.get_position(contract_symbol='BTCUSDT')[0][
               'code'] == 1000


def test_get_trades():
    """Test GET https://api-cloud.bitmart.com/contract/private/trades"""
    trades = contractAPI.get_trades(contract_symbol='BTCUSDT', start_time=1662368173, end_time=1662368179)
    assert trades[0]['success'] == True


def test_get_transfer_list():
    """Test POST https://api-cloud.bitmart.com/account/v1/transfer-contract-list"""
    trades = contractAPI.get_transfer_list(page=1, limit=10)
    assert trades[0]['success'] == True


def test_post_submit_order():
    """Test POST https://api-cloud.bitmart.com/contract/private/submit-order"""
    assert \
        contractAPI.post_submit_order(contract_symbol='BTCUSDT', side=4, type='limit', leverage='1',
                                      open_type='isolated',
                                      size=10, price='20000')[0][
            'code'] == 1000


def test_post_cancel_order():
    """Test POST https://api-cloud.bitmart.com/contract/private/cancel-order"""
    assert \
        contractAPI.post_cancel_order(contract_symbol='ETHUSDT', order_id='220906179559421')[0][
            'code'] == 1000


def test_post_cancel_orders():
    """Test POST https://api-cloud.bitmart.com/contract/private/cancel-orders"""
    assert \
        contractAPI.post_cancel_orders(contract_symbol='ETHUSDT')[0][
            'code'] == 1000


def test_post_submit_plan_order():
    """Test POST https://api-cloud.bitmart.com/contract/private/submit-plan-order"""
    assert \
        contractAPI.post_submit_plan_order(contract_symbol='BTCUSDT', type='limit', side=4,  leverage='1',
                                      open_type='isolated', mode=1, size=10, trigger_price='3000',
                                           price_type=1, price_way=1, executive_price='2800')[0][
            'code'] == 1000


def test_post_cancel_plan_order():
    """Test POST https://api-cloud.bitmart.com/contract/private/cancel-plan-order"""
    assert \
        contractAPI.post_cancel_plan_order(contract_symbol='BTCUSDT',order_id='230602272118231')[0][
            'code'] == 1000


def test_post_transfer():
    """Test POST https://api-cloud.bitmart.com/account/v1/transfer-contract"""
    assert \
        contractAPI.post_transfer(currency='USDT', amount='10', type='spot_to_contract')[0][
            'code'] == 1000
