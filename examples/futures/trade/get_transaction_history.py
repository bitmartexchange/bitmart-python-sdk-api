import logging
from examples.config import API_KEY, SECRET_KEY, MEMO
import time

from bitmart.api_contract import APIContract
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging


config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

futuresAPI = APIContract(api_key=API_KEY,
                         secret_key=SECRET_KEY,
                         memo=MEMO,
                         logger=logger)

try:
    response = futuresAPI.get_transaction_history(contract_symbol='BTCUSDT', flow_type=1)[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )

try:
    before = int(time.time()) * 1000
    after = before + 3600 * 1000
    response = futuresAPI.get_transaction_history(
        contract_symbol='BTCUSDT',
        start_time=before,
        end_time=after
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )

try:
    before = int(time.time()) * 1000
    after = before + 3600 * 1000
    response = futuresAPI.get_transaction_history(
        contract_symbol='BTCUSDT',
        flow_type=1,
        start_time=before,
        end_time=after,
        account='futures'
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
