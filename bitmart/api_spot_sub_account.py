from bitmart.lib.cloud_client import CloudClient
from bitmart.lib.cloud_consts import *


class APISpotSubAccount(CloudClient):

    def __init__(self, api_key: str = "", secret_key: str = "", memo: str = "", url: str = API_URL,
                 timeout: tuple = TIMEOUT, headers=None, logger=None):
        """
        Create api key from https://www.bitmart.com/api-config/en-US
        :param api_key: your access key
        :param secret_key: your secret key
        :param memo: your memo
        :param url: https://api-cloud.bitmart.com
        :param timeout: (2, 10)
        """
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout, headers, logger)

    def post_sub_to_main(self, request_no: str, amount: str, currency: str, sub_account: str):
        """Sub-Account to Main-Account (For Main Account) (SIGNED)
        Transfer from a sub-account spot wallet to the main-account spot wallet (for main account)

        POST https://api-cloud.bitmart.com/account/sub-account/main/v1/sub-to-main

        :param request_no: uuid or other universally unique identifier, max length 64
        :param amount: Transfer amount
        :param currency: Currency
        :param sub_account: Sub-account username
        :return:
        """
        param = {
            'requestNo': request_no,
            'amount': amount,
            'currency': currency,
            'subAccount': sub_account
        }
        return self._request_with_params(POST, API_ACCOUNT_SUB_TO_MAIN_URL, param, Auth.SIGNED)

    def post_sub_to_main_from_sub_account(self, request_no: str, amount: str, currency: str):
        """Sub-Account to Main-Account (For Sub Account) (SIGNED)
        Transfer from a sub-account spot wallet to the main-account spot wallet (for sub account)

        POST https://api-cloud.bitmart.com/account/sub-account/sub/v1/sub-to-main

        :param request_no: uuid or other universally unique identifier, max length 64
        :param amount: Transfer amount
        :param currency: Currency
        :return:
        """
        param = {
            'requestNo': request_no,
            'amount': amount,
            'currency': currency
        }
        return self._request_with_params(POST, API_ACCOUNT_SUB_TO_MAIN_FROM_SUB_URL, param, Auth.SIGNED)

    def post_main_to_sub(self, request_no: str, amount: str, currency: str, sub_account: str):
        """Main-Account to Sub-Account (For Main Account) (SIGNED)
        Transfer from the main-account spot wallet to a sub-account spot wallet (for main account)

        POST https://api-cloud.bitmart.com/account/sub-account/main/v1/main-to-sub

        :param request_no: uuid or other universally unique identifier, max length 64
        :param amount: Transfer amount
        :param currency: Currency
        :param sub_account: Sub-account username
        :return:
        """
        param = {
            'requestNo': request_no,
            'amount': amount,
            'currency': currency,
            'subAccount': sub_account
        }
        return self._request_with_params(POST, API_ACCOUNT_MAIN_TO_SUB_URL, param, Auth.SIGNED)

    def post_sub_to_sub(self, request_no: str, amount: str, currency: str, from_account: str, to_account: str):
        """Sub-Account to Sub-Account (For Main Account) (SIGNED)
        Transfer from a sub-account spot wallet to another sub-account spot wallet (for main account)

        POST https://api-cloud.bitmart.com/account/sub-account/main/v1/sub-to-sub

        :param request_no: uuid or other universally unique identifier, max length 64
        :param amount: Transfer amount
        :param currency: Currency
        :param from_account: Transfer-out sub-account username
        :param to_account: Transfer-in sub-account username
        :return:
        """
        param = {
            'requestNo': request_no,
            'amount': amount,
            'currency': currency,
            'fromAccount': from_account,
            'toAccount': to_account
        }
        return self._request_with_params(POST, API_ACCOUNT_SUB_TO_SUB_URL, param, Auth.SIGNED)

    def get_sub_transfer_list(self, move_type: str, n: int, account_name: str = None):
        """Get Sub-Account Transfer History (For Main Account) (KEYED)
        Get the transfer history of sub-accounts (for main account)

        GET https://api-cloud.bitmart.com/account/sub-account/main/v1/transfer-list

        :param move_type: Transfer type, e.g. 'spot to spot'
        :param n: Recent N records (value range 1-100)
        :param account_name: Sub-account username (default: query all sub-accounts)
        :return:
        """
        param = {
            'moveType': move_type,
            'N': n
        }

        if account_name:
            param['accountName'] = account_name

        return self._request_with_params(GET, API_ACCOUNT_SUB_TRANSFER_LIST_URL, param, Auth.KEYED)

    def get_account_transfer_history(self, move_type: str, n: int):
        """Get Account Transfer History (For Main and Sub Account) (KEYED)
        Get account transfer history (for both main and sub account)

        GET https://api-cloud.bitmart.com/account/sub-account/v1/transfer-history

        :param move_type: Transfer type, e.g. 'spot to spot'
        :param n: Recent N records (value range 1-100)
        :return:
        """
        param = {
            'moveType': move_type,
            'N': n
        }
        return self._request_with_params(GET, API_ACCOUNT_SUB_TRANSFER_HISTORY_URL, param, Auth.KEYED)

    def get_sub_spot_wallet(self, sub_account: str, currency: str = None):
        """Get Sub-Account Spot Wallet Balance (For Main Account) (KEYED)
        Get the spot wallet balance of a sub-account (for main account)

        GET https://api-cloud.bitmart.com/account/sub-account/main/v1/wallet

        :param sub_account: Sub-account username
        :param currency: Currency
        :return:
        """
        param = {
            'subAccount': sub_account
        }

        if currency:
            param['currency'] = currency

        return self._request_with_params(GET, API_ACCOUNT_SUB_WALLET_URL, param, Auth.KEYED)

    def get_sub_account_list(self):
        """Get Sub-Account List (For Main Account) (KEYED)
        Get the list of sub-accounts (for main account)

        GET https://api-cloud.bitmart.com/account/sub-account/main/v1/subaccount-list

        :return:
        """
        return self._request_without_params(GET, API_ACCOUNT_SUB_LIST_URL, Auth.KEYED)
