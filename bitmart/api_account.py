from .cloud_client import CloudClient
from .cloud_consts import *


class APIAccount(CloudClient):

    def __init__(self, api_key, secret_key, memo, url=API_URL):
        CloudClient.__init__(self, api_key, secret_key, memo, url)

    # GET https://api-cloud.bitmart.com/account/v1/currencies
    def get_currencies(self):
        return self._request_without_params(GET, API_ACCOUNT_CURRENCIES_URL)

    # GET https://api-cloud.bitmart.com/account/v1/wallet
    def get_wallet(self, accountType: str):
        param = {
            'account_type': accountType
        }
        return self._request_with_params(GET, API_ACCOUNT_WALLET_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/account/v1/deposit/address
    def get_deposit_address(self, currency: str):
        param = {
            'currency': currency
        }
        return self._request_with_params(GET, API_ACCOUNT_DEPOSIT_ADDRESS_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/account/v1/withdraw/charge
    def get_withdraw_charge(self, currency: str):
        param = {
            'currency': currency
        }
        return self._request_with_params(GET, API_ACCOUNT_WITHDRAW_CHARGE_URL, param, Auth.KEYED)

    # POST https://api-cloud.bitmart.com/account/v1/withdraw/apply
    def post_withdraw_apply(self, currency: str, amount: str, destination: str, address: str, address_memo: str):
        param = {
            'currency': currency,
            'amount': amount,
            'destination': destination,
            'address': address,
            'address_memo': address_memo
        }
        return self._request_with_params(POST, API_ACCOUNT_WITHDRAW_APPLY_URL, param, Auth.SIGNED)

    # GET https://api-cloud.bitmart.com/account/v1/deposit-withdraw/history
    def get_deposit_withdraw_history(self, currency: str, operationType: str, offset: int, limit: int):
        param = {
            'currency': currency,
            'operation_type': operationType,
            'offset': offset,
            'limit': limit
        }
        return self._request_with_params(GET, API_ACCOUNT_DEPOSIT_WITHDRAW_HISTORY_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/account/v1/deposit-withdraw/detail
    def get_deposit_withdraw_detail(self, id:str):
        param = {
            'id': id
        }
        return self._request_with_params(GET, API_ACCOUNT_DEPOSIT_WITHDRAW_DETAIL, param, Auth.KEYED)
