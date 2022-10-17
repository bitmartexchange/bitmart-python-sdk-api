from .cloud_client import CloudClient
from .cloud_consts import *


class APIAccount(CloudClient):

    def __init__(self, api_key, secret_key, memo, url: str = API_URL, timeout: tuple = TIMEOUT):
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout)

    # GET https://api-cloud.bitmart.com/account/v1/currencies
    def get_currencies(self):
        return self._request_without_params(GET, API_ACCOUNT_CURRENCIES_URL)

    # GET https://api-cloud.bitmart.com/account/v1/wallet
    def get_wallet(self, currency: str):
        param = {
            'currency': currency
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

    # GET https://api-cloud.bitmart.com/account/v2/deposit-withdraw/history
    def get_deposit_withdraw_history_v2(self, currency: str, operationType: str, N: int):
        param = {
            'currency': currency,
            'operation_type': operationType,
            'N': N
        }
        return self._request_with_params(GET, API_ACCOUNT_DEPOSIT_WITHDRAW_HISTORY_V2_URL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/account/v1/deposit-withdraw/detail
    def get_deposit_withdraw_detail(self, id: str):
        param = {
            'id': id
        }
        return self._request_with_params(GET, API_ACCOUNT_DEPOSIT_WITHDRAW_DETAIL, param, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/account
    def get_margin_account_details_isolated(self):
        return self._request_without_params(GET, API_SPOT_MARGIN_ACCOUNT_DETAILS_ISOLATED, Auth.KEYED)

    def get_margin_account_details_isolated_by_symbol(self, symbol: str):
        param = {
            'symbol': symbol
        }
        return self._request_with_params(GET, API_SPOT_MARGIN_ACCOUNT_DETAILS_ISOLATED, param, Auth.KEYED)

    # POST https://api-cloud.bitmart.com/spot/v1/margin/isolated/transfer
    def margin_asset_transfer(self, symbol: str, currency: str, amount: str, side: str):
        param = {
            'symbol': symbol,
            'currency': currency,
            'amount': amount,
            'side': side
        }
        return self._request_with_params(POST, API_SPOT_MARGIN_ISOLATED_TRANSFER, param, Auth.SIGNED)

    # GET https://api-cloud.bitmart.com/spot/v1/user_fee
    def get_basic_fee_rate(self):
        return self._request_without_params(GET, API_SPOT_BASIC_FEE_RATE, Auth.KEYED)

    # GET https://api-cloud.bitmart.com/spot/v1/trade_fee
    def get_actual_trade_fee_rate(self, symbol: str):
        param = {
            'symbol': symbol
        }
        return self._request_with_params(GET, API_SPOT_ACTUAL_TRADE_FEE_RATE, param, Auth.KEYED)
