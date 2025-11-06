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
    response = marginLoanAPI.margin_borrow_isolated(symbol='BTC_USDT', currency='BTC', amount='1')[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
