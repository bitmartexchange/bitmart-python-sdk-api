
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

order_ids = ['12312', '2333333']

try:
    response = spotAPI.post_cancel_orders(
        symbol='BTC_USDT',
        order_ids=order_ids)[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )


client_order_ids = ['12321312312321', '4r4546464564']

try:
    response = spotAPI.post_cancel_orders(
        symbol='BTC_USDT',
        client_order_ids=client_order_ids)[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )