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
    # Query the default deposit crediting account
    logger.info(accountAPI.get_deposit_account()[0])

    # Set the deposit crediting account type
    logger.info(accountAPI.post_set_deposit_account(account_type='SPOT')[0])
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
