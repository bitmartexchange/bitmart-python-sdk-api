import logging
from examples.config import API_KEY, SECRET_KEY, MEMO
import time

from bitmart.api_contract import APIContract
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging


config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

futuresAPI = APIContract(api_key=API_KEY,
                         logger=logger)

try:
    before = int(time.time())
    after = before + 3600
    response = futuresAPI.get_order_history(contract_symbol='BTCUSDT', start_time=before, end_time=after)[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )

try:
    before = int(time.time())
    after = before + 3600
    response = futuresAPI.get_order_history(
        contract_symbol='BTCUSDT', 
        start_time=before, 
        end_time=after,
        account='futures',
        order_id='12312312312',
        client_order_id='client_order_123'
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
