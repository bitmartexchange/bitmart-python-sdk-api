
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
    response = spotAPI.v4_query_order_by_id(
        order_id='12312312313123',
        query_state='open',
        recv_window=5000)[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
