import logging
from examples.config import API_KEY, SECRET_KEY, MEMO

from bitmart.api_account import APIAccount
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging


config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

accountAPI = APIAccount(api_key=API_KEY,
                        secret_key=SECRET_KEY,
                        memo=MEMO,
                        logger=logger)

try:
    response = accountAPI.get_withdraw_charge(currency='BTC')[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )



