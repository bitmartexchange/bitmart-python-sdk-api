import logging
from examples.config import API_KEY, SECRET_KEY, MEMO

from bitmart.api_spot import APISpot
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging


config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

spotAPI = APISpot(api_key=API_KEY,
                  secret_key=SECRET_KEY,
                  memo=MEMO,
                  logger=logger)

orderParams = [{'side': 'buy', 'type': 'limit', 'size': '0.01', 'price': '8800', 'clientOrderId': '123128930180'}]

try:
    response = spotAPI.post_batch_orders(
        symbol='BTC_USDT',
        order_params=orderParams,
        recv_window=6000)[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
