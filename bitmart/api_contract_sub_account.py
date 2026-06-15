from bitmart.lib.cloud_client import CloudClient
from bitmart.lib.cloud_consts import *


class APIContractSubAccount(CloudClient):

    def __init__(self, api_key: str = "", secret_key: str = "", memo: str = "", url: str = API_V2_URL,
                 timeout: tuple = TIMEOUT, headers=None, logger=None):
        """
        Create api key from https://www.bitmart.com/api-config/en-US
        :param api_key: your access key
        :param secret_key: your secret key
        :param memo: your memo
        :param url: https://api-cloud-v2.bitmart.com
        :param timeout: (2, 10)
        """
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout, headers, logger)

    def post_sub_to_main(self, request_no: str, amount: str, currency: str, sub_account: str):
        """Sub-Account to Main-Account Futures Asset Transfer (For Main Account) (SIGNED)
        Transfer from a sub-account futures wallet to the main-account futures wallet (for main account)

        POST https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/sub-to-main

        :param request_no: uuid or other universally unique identifier, max length 64
        :param amount: Transfer amount
        :param currency: Currency (only USDT supported currently)
        :param sub_account: Sub-account username
        :return:
        """
        param = {
            'requestNo': request_no,
            'amount': amount,
            'currency': currency,
            'subAccount': sub_account
        }
        return self._request_with_params(POST, API_CONTRACT_SUB_TO_MAIN_URL, param, Auth.SIGNED)

    def post_sub_to_main_from_sub_account(self, request_no: str, amount: str, currency: str):
        """Sub-Account to Main-Account Futures Asset Transfer (For Sub Account) (SIGNED)
        Transfer from a sub-account futures wallet to the main-account futures wallet (for sub account)

        POST https://api-cloud-v2.bitmart.com/account/contract/sub-account/sub/v1/sub-to-main

        :param request_no: uuid or other universally unique identifier, max length 64
        :param amount: Transfer amount
        :param currency: Currency (only USDT supported currently)
        :return:
        """
        param = {
            'requestNo': request_no,
            'amount': amount,
            'currency': currency
        }
        return self._request_with_params(POST, API_CONTRACT_SUB_TO_MAIN_FROM_SUB_URL, param, Auth.SIGNED)

    def post_main_to_sub(self, request_no: str, amount: str, currency: str, sub_account: str):
        """Main-Account to Sub-Account Futures Asset Transfer (For Main Account) (SIGNED)
        Transfer from the main-account futures wallet to a sub-account futures wallet (for main account)

        POST https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/main-to-sub

        :param request_no: uuid or other universally unique identifier, max length 64
        :param amount: Transfer amount
        :param currency: Currency (only USDT supported currently)
        :param sub_account: Sub-account username
        :return:
        """
        param = {
            'requestNo': request_no,
            'amount': amount,
            'currency': currency,
            'subAccount': sub_account
        }
        return self._request_with_params(POST, API_CONTRACT_MAIN_TO_SUB_URL, param, Auth.SIGNED)

    def get_sub_transfer_list(self, sub_account: str, limit: int):
        """Get Sub-Account Futures Transfer History (For Main Account) (KEYED)
        Get the futures transfer history of a sub-account (for main account)

        GET https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/transfer-list

        :param sub_account: Sub-account username
        :param limit: Recent N records (value range 1-100)
        :return:
        """
        param = {
            'subAccount': sub_account,
            'limit': limit
        }
        return self._request_with_params(GET, API_CONTRACT_SUB_TRANSFER_LIST_URL, param, Auth.KEYED)

    def get_sub_transfer_history(self, limit: int):
        """Get Account Futures Transfer History (For Main and Sub Account) (KEYED)
        Get account futures transfer history (for both main and sub account)

        GET https://api-cloud-v2.bitmart.com/account/contract/sub-account/v1/transfer-history

        :param limit: Recent N records (value range 1-100)
        :return:
        """
        param = {
            'limit': limit
        }
        return self._request_with_params(GET, API_CONTRACT_SUB_TRANSFER_HISTORY_URL, param, Auth.KEYED)

    def get_sub_wallet(self, sub_account: str, currency: str = None):
        """Get Sub-Account Futures Wallet Balance (For Main Account) (KEYED)
        Get the futures wallet balance of a sub-account (for main account)

        GET https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/wallet

        :param sub_account: Sub-account username
        :param currency: Currency
        :return:
        """
        param = {
            'subAccount': sub_account
        }

        if currency:
            param['currency'] = currency

        return self._request_with_params(GET, API_CONTRACT_SUB_WALLET_URL, param, Auth.KEYED)
