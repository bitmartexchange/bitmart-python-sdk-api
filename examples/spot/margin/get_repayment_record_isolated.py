import logging
from examples.config import API_KEY, SECRET_KEY, MEMO

from bitmart.api_margin_loan import APIMarginLoan
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging


config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

marginLoanAPI = APIMarginLoan(api_key=API_KEY,
                              secret_key=SECRET_KEY,
                              memo=MEMO,
                              logger=logger)

try:
    response = marginLoanAPI.repayment_record_isolated(symbol='BTC_USDT')[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )

try:
    response = marginLoanAPI.repayment_record_isolated(symbol='BTC_USDT', repay_id='ES16612345642160qnqR1ce')[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )