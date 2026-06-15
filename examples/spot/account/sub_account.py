import logging
from examples.config import API_KEY, SECRET_KEY, MEMO

from bitmart.api_spot_sub_account import APISpotSubAccount
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging


config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

accountAPI = APISpotSubAccount(api_key=API_KEY,
                               secret_key=SECRET_KEY,
                               memo=MEMO,
                               logger=logger)

try:
    # Sub-account to main-account (for main account)
    logger.info(accountAPI.post_sub_to_main(
        request_no='uuid-0001', amount='1', currency='USDT', sub_account='subAccountName')[0])

    # Sub-account to main-account (for sub account)
    logger.info(accountAPI.post_sub_to_main_from_sub_account(
        request_no='uuid-0002', amount='1', currency='USDT')[0])

    # Main-account to sub-account (for main account)
    logger.info(accountAPI.post_main_to_sub(
        request_no='uuid-0003', amount='1', currency='USDT', sub_account='subAccountName')[0])

    # Sub-account to sub-account (for main account)
    logger.info(accountAPI.post_sub_to_sub(
        request_no='uuid-0004', amount='1', currency='USDT',
        from_account='subA', to_account='subB')[0])

    # Sub-account transfer history (for main account)
    logger.info(accountAPI.get_sub_transfer_list(move_type='spot to spot', n=10)[0])

    # Account transfer history (for main and sub account)
    logger.info(accountAPI.get_account_transfer_history(move_type='spot to spot', n=10)[0])

    # Sub-account spot wallet balance (for main account)
    logger.info(accountAPI.get_sub_spot_wallet(sub_account='subAccountName', currency='USDT')[0])

    # Sub-account list (for main account)
    logger.info(accountAPI.get_sub_account_list()[0])
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
