from bitmart.api_account import APIAccount
from bitmart.cloud_log import CloudLog
from tests import data as data

# account api
accountAPI = APIAccount(data.api_key, data.secret_key, data.memo, data.url)


# Close Request Printout
# CloudLog.set_logger_level(logger_level='info')

def test_get_currencies():
    """Test GET https://api-cloud.bitmart.com/account/v1/currencie"""
    assert accountAPI.get_currencies()[0]['code'] == 1000


def test_get_wallet():
    """Test GET https://api-cloud.bitmart.com/account/v1/wallet"""
    assert accountAPI.get_wallet(currency='BTC')[0]['code'] == 1000


def test_get_deposit_address():
    """Test GET https://api-cloud.bitmart.com/account/v1/deposit/address"""
    assert accountAPI.get_deposit_address(currency='USDT-ERC20')[0]['code'] == 1000


def test_get_withdraw_charge():
    """Test GET https://api-cloud.bitmart.com/account/v1/withdraw/charge"""
    assert accountAPI.get_withdraw_charge(currency='USDT-ERC20')[0]['code'] == 1000


def test_post_withdraw_apply():
    """Test POST https://api-cloud.bitmart.com/account/v1/withdraw/apply"""
    assert accountAPI.post_withdraw_apply(currency='USDT-ERC20', amount='40', destination='To Digital Address',
                                          address='0xe57b69a8776b37860407965B73cdFFBDFe668Bb5', address_memo='')[0][
               'code'] == 1000


def test_get_deposit_withdraw_history():
    """Test GET https://api-cloud.bitmart.com/account/v1/deposit-withdraw/history"""
    assert accountAPI.get_deposit_withdraw_history(
        currency='USDT-ERC20', operationType='withdraw', offset=1, limit=50)[0]['code'] == 1000


def test_get_deposit_withdraw_history_v2():
    """Test GET https://api-cloud.bitmart.com/account/v2/deposit-withdraw/history"""
    assert accountAPI.get_deposit_withdraw_history_v2(
        currency='USDT-ERC20', operationType='withdraw', N=10)[0]['code'] == 1000


def test_get_deposit_withdraw_detail():
    """Test GET https://api-cloud.bitmart.com/account/v1/deposit-withdraw/detail"""
    assert accountAPI.get_deposit_withdraw_detail(id='1680001')[0]['code'] == 1000
