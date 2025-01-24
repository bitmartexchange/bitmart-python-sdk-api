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
    response = futuresAPI.post_submit_trail_order(contract_symbol='BTCUSDT', side=4, leverage='80',
                                                  open_type='isolated', size=1, activation_price='190000',
                                                  callback_rate='1', activation_price_type=1)[0]
    #  'order_id': 56739000045
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
