import logging
import time

from bitmart.api_contract import APIContract
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

futuresAPI = APIContract(api_key="Your_Api_Key",
                         secret_key="Your_Secret_Key",
                         memo="Your_Memo",
                         logger=logger)

try:
    response = futuresAPI.post_modify_limit_order(
        contract_symbol="BTCUSDT",
        client_order_id="ASDSD23e12e121212crewc",
        price="1000.10"
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )

