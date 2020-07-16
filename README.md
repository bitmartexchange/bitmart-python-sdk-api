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
```python
from bitmart.api_spot import APISpot

if __name__ == '__main__':

    api_key = "Your API KEY"
    secret_key = "Your Secret KEY"
    memo = "Your Memo"

    spotAPI = APISpot(api_key, secret_key, memo)

    spotAPI.post_submit_limit_buy_order('BTC_USDT', size='0.01', price='8800')
```

Release Notes
=========================

** 2020-07-16 
- Interface Spot API `Cancel Order` update to v2 version that is `POST https://api-cloud.bitmart.com/spot/v2/cancel_order`
- UserAgent set "BitMart-Java-SDK/1.0.1"
          
          
License
=========================
