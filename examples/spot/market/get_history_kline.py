
import logging
import time

from bitmart.api_spot import APISpot
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

spotAPI = APISpot(logger=logger)

try:
    before = int(time.time())
    after = before - 3600
    response = spotAPI.get_v3_history_kline(symbol='BTC_USDT', before=before, after=after, step=60, limit=5)[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
