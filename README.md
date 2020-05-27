[![Logo](./logo.png)](https://bitmart.com)

BitMart-Python-API
=========================
<p align="left">
    <a href='#'><img src='https://travis-ci.org/meolu/walle-web.svg?branch=master' alt="Build Status"></a>  
</p>

Python client for the [BitMart Cloud API](http://developer-pro.bitmart.com).



Feature
=========================
- Provides exchange quick trading API


Installation
=========================

* 1.Python 3.6+ support

* 2.Clone
```git
git clone git@github.com:bitmartexchange/bitmart-python-api.git
pip install -r requirements.txt
```



Usage
=========================
* An example of a spot trade API
* Replace it with your own API KEY
* Run
```python
from bitmart.api_spot import APISpot

if __name__ == '__main__':

    api_key = "80618e45710812162b04892c7ee5ead4a3cc3e56"
    secret_key = "6c6c98544461bbe71db2bca4c6d7fd0021e0ba9efc215f9c6ad41852df9d9df9"
    memo = "test001"

    spotAPI = APISpot(api_key, secret_key, memo)

    spotAPI.post_submit_limit_buy_order('BTC_USDT', size=0.01, price=8800)
```


License
=========================
