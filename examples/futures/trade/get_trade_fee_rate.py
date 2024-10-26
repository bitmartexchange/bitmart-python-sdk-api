import logging

from bitmart.api_contract import APIContract
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

futuresAPI = APIContract(api_key="c783b945b6394f394cee77ee88b6b3fe68b6f7da",
                         secret_key="Your_Secret_Key",
                         memo="Your_Memo",
                         logger=logger)

try:
    response = futuresAPI.get_trade_fee_rate("BTCUSDT")[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
