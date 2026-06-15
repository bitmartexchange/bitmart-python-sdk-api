import logging
from examples.config import API_KEY, SECRET_KEY, MEMO

from bitmart.api_contract_sub_account import APIContractSubAccount
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging


config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

futuresAPI = APIContractSubAccount(api_key=API_KEY,
                                   secret_key=SECRET_KEY,
                                   memo=MEMO,
                                   logger=logger)

try:
    # Sub-account to main-account (for main account)
    logger.info(futuresAPI.post_sub_to_main(
        request_no='uuid-0001', amount='1', currency='USDT', sub_account='subAccountName')[0])

    # Sub-account to main-account (for sub account)
    logger.info(futuresAPI.post_sub_to_main_from_sub_account(
        request_no='uuid-0002', amount='1', currency='USDT')[0])

    # Main-account to sub-account (for main account)
    logger.info(futuresAPI.post_main_to_sub(
        request_no='uuid-0003', amount='1', currency='USDT', sub_account='subAccountName')[0])

    # Sub-account futures transfer history (for main account)
    logger.info(futuresAPI.get_sub_transfer_list(sub_account='subAccountName', limit=10)[0])

    # Account futures transfer history (for main and sub account)
    logger.info(futuresAPI.get_sub_transfer_history(limit=10)[0])

    # Sub-account futures wallet balance (for main account)
    logger.info(futuresAPI.get_sub_wallet(sub_account='subAccountName', currency='USDT')[0])
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
