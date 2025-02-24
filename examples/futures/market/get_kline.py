
import logging
import time

from bitmart.api_contract import APIContract
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

contractAPI = APIContract(logger=logger)

try:
    end_time = int(time.time())
    start_time = end_time - 3600
    response = contractAPI.get_kline(
        contract_symbol='BTCUSDT',
        step=5,
        start_time=start_time,
        end_time=end_time
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
