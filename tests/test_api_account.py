import time

from bitmart.api_account import APIAccount
from tests import data as data

# account api
accountAPI = APIAccount(data.api_key, data.secret_key, data.memo, data.url)


def test_get_currencies():
    """Test GET https://api-cloud.bitmart.com/account/v1/currencie"""
    assert accountAPI.get_currencies()[0]['code'] == 1000
    assert accountAPI.get_currencies(currencies='BTC,ETH')[0]['code'] == 1000


def test_get_wallet():
    """Test GET https://api-cloud.bitmart.com/account/v1/wallet"""
    assert accountAPI.get_wallet(currency='BTC')[0]['code'] == 1000


def test_get_deposit_address():
    """Test GET https://api-cloud.bitmart.com/account/v1/deposit/address"""
    assert accountAPI.get_deposit_address(currency='USDT-ERC20')[0]['code'] == 1000

def test_get_withdraw_address():
    """Test GET https://api-cloud.bitmart.com/account/v1/withdraw/address/list"""
    assert accountAPI.get_withdraw_address()[0]['code'] == 1000


def test_get_withdraw_charge():
    """Test GET https://api-cloud.bitmart.com/account/v1/withdraw/charge"""
    assert accountAPI.get_withdraw_charge(currency='USDT-ERC20')[0]['code'] == 1000


def test_post_withdraw_apply():
    """Test POST https://api-cloud.bitmart.com/account/v1/withdraw/apply"""
    assert accountAPI.post_withdraw_apply(currency='USDT-ERC20', amount='40', destination='To Digital Address',
                                          address='0xe57b69a8776b37860407965B73cdFFBDFe668Bb5', address_memo='')[0][
               'code'] == 1000


def test_get_deposit_withdraw_history_v2():
    """Test GET https://api-cloud.bitmart.com/account/v2/deposit-withdraw/history"""
    after = int(time.time())
    before = after - 3600
    assert accountAPI.get_deposit_withdraw_history_v2(
        currency='USDT-ERC20', operation_type='withdraw', n=10, start_time=before, end_time=after)[0]['code'] == 1000


def test_get_deposit_withdraw_detail():
    """Test GET https://api-cloud.bitmart.com/account/v1/deposit-withdraw/detail"""
    assert accountAPI.get_deposit_withdraw_detail(id='1680001')[0]['code'] == 1000


def test_get_margin_account_details_isolated():
    """Test GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/account"""
    assert accountAPI.get_margin_account_details_isolated(
        symbol='BTC_USDT')[0]['code'] == 1000


def test_margin_asset_transfer():
    """Test POST https://api-cloud.bitmart.com/spot/v1/margin/isolated/transfer"""
    assert accountAPI.margin_asset_transfer(
        symbol='BTC_USDT', currency='BTC', amount='1', side='in')[0]['code'] == 1000


def test_get_basic_fee_rate():
    """Test GET https://api-cloud.bitmart.com/spot/v1/user_fee"""
    assert accountAPI.get_basic_fee_rate()[0]['code'] == 1000


def test_get_actual_trade_fee_rate():
    """Test GET https://api-cloud.bitmart.com/spot/v1/trade_fee"""
    assert accountAPI.get_actual_trade_fee_rate(
        symbol='BTC_USDT')[0]['code'] == 1000
