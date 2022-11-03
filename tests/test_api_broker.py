import time

from bitmart.api_broker import APIBroker
from tests import data as data

# broker api
brokerAPI = APIBroker(data.api_key, data.secret_key, data.memo, data.url, timeout=data.timeout)


def test_broker_rebate():
    """Test GET https://api-cloud.bitmart.com/spot/v1/broker/rebate"""
    assert brokerAPI.broker_rebates()[0]['code'] == 1000


def test_broker_rebate_by_timestamp():
    """Test GET https://api-cloud.bitmart.com/spot/v1/broker/rebate"""
    assert brokerAPI.broker_rebates_by_timestamp(
        start_time=int(time.time()) - 60 * 60 * 24 * 7, end_time=int(time.time()))[0]['code'] == 1000
