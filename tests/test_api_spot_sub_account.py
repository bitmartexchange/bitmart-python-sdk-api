from bitmart.api_spot_sub_account import APISpotSubAccount
from tests import data as data

# spot sub-account api
subAPI = APISpotSubAccount(data.api_key, data.secret_key, data.memo, data.url)


def test_post_sub_to_main():
    """Test POST https://api-cloud.bitmart.com/account/sub-account/main/v1/sub-to-main"""
    assert subAPI.post_sub_to_main(
        request_no='uuid-0001', amount='1', currency='USDT', sub_account='subAccountName')[0]['code'] == 1000


def test_post_sub_to_main_from_sub_account():
    """Test POST https://api-cloud.bitmart.com/account/sub-account/sub/v1/sub-to-main"""
    assert subAPI.post_sub_to_main_from_sub_account(
        request_no='uuid-0002', amount='1', currency='USDT')[0]['code'] == 1000


def test_post_main_to_sub():
    """Test POST https://api-cloud.bitmart.com/account/sub-account/main/v1/main-to-sub"""
    assert subAPI.post_main_to_sub(
        request_no='uuid-0003', amount='1', currency='USDT', sub_account='subAccountName')[0]['code'] == 1000


def test_post_sub_to_sub():
    """Test POST https://api-cloud.bitmart.com/account/sub-account/main/v1/sub-to-sub"""
    assert subAPI.post_sub_to_sub(
        request_no='uuid-0004', amount='1', currency='USDT',
        from_account='subA', to_account='subB')[0]['code'] == 1000


def test_get_sub_transfer_list():
    """Test GET https://api-cloud.bitmart.com/account/sub-account/main/v1/transfer-list"""
    assert subAPI.get_sub_transfer_list(move_type='spot to spot', n=10)[0]['code'] == 1000
    assert subAPI.get_sub_transfer_list(
        move_type='spot to spot', n=10, account_name='subAccountName')[0]['code'] == 1000


def test_get_account_transfer_history():
    """Test GET https://api-cloud.bitmart.com/account/sub-account/v1/transfer-history"""
    assert subAPI.get_account_transfer_history(move_type='spot to spot', n=10)[0]['code'] == 1000


def test_get_sub_spot_wallet():
    """Test GET https://api-cloud.bitmart.com/account/sub-account/main/v1/wallet"""
    assert subAPI.get_sub_spot_wallet(sub_account='subAccountName')[0]['code'] == 1000
    assert subAPI.get_sub_spot_wallet(
        sub_account='subAccountName', currency='USDT')[0]['code'] == 1000


def test_get_sub_account_list():
    """Test GET https://api-cloud.bitmart.com/account/sub-account/main/v1/subaccount-list"""
    assert subAPI.get_sub_account_list()[0]['code'] == 1000
