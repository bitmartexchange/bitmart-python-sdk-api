import logging

from bitmart.api_finance import APIFinance
from bitmart.lib.cloud_utils import config_logging
from tests import data as data

# finance api
config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)
financeAPI = APIFinance(
    api_key=data.api_key,
    secret_key=data.secret_key,
    memo=data.memo,
    url=data.url,
    logger=logger,
)


def test_get_earn_assets():
    """Test GET https://api-cloud.bitmart.com/newearn/cloud/v1/earn"""
    assert financeAPI.get_earn_assets()[0]["code"] == 1000


def test_get_savings_product():
    """Test GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/product"""
    assert financeAPI.get_savings_product(current_page=1, size_page=10)[0]["code"] == 1000
    assert financeAPI.get_savings_product(
        current_page=1, size_page=10, coin_name="USDT")[0]["code"] == 1000


def test_post_savings_subscribe():
    """Test POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/subscribe"""
    assert financeAPI.post_savings_subscribe(
        product_id="1001", amount="100", request_no="20000009000000300000")[0]["code"] == 1000


def test_post_savings_redeem():
    """Test POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/redeem"""
    assert financeAPI.post_savings_redeem(
        earn_id="200001", amount="50", request_no="20000009000000300001")[0]["code"] == 1000


def test_get_savings_holdings():
    """Test GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/earn"""
    assert financeAPI.get_savings_holdings(current_page=1, size_page=10)[0]["code"] == 1000


def test_get_savings_records():
    """Test GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/record"""
    assert financeAPI.get_savings_records(
        type="subscribe", current_page=1, size_page=10)[0]["code"] == 1000


def test_get_fixed_product():
    """Test GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/product"""
    assert financeAPI.get_fixed_product(current_page=1, size_page=10)[0]["code"] == 1000


def test_post_fixed_subscribe():
    """Test POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/subscribe"""
    assert financeAPI.post_fixed_subscribe(
        product_id="2001", amount="10", request_no="20000009000000300002",
        auto_subscribe="OFF")[0]["code"] == 1000


def test_get_fixed_holdings():
    """Test GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/earn"""
    assert financeAPI.get_fixed_holdings(current_page=1, size_page=10)[0]["code"] == 1000


def test_get_fixed_records():
    """Test GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/record"""
    assert financeAPI.get_fixed_records(
        type="subscribe", current_page=1, size_page=10)[0]["code"] == 1000


def test_post_fixed_redeem():
    """Test POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/redeem"""
    assert financeAPI.post_fixed_redeem(
        earn_id="300001", request_no="20000009000000300003")[0]["code"] == 1000


def test_post_fixed_modify_auto_renewal():
    """Test POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/subscribe/operate"""
    assert financeAPI.post_fixed_modify_auto_renewal(
        earn_id="300001", auto_subscribe="REINVEST_FIXED")[0]["code"] == 1000


def test_post_auto_subscribe_toggle():
    """Test POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/subscribe/batch/operate"""
    assert financeAPI.post_auto_subscribe_toggle(auto_subscribe="open")[0]["code"] == 1000


def test_get_auto_subscribe_status():
    """Test GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/subscribe/batch"""
    assert financeAPI.get_auto_subscribe_status()[0]["code"] == 1000


def test_post_flexible_auto_subscribe_toggle():
    """Test POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/subscribe/operate"""
    assert financeAPI.post_flexible_auto_subscribe_toggle(
        product_id="1001", auto_subscribe="open")[0]["code"] == 1000


def test_get_flexible_auto_subscribe_status():
    """Test GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/subscribe/status"""
    assert financeAPI.get_flexible_auto_subscribe_status(product_id="1001")[0]["code"] == 1000
