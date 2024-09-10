
import logging

from bitmart.api_spot import APISpot
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

spotAPI = APISpot(api_key="Your_Api_Key",
                  secret_key="Your_Secret_Key",
                  memo="Your_Memo",
                  logger=logger)

try:
    response = spotAPI.post_cancel_order_by_orderid(
        symbol='BTC_USDT',
        order_id='12321312')[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )


try:
    response = spotAPI.post_cancel_order_by_clientid(
        symbol='BTC_USDT',
        client_order_id='1232131212312')[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
