from bitmart.api_contract import APIContract
from tests import data as data

# contract api
contractAPI = APIContract(data.api_key, data.secret_key, data.memo, data.url)


def test_get_ticker():
    """Test GET https://api-cloud.bitmart.com/contract/v1/tickers"""
    assert contractAPI.get_ticker(contract_symbol='ETHUSDT')[0]['code'] == 1000
