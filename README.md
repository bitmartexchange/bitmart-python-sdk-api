[![Logo](https://img.bitmart.com/static-file/public/sdk/sdk_logo.png)](https://bitmart.com)

BitMart-Python-SDK-API
=========================
[![PyPI version](https://img.shields.io/badge/pypi-v1.0.0-blue)](https://pypi.org/project/bitmart-python-sdk-api)
[![Python version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


[BitMart Exchange official](https://bitmart.com) Python client for the [BitMart Cloud API](http://developer-pro.bitmart.com).



Feature
=========================
- Provides exchange quick trading API
- Easier withdrawal
- Efficiency, higher speeds, and lower latencies
- Priority in development and maintenance
- Dedicated and responsive technical support
- Provide webSocket apis calls
- Supported APIs:
    - `/spot/*`
    - `/contract/*`
    - `/account/*`
    - Spot WebSocket Market Stream
    - Spot User Data Stream
    - Contract User Data Stream
    - Contract WebSocket Market Stream
- Test cases and examples



Installation
=========================
```bash
pip install bitmart-python-sdk-api
```


Usage
=========================
* An example of a spot trade API
* Replace it with your own API KEY
* Run

#### Spot Public API Example
```python
from bitmart.api_spot import APISpot

if __name__ == '__main__':

    spotAPI = APISpot(timeout=(2, 10))
    
    # Get a list of all cryptocurrencies on the platform
    spotAPI.get_currencies()
    
    # Querying aggregated tickers of a particular trading pair
    spotAPI.get_symbol_ticker(symbol='BTC_USDT')
    
    # Get the latest trade records of the specified trading pair
    spotAPI.get_symbol_trades(symbol='BTC_USDT', N=50)
```


#### Spot API Example
```python
from bitmart.api_spot import APISpot
from bitmart.lib import cloud_exceptions
from bitmart.lib.cloud_log import CloudLog

if __name__ == '__main__':

    api_key = "Your API KEY"
    secret_key = "Your Secret KEY"
    memo = "Your Memo"

    try:
        spotAPI = APISpot(api_key, secret_key, memo, timeout=(3, 10))
        CloudLog.set_logger_level('info')

        response = spotAPI.post_submit_order(
            symbol='BTC_USDT',
            side='sell',
            type='limit',
            size='10000',
            price='1000000'
        )

    except cloud_exceptions.APIException as apiException:
        print("Error[HTTP<>200]:", apiException.response)
    except Exception as exception:
        print("Error[Exception]:", exception)
    else:
        if response[0]['code'] == 1000:
            print('Call Success:', response[0])
        else:
            print('Call Failed:', response[0]['message'])
    
```

More Example: [test_api_spot.py](https://github.com/bitmartexchange/bitmart-python-sdk-api/blob/master/tests/test_api_spot.py)
More Example: [test_api_account.py](https://github.com/bitmartexchange/bitmart-python-sdk-api/blob/master/tests/test_api_account.py)


#### Spot WebSocket Public Channel Example

```python

from bitmart.lib import cloud_consts
from bitmart.lib.cloud_ws_client import CloudWSClient
from bitmart.ws_spot import create_channel, create_spot_subscribe_params


class WSTest(CloudWSClient):

    def on_message(self, message):
        print(f'[ReceiveServerMessage]-------->{message}')


if __name__ == '__main__':
    ws = WSTest(url=cloud_consts.WS_URL)
    ws.set_debug(False)
    channels = [
        # public channel
        create_channel(cloud_consts.WS_PUBLIC_SPOT_TICKER, 'BTC_USDT'),
        create_channel(cloud_consts.WS_PUBLIC_SPOT_KLINE_1M, 'BTC_USDT'),
        create_channel(cloud_consts.WS_PUBLIC_SPOT_DEPTH5, 'BTC_USDT')
        
        # or  public channel
        #"spot/ticker:BTC_USDT",
        #"spot/kline1m:BTC_USDT",
        #"spot/depth5:BTC_USDT"
    ]

    ws.spot_subscribe_without_login(create_spot_subscribe_params(channels))

```

#### Spot WebSocket Private Channel Example

```python

from bitmart.lib import cloud_consts
from bitmart.lib.cloud_ws_client import CloudWSClient
from bitmart.ws_spot import create_channel, create_spot_subscribe_params


class WSTest(CloudWSClient):

    def on_message(self, message):
        print(f'[ReceiveServerMessage]-------->{message}')


if __name__ == '__main__':
    ws = WSTest(cloud_consts.WS_URL_USER, api_key="Your API KEY", secret_key="Your Secret KEY", memo="Your Memo")
    ws.set_debug(True)
    channels = [
        # private channel
        create_channel(cloud_consts.WS_USER_SPOT_ORDER, 'BTC_USDT')
    ]

    ws.spot_subscribe_with_login(create_spot_subscribe_params(channels))

```

#### Contract Public API Example
```python
from bitmart.api_contract import APIContract

if __name__ == '__main__':

    contractAPI = APIContract(timeout=(2, 10))

    # query contract details
    contractAPI.get_details(contract_symbol='ETHUSDT')
    
    # Get full depth of trading pairs.
    contractAPI.get_depth(contract_symbol='ETHUSDT')

    # Querying the open interest and open interest value data of the specified contract
    contractAPI.get_open_interest(contract_symbol='ETHUSDT')

    # Applicable for checking the current funding rate of a specified contract
    contractAPI.get_funding_rate(contract_symbol='ETHUSDT')
    
    # querying K-line data
    contractAPI.get_kline(contract_symbol='ETHUSDT', step=5, start_time=1662518172, end_time=1662518172)

```

#### Contract API Example
```python
from bitmart.api_contract import APIContract

if __name__ == '__main__':

    api_key = "Your API KEY"
    secret_key = "Your Secret KEY"
    memo = "Your Memo"

    contractAPI = APIContract(api_key, secret_key, memo, timeout=(3, 10))

    contractAPI.post_submit_order(contract_symbol='BTCUSDT', 
                                  side=4, 
                                  type='limit', 
                                  leverage='1',
                                  open_type='isolated',
                                  size=10, 
                                  price='20000')
```

More Example: [test_api_contract.py](https://github.com/bitmartexchange/bitmart-python-sdk-api/blob/master/tests/test_api_contract.py)


#### Contract WebSocket Public Channel Example
```python

from bitmart.lib import cloud_consts
from bitmart.lib.cloud_ws_contract_client import CloudWSContractClient
from bitmart.ws_contract import create_channel, create_contract_subscribe_params


class WSTest(CloudWSContractClient):

    def on_message(self, message):
        print(f'[ReceiveServerMessage]-------->{message}')


if __name__ == '__main__':
    ws = WSTest(cloud_consts.CONTRACT_WS_URL)
    ws.set_debug(False)
    channels = [
        # public channel
        cloud_consts.WS_PUBLIC_CONTRACT_TICKER,
        create_channel(cloud_consts.WS_PUBLIC_CONTRACT_DEPTH5, 'BTCUSDT'),
        create_channel(cloud_consts.WS_PUBLIC_CONTRACT_KLINE_1M, 'BTCUSDT'),
    ]

    ws.contract_subscribe_without_login(create_contract_subscribe_params(channels))

```

#### Contract WebSocket Private Channel Example
```python

from bitmart.lib import cloud_consts
from bitmart.lib.cloud_ws_contract_client import CloudWSContractClient
from bitmart.ws_contract import create_channel, create_contract_subscribe_params


class WSTest(CloudWSContractClient):

    def on_message(self, message):
        print(f'[ReceiveServerMessage]-------->{message}')


if __name__ == '__main__':
    ws = WSTest(cloud_consts.CONTRACT_WS_URL_USER, api_key="Your API KEY", secret_key="Your Secret KEY", memo="Your Memo")
    ws.set_debug(False)
    channels = [
        # private channel
        create_channel(cloud_consts.WS_USER_CONTRACT_ASSET, 'USDT'),
        cloud_consts.WS_USER_CONTRACT_POSITION,
        cloud_consts.WS_USER_CONTRACT_UNICAST,
    ]

    ws.contract_subscribe_with_login(create_contract_subscribe_params(channels))

```

