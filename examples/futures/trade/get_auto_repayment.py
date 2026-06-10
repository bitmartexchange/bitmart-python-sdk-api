import logging
from examples.config import API_KEY, SECRET_KEY, MEMO

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
    response = futuresAPI.get_auto_repayment(
        start_time=1770739200,
        end_time=1771257600,
        page=1,
        size=1000,
        from_coin_code='USDT',
        type='AUTO_REPAY')[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
