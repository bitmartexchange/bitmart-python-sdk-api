import logging
from examples.config import API_KEY, SECRET_KEY, MEMO

from bitmart.api_finance import APIFinance
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging


config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

financeAPI = APIFinance(api_key=API_KEY,
                        secret_key=SECRET_KEY,
                        memo=MEMO,
                        logger=logger)

try:
    # Earn account holdings
    logger.info(financeAPI.get_earn_assets()[0])

    # Flexible savings
    logger.info(financeAPI.get_savings_product(current_page=1, size_page=10, coin_name='USDT')[0])
    logger.info(financeAPI.post_savings_subscribe(
        product_id='1001', amount='100', request_no='20000009000000300000')[0])
    logger.info(financeAPI.post_savings_redeem(
        earn_id='200001', amount='50', request_no='20000009000000300001')[0])
    logger.info(financeAPI.get_savings_holdings(current_page=1, size_page=10)[0])
    logger.info(financeAPI.get_savings_records(type='subscribe', current_page=1, size_page=10)[0])

    # Fixed savings
    logger.info(financeAPI.get_fixed_product(current_page=1, size_page=10)[0])
    logger.info(financeAPI.post_fixed_subscribe(
        product_id='2001', amount='10', request_no='20000009000000300002', auto_subscribe='OFF')[0])
    logger.info(financeAPI.get_fixed_holdings(current_page=1, size_page=10)[0])
    logger.info(financeAPI.get_fixed_records(type='subscribe', current_page=1, size_page=10)[0])
    logger.info(financeAPI.post_fixed_redeem(earn_id='300001', request_no='20000009000000300003')[0])
    logger.info(financeAPI.post_fixed_modify_auto_renewal(earn_id='300001', auto_subscribe='REINVEST_FIXED')[0])

    # Auto earn
    logger.info(financeAPI.post_auto_subscribe_toggle(auto_subscribe='open')[0])
    logger.info(financeAPI.get_auto_subscribe_status()[0])
    logger.info(financeAPI.post_flexible_auto_subscribe_toggle(product_id='1001', auto_subscribe='open')[0])
    logger.info(financeAPI.get_flexible_auto_subscribe_status(product_id='1001')[0])
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
