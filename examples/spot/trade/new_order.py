
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

try:

    # Place limit order
    response = spotAPI.post_submit_order(
        symbol='BTC_USDT',
        side='buy',
        type='limit',
        size='0.01',
        price='8800')[0]
    logger.info(response)

    # Place market order
    # Special Parameters for Market Buy Orders (type=market, side=buy)
    response1 = spotAPI.post_submit_order(
        symbol='BTC_USDT',
        side='buy',
        type='market',
        notional='10000',
    )
    logger.info(response1)

    # Special Parameters for Market Sell Orders (type=market, side=sell)
    response2 = spotAPI.post_submit_order(
        symbol='BTC_USDT',
        side='sell',
        type='market',
        size='10000',
    )
    logger.info(response2)

except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )


