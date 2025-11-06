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
    response = futuresAPI.post_submit_tp_sl_order(
            contract_symbol='BTCUSDT',
            side=2,
            type="take_profit",
            size=10,
            trigger_price="2000",
            executive_price="1450",
            price_type=1,
            plan_category=1,
            client_order_id="12314323424",
            category="limit"
        )[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )

