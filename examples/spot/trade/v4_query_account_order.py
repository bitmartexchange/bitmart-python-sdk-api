
import logging
import time

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
    before = int(time.time()) * 1000
    after = before + 3600
    response = spotAPI.v4_query_account_orders(
        symbol='BTC_USDT',
        order_mode='spot',
        start_time=before,
        end_time=after,
        limit=10,
        recv_window=5000)[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
