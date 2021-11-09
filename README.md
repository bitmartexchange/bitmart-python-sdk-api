[![Logo](./logo.png)](https://bitmart.com)

BitMart-Python-SDK-API
=========================
<p align="left">
    <a href='#'><img src='https://travis-ci.org/meolu/walle-web.svg?branch=master' alt="Build Status"></a>  
</p>

Python client for the [BitMart Cloud API](http://developer-pro.bitmart.com).



Feature
=========================
- Provides exchange quick trading API
- Easier withdrawal
- Efficiency, higher speeds, and lower latencies
- Priority in development and maintenance
- Dedicated and responsive technical support
- Provide webSocket apis calls

Installation
=========================

* 1.Python 3.6+ support

* 2.Clone
```git
git clone https://github.com/bitmartexchange/bitmart-python-sdk-api.git
pip3 install -r requirements.txt
```

* 3.Copy 
```bash
mv bitmart-python-sdk-api/bitmart /Your Working Directory
```


Usage
=========================
* An example of a spot trade API
* Replace it with your own API KEY
* Run

#### API Example
```python
from bitmart.api_spot import APISpot

if __name__ == '__main__':

    api_key = "Your API KEY"
    secret_key = "Your Secret KEY"
    memo = "Your Memo"

    spotAPI = APISpot(api_key, secret_key, memo, timeout=(3, 10))

    spotAPI.post_submit_limit_buy_order('BTC_USDT', size='0.01', price='8800')
```



#### WebSocket Example
```python

from bitmart import cloud_consts
from bitmart.cloud_ws_client import CloudWSClient
from bitmart.ws_spot import create_channel, create_spot_subscribe_params


class WSTest(CloudWSClient):

    def on_message(self, message):
        print(f'[ReceiveServerMessage]-------->{message}')


if __name__ == '__main__':
    ws = WSTest(api_key="Your API KEY", secret_key="Your Secret KEY", memo="Your Memo")
    ws.set_debug(True)
    channels = [
        # public channel
        create_channel(cloud_consts.WS_PUBLIC_SPOT_TICKER, 'BTC_USDT'),
        create_channel(cloud_consts.WS_PUBLIC_SPOT_KLINE_1M, 'BTC_USDT'),
        create_channel(cloud_consts.WS_PUBLIC_SPOT_DEPTH5, 'BTC_USDT'),

        # private channel
        create_channel(cloud_consts.WS_USER_SPOT_ORDER, 'BTC_USDT')
    ]

    ws.spot_subscribe_with_login(create_spot_subscribe_params(channels))

```

Release Notes
=========================

** 2020-07-16 
- Interface Spot API `Cancel Order` update to v2 version that is `POST https://api-cloud.bitmart.com/spot/v2/cancel_order`
- UserAgent set "BitMart-Java-SDK/1.0.1"

** 2020-09-21
- Interface Spot API `/spot/v1/symbols/book` add `size` parameter, which represents the number of depths

** 2021-11-09
- Add the following API interfaces:

| Interface | Interface Name |
| - | - |
|/account/v2/deposit-withdraw/history               | Get Deposit And Withdraw  History V2 |
|/spot/v2/orders                                    | Get User Order History V2 |
|/spot/v1/batch_orders                              | Batch Order ｜

- Modify the following API interfaces:

| Interface | Interface Name | Remark |
| - | - | - |
| /spot/v1/symbols/trades | Get Recent Trades | Add optional parameter N to return the number of items, the default is up to 50 items |
| /account/v1/wallet | Get Account Balance | Remove the account_type,Only respond to currency accounts; you can bring currency parameters (optional) |

License
=========================
