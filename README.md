[![Logo](https://img.bitmart.com/static-file/public/sdk/sdk_logo.png)](https://bitmart.com)

BitMart-Python-SDK-API
=========================
[![PyPI version](https://img.shields.io/badge/pypi-v1.0.0-blue)](https://pypi.org/project/bitmart-python-sdk-api)
[![Python version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


[BitMart Exchange official](https://bitmart.com) Python client for the BitMart Cloud API.



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

Documentation
=========================
[API Documentation](https://developer-pro.bitmart.com/en/spot/#change-log)


Example
=========================

#### Spot Public API Example
```python
from bitmart.api_spot import APISpot

if __name__ == '__main__':

    spotAPI = APISpot(timeout=(2, 10))
    
    # Get a list of all cryptocurrencies on the platform
    spotAPI.get_currencies()
    
    # Querying aggregated tickers of a particular trading pair
    spotAPI.get_v3_ticker(symbol='BTC_USDT')
    
    # Get the latest trade records of the specified trading pair
    spotAPI.get_v3_trades(symbol='BTC_USDT', limit=10)
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

import logging
import time

from bitmart.lib.cloud_consts import SPOT_PUBLIC_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.spot_socket_client import SpotSocketClient

def message_handler(_, message):
    logging.info(message)
      
if __name__ == '__main__':
  config_logging(logging, logging.DEBUG)
  
  
  my_client = SpotSocketClient(stream_url=SPOT_PUBLIC_WS_URL,
                               on_message=message_handler)
  
  # Subscribe to a single symbol stream
  my_client.subscribe(args="spot/ticker:BMX_USDT")
  
  # Subscribe to multiple symbol streams
  my_client.subscribe(args=["spot/ticker:BMX_USDT", "spot/ticker:BTC_USDT"])
  
  # Send the original subscription message
  my_client.send({"op": "subscribe", "args": ["spot/ticker:ETH_USDT"]})
  
  time.sleep(5)
  
  # Unsubscribe
  my_client.unsubscribe(args="spot/ticker:BMX_USDT")
  
  my_client.send({"op": "unsubscribe", "args": ["spot/ticker:BMX_USDT"]})


```

#### Spot WebSocket Private Channel Example

```python

import logging

from bitmart.lib.cloud_consts import SPOT_PRIVATE_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.spot_socket_client import SpotSocketClient

def message_handler(_, message):
    logging.info(message)
    
if __name__ == '__main__':
    config_logging(logging, logging.DEBUG)

    my_client = SpotSocketClient(stream_url=SPOT_PRIVATE_WS_URL,
                             on_message=message_handler,
                             api_key="your_api_key",
                             api_secret_key="your_secret_key",
                             api_memo="your_api_memo")

    # Login
    my_client.login()

    # Subscribe to a single symbol stream
    my_client.subscribe(args="spot/user/balance:BALANCE_UPDATE")

    # Stop
    # my_client.stop()

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

import logging
import time

from bitmart.lib.cloud_consts import FUTURES_PUBLIC_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.futures_socket_client import FuturesSocketClient

def message_handler(_, message):
    logging.info(message)
    
    

if __name__ == '__main__':
    config_logging(logging, logging.DEBUG)
    
    my_client = FuturesSocketClient(stream_url=FUTURES_PUBLIC_WS_URL,
                                on_message=message_handler)

    # Example 1:
    # Subscribe to a single symbol stream
    my_client.subscribe(args="futures/ticker")

    time.sleep(2)

    # Unsubscribe
    my_client.unsubscribe(args="futures/ticker")

    time.sleep(5)
    # Example 2:
    # Send the original subscription message
    my_client.send({"action": "subscribe", "args": ["futures/ticker"]})

    time.sleep(2)

    # Unsubscribe
    my_client.send({"action": "unsubscribe", "args": ["futures/ticker"]})

    # Stop
    # my_client.stop()


```

#### Contract WebSocket Private Channel Example

```python

import logging

from bitmart.lib.cloud_consts import FUTURES_PRIVATE_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.futures_socket_client import FuturesSocketClient

def message_handler(_, message):
    logging.info(message)


if __name__ == '__main__':
    config_logging(logging, logging.INFO)
  
    my_client = FuturesSocketClient(stream_url=FUTURES_PRIVATE_WS_URL,
                                on_message=message_handler,
                                api_key="your_api_key",
                                api_secret_key="your_secret_key",
                                api_memo="your_api_memo")

    # Login
    my_client.login()

    # Subscribe to a single symbol stream
    my_client.subscribe(args="futures/asset:USDT")

    # Subscribe to multiple symbol streams
    my_client.subscribe(args=["futures/asset:BTC", "futures/asset:ETH"])

    # Stop
    # my_client.stop()
```

Extra Options
=========================

### Authentication
How to set API KEY?

```python
from bitmart.api_spot import APISpot
from bitmart.api_contract import APIContract

spotAPI = APISpot(api_key="your api access key", secret_key="your api secret key", memo="your api memo")
contractAPI = APIContract(api_key="your api access key", secret_key="your api secret key", memo="your api memo")
```

### Timeout
Set HTTP `connection timeout` and `read timeout`.

```python
from bitmart.api_spot import APISpot
from bitmart.api_contract import APIContract
spotAPI = APISpot(timeout=(2, 10))
contractAPI = APIContract(timeout=(2, 10))
```

### Logging
If you want to `debug` the data requested by the API and the corresponding data returned by the API,
you can set it like this:

```python
import logging
from bitmart.api_spot import APISpot
from bitmart.lib.cloud_utils import config_logging

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

spotAPI = APISpot(logger=logger)
```



### Domain
How to set API domain name? The domain name parameter is optional,
the default domain name is `https://api-cloud.bitmart.com`.

```python
from bitmart.api_spot import APISpot
from bitmart.api_contract import APIContract
spotAPI = APISpot(url='https://api-cloud.bitmart.com')
contractAPI = APIContract(url='https://api-cloud.bitmart.com')
```


### Custom request headers
You can add your own request header information here, but please do not fill in `X-BM-KEY, X-BM-SIGN, X-BM-TIMESTAMP`

```python
from bitmart.api_spot import APISpot
spotAPI = APISpot(headers={'Your-Custom-Header': 'xxxxxxx'})
```