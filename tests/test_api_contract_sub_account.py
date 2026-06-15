import logging

from bitmart.api_contract_sub_account import APIContractSubAccount
from bitmart.lib.cloud_utils import config_logging
from tests import data as data

# contract sub-account api
config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)
subAPI = APIContractSubAccount(
    api_key=data.api_key,
    secret_key=data.secret_key,
    memo=data.memo,
    url=data.url,
    logger=logger,
)


def test_post_sub_to_main():
    """Test POST https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/sub-to-main"""
    assert subAPI.post_sub_to_main(
        request_no="uuid-0001", amount="1", currency="USDT", sub_account="subAccountName"
    )[0]["code"] == 1000


def test_post_sub_to_main_from_sub_account():
    """Test POST https://api-cloud-v2.bitmart.com/account/contract/sub-account/sub/v1/sub-to-main"""
    assert subAPI.post_sub_to_main_from_sub_account(
        request_no="uuid-0002", amount="1", currency="USDT"
    )[0]["code"] == 1000


def test_post_main_to_sub():
    """Test POST https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/main-to-sub"""
    assert subAPI.post_main_to_sub(
        request_no="uuid-0003", amount="1", currency="USDT", sub_account="subAccountName"
    )[0]["code"] == 1000


def test_get_sub_transfer_list():
    """Test GET https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/transfer-list"""
    assert subAPI.get_sub_transfer_list(sub_account="subAccountName", limit=10)[0]["code"] == 1000


def test_get_sub_transfer_history():
    """Test GET https://api-cloud-v2.bitmart.com/account/contract/sub-account/v1/transfer-history"""
    assert subAPI.get_sub_transfer_history(limit=10)[0]["code"] == 1000


def test_get_sub_wallet():
    """Test GET https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/wallet"""
    assert subAPI.get_sub_wallet(sub_account="subAccountName")[0]["code"] == 1000
    assert subAPI.get_sub_wallet(
        sub_account="subAccountName", currency="USDT"
    )[0]["code"] == 1000
