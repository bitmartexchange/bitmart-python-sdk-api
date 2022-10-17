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



#### WebSocket Public Channel Example
```python

from bitmart import cloud_consts
from bitmart.cloud_ws_client import CloudWSClient
from bitmart.ws_spot import create_channel, create_spot_subscribe_params


class WSTest(CloudWSClient):

    def on_message(self, message):
        print(f'[ReceiveServerMessage]-------->{message}')


if __name__ == '__main__':
    ws = WSTest(cloud_consts.WS_URL, "", "", "")
    ws.set_debug(True)
    channels = [
        # public channel
        create_channel(cloud_consts.WS_PUBLIC_SPOT_TICKER, 'BTC_USDT'),
        create_channel(cloud_consts.WS_PUBLIC_SPOT_KLINE_1M, 'BTC_USDT'),
        create_channel(cloud_consts.WS_PUBLIC_SPOT_DEPTH5, 'BTC_USDT')
    ]

    ws.spot_subscribe_without_login(create_spot_subscribe_params(channels))

```

#### WebSocket Private Channel Example
```python

from bitmart import cloud_consts
from bitmart.cloud_ws_client import CloudWSClient
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


Release Notes
=========================

###### 2020-07-16 
- Interface Spot API `Cancel Order` update to v2 version that is `POST https://api-cloud.bitmart.com/spot/v2/cancel_order`
- UserAgent set "BitMart-Java-SDK/1.0.1"

###### 2020-09-21
- Interface Spot API `/spot/v1/symbols/book` add `size` parameter, which represents the number of depths

###### 2021-01-19
- New endpoints for Spot WebSocket
  - Public - ticket channels
  - Public - K channel
  - Public - trading channels
  - Public - depth channels
  - Login
  - User - Trading Channel

###### 2021-11-06
- Update endpoints for Spot WebSocket
  - Public-Depth Channel:
    - spot/depth20     20 Level Depth Channel
    - spot/depth50     50 Level Depth Channel
  - User-Trade Channel:
    - Eligible pushes add new orders successfully

###### 2021-11-24
- New endpoints for Spot
  - <code>/spot/v2/orders</code>Get User Order History V2
  - <code>/spot/v1/batch_orders</code>Batch Order
- Update endpoints for Spot
  - <code>/spot/v1/symbols/kline</code>Add new field 'quote_volume'
  - <code>/spot/v1/symbols/trades</code>Add optional parameter N to return the number of items, the default is up to 50 items
  - <code>/spot/v1/order_detail</code>Add new field 'unfilled_volume'
  - <code>/spot/v1/submit_order</code>The request parameter type added limit_maker and ioc order types
- New endpoints for Account
  - <code>/account/v2/deposit-withdraw/history</code>Get Deposit And Withdraw  History V2
- Update endpoints for Account
  - <code>/account/v1/wallet</code>Remove the account_type,Only respond to currency accounts; you can bring currency parameters (optional)

###### 2022-01-18
- websocket public channel address<code>wss://ws-manager-compress.bitmart.com?protocol=1.1</code>will be taken down on 2022-02-28 UTC time,The new address is<code>wss://ws-manager-compress.bitmart.com/api?protocol=1.1</code>

###### 2022-01-20
- Update endpoints for Spot
  - <code>/spot/v1/symbols/details</code>Add a new respond parameter trade_status, to show the trading status of a trading pair symbol.

###### 2022-10-20
- New endpoints for Spot & Margin
    - <code>/spot/v1/margin/isolated/account</code>Applicable for isolated margin account inquiries
    - <code>/spot/v1/margin/isolated/transfer</code>For fund transfers between a margin account and spot account
    - <code>/spot/v1/user_fee</code>For querying the base rate of the current user
    - <code>/spot/v1/trade_fee</code>For the actual fee rate of the trading pairs
    - <code>/spot/v2/ticker</code>Applicable to query the latest ticker of all trading pairs, please note that the endpoint returns more data, please reduce the frequency of calls
    - <code>/spot/v1/ticker_detail</code>Applicable for querying aggregated tickers of a particular trading pair
    - <code>/spot/v2/submit_order</code>Applicable for spot order placement
    - <code>/spot/v1/margin/submit_order</code>Applicable for margin order placement
    - <code>/spot/v2/batch_orders</code>Batch order
    - <code>/spot/v3/cancel_order</code>Applicable to the cancellation of a specified unfinished order
    - <code>/spot/v2/order_detail</code>Applicable query a specified order detail
    - <code>/spot/v3/orders</code>Applicable for searching the recent order history, up to 200 queries
    - <code>/spot/v2/trades</code>Applicable for searching the recent trade history, up to 200 recent entries
    - <code>/spot/v1/margin/isolated/borrow</code>Applicable to isolated margin account borrowing operations
    - <code>/spot/v1/margin/isolated/repay</code>Applicable to isolated margin account repayment operations
    - <code>/spot/v1/margin/isolated/borrow_record</code>Applicable to the inquiry of borrowing records of an isolated margin account
    - <code>/spot/v1/margin/isolated/repay_record</code>Applicable to the inquiry of repayment records of isolated margin account
    - <code>/spot/v1/margin/isolated/pairs</code>Applicable for checking the borrowing rate and borrowing amount of trading pairs

License
=========================
