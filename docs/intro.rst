.. role:: raw-html-m2r(raw)
   :format: html


bitmart-python-sdk-api
===================================


.. image:: https://img.shields.io/pypi/v/bitmart-python-sdk-api.svg
   :target: https://pypi.org/project/bitmart-python-sdk-api/
   :alt: PyPI version


.. image:: https://img.shields.io/pypi/pyversions/bitmart-python-sdk-api
   :target: https://www.python.org/downloads/
   :alt: Python version


.. image:: https://img.shields.io/badge/docs-latest-blue
   :target: https://bitmart-python-sdk-api.readthedocs.io/en/stable/)
   :alt: Documentation


.. image:: https://img.shields.io/badge/code_style-black-black
   :target: https://black.readthedocs.io/en/stable/
   :alt: Code Style


.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT


[BitMart Exchange official](https://bitmart.com) Python client for the [BitMart Cloud API](http://developer-pro.bitmart.com).
It's designed to be simple, clean, and easy to use with minimal dependencies.

* Source Code: https://github.com/bitmartexchange/bitmart-python-sdk-api
* Official API document:

  * https://developer-pro.bitmart.com/

* Support channels:

  * Telegram Channel: https://t.me/bitmart_api

* API key setup: https://developer-pro.bitmart.com/en/spot/#api-key-create

Features
--------
* Provides exchange quick trading API
* Easier withdrawal
* Efficiency, higher speeds, and lower latencies
* Priority in development and maintenance
* Dedicated and responsive technical support
* Provide webSocket apis calls
* Supported APIs:
    * `/spot/*`
    * `/contract/*`
    * `/account/*`
    * Spot WebSocket Market Stream
    * Spot User Data Stream
    * Contract User Data Stream
    * Contract WebSocket Market Stream
* Test cases and examples


Quick Start
-----------

Installation
^^^^^^^^^^^^

* Install via package name

  .. code-block:: bash

     pip install bitmart-python-sdk-api

* Alternatively, install with git repository path

  .. code-block:: bash

    python -m pip install git+https://github.com/bitmartexchange/bitmart-python-sdk-api.git


Usage
-----

RESTful APIs
^^^^^^^^^^^^

.. code-block:: python

    from bitmart.api_spot import APISpot

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


Please find `examples <https://github.com/bitmartexchange/bitmart-python-sdk-api/blob/master/tests/test_api_spot.py>`_  to check for more endpoints.


Websocket
^^^^^^^^^

.. code-block:: python


    from bitmart.lib import cloud_consts
    from bitmart.lib.cloud_ws_client import CloudWSClient
    from bitmart.ws_spot import create_channel, create_spot_subscribe_params


    class WSTest(CloudWSClient):

        def on_message(self, message):
            print(f'[ReceiveServerMessage]-------->{message}')


    if __name__ == '__main__':
        ws = WSTest(cloud_consts.WS_URL, "", "", "")
        ws.set_debug(True)
        channels = [
            # public channel
            "spot/ticker:BTC_USDT",
            "spot/kline1m:BTC_USDT",
            "spot/depth5:BTC_USDT"
        ]

        ws.spot_subscribe_without_login(create_spot_subscribe_params(channels))

More websocket examples are available in the `examples <https://github.com/bitmartexchange/bitmart-python-sdk-api/blob/master/tests/test_ws_spot.py>`_
