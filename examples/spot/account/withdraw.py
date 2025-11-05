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
    response = accountAPI.post_withdraw_apply(
        currency='USDT-TRC20',
        amount='100.000',
        destination='To Digital Address',
        address='0x1EE6FA5A3803608fc22a1f3F76********',
        address_memo=''
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )


try:
    response = accountAPI.post_withdraw_apply(
        currency='USDT-TRC20',
        amount='100.000',
        type=1,
        value='876940329',
        area_code=''
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )

