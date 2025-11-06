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
    response = futuresAPI.post_submit_plan_order(
        contract_symbol="ETHUSDT",
        side=4,
        mode=1,
        type="limit",
        leverage="1",
        open_type="isolated",
        size=10,
        trigger_price="2000",
        executive_price="1450",
        price_type=1,
        price_way=1
    )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )

