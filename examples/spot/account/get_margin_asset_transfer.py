import logging

from bitmart.api_account import APIAccount
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

accountAPI = APIAccount(api_key="Your_Api_Key",
                        secret_key="Your_Secret_Key",
                        memo="Your_Memo",
                        logger=logger)

try:
    response = accountAPI.margin_asset_transfer(
        symbol='BMX_USDT',
        currency='BTC',
        amount='100',
        side='in'
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
