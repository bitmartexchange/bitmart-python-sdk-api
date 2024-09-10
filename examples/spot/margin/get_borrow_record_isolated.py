import logging

from bitmart.api_margin_loan import APIMarginLoan
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

marginLoanAPI = APIMarginLoan(api_key="Your_Api_Key",
                              secret_key="Your_Secret_Key",
                              memo="Your_Memo",
                              logger=logger)

try:
    response = marginLoanAPI.borrow_record_isolated(symbol='BTC_USDT')[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )

try:
    response = marginLoanAPI.borrow_record_isolated(symbol='BTC_USDT', borrow_id='ES16612345642160qnqR1ce')[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )