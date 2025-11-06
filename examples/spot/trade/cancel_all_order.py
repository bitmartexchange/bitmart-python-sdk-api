
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
    response = spotAPI.post_cancel_all_order()[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )


try:
    response = spotAPI.post_cancel_all_order(
        symbol='BTC_USDT', side='buy')[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
