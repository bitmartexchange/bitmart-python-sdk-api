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
    response = futuresAPI.post_cancel_plan_order(
        contract_symbol="ETHUSDT",
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )

try:
    response = futuresAPI.post_cancel_plan_order(
        contract_symbol="ETHUSDT",
        order_id='12312312',
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )



try:
    response = futuresAPI.post_cancel_plan_order(
        contract_symbol="ETHUSDT",
        client_order_id='12312312',
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )

