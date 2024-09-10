from bitmart.lib.cloud_client import CloudClient
from bitmart.lib.cloud_consts import *


class APIAccount(CloudClient):

    def __init__(self, api_key: str = "", secret_key: str = "", memo: str = "", url: str = API_URL, timeout: tuple = TIMEOUT, headers=None, logger=None):
        """
        Create api key from https://www.bitmart.com/api-config/en-US
        :param api_key: your access key
        :param secret_key: your secret key
        :param memo: your memo
        :param url: https://api-cloud.bitmart.com
        :param timeout: (2, 10)
        """
        CloudClient.__init__(self, api_key, secret_key, memo, url, timeout, headers, logger)

    def get_currencies(self):
        """Get Currencies
        Gets the currency of the asset for withdrawal

        GET https://api-cloud.bitmart.com/account/v1/currencies

        :return:
        """
        return self._request_without_params(GET, API_ACCOUNT_CURRENCIES_URL)

    def get_wallet(self, currency: str = None):
        """Get Account Balance (KEYED)
        Gets Account Balance

        GET https://api-cloud.bitmart.com/account/v1/wallet

        :param currency: Token symbol, e.g., 'BTC'
        :return:
        """
        param = {}

        if currency:
            param['currency'] = currency

        return self._request_with_params(GET, API_ACCOUNT_WALLET_URL, param, Auth.KEYED)

    def get_deposit_address(self, currency: str):
        """Deposit Address (KEYED)
        Gets Deposit Address

        GET https://api-cloud.bitmart.com/account/v1/deposit/address

        :param currency: Token symbol, e.g., 'BTC'
        :return:
        """
        param = {
            'currency': currency
        }
        return self._request_with_params(GET, API_ACCOUNT_DEPOSIT_ADDRESS_URL, param, Auth.KEYED)

    def get_withdraw_charge(self, currency: str):
        """Withdraw Quota (KEYED)
        Query withdraw quota for currencies

        GET https://api-cloud.bitmart.com/account/v1/withdraw/charge

        :param currency: Token symbol, e.g., 'BTC'
        :return:
        """
        param = {
            'currency': currency
        }
        return self._request_with_params(GET, API_ACCOUNT_WITHDRAW_CHARGE_URL, param, Auth.KEYED)

    def post_withdraw_apply(self, currency: str, amount: str,
                            destination: str = None, address: str = None, address_memo: str = None,
                            type: int = None, value: str = None, area_code: str = None):
        """Withdraw (SIGNED)
        Creates a withdraw request from spot account to an external address

        POST https://api-cloud.bitmart.com/account/v1/withdraw/apply

        :param currency: Token symbol, e.g., 'BTC'
        :param amount: The amount of currency to withdraw
        :param destination: withdrawal address
                        -To Digital Address=Withdraw to the digital currency address
        :param address: Address (only the address added on the official website is supported)
        :param address_memo: Tag(tag Or payment_id Or memo)
        :param type: Account type 1=CID 2=Email 3=Phone
        :param value: Account
        :param area_code: Phone area code, required when account type is phone, e.g.: 61
        :return:
        """
        param = {
            'currency': currency,
            'amount': amount,
        }

        # Parameters for Withdraw to the blockchain
        if address:
            param['address'] = address

        if address_memo:
            param['address_memo'] = address_memo

        if destination:
            param['destination'] = destination

        # Parameters for Withdraw to BitMart account
        if type:
            param['type'] = type
        if value:
            param['value'] = value
        if area_code:
            param['areaCode'] = area_code

        return self._request_with_params(POST, API_ACCOUNT_WITHDRAW_APPLY_URL, param, Auth.SIGNED)

    def get_deposit_withdraw_history_v2(self, operation_type: str, n: int, currency: str = None):
        """Get Deposit And Withdraw History (KEYED)
        Search for all existed withdraws and deposits and return their latest status.

        GET https://api-cloud.bitmart.com/account/v2/deposit-withdraw/history


        :param currency: Token symbol, e.g., 'BTC'
        :param operation_type: type
                    -deposit=deposit
                    -withdraw=withdraw
        :param n: Recent N records (value range 1-100)
        :return:
        """
        param = {
            'operation_type': operation_type,
            'N': n
        }

        if currency:
            param['currency'] = currency

        return self._request_with_params(GET, API_ACCOUNT_DEPOSIT_WITHDRAW_HISTORY_V2_URL, param, Auth.KEYED)

    def get_deposit_withdraw_detail(self, id: str):
        """Get A Deposit Or Withdraw Detail (KEYED)
        Query a single charge record

        GET https://api-cloud.bitmart.com/account/v1/deposit-withdraw/detail

        :param id: withdraw_id or deposit_id
        :return:
        """
        param = {
            'id': id
        }
        return self._request_with_params(GET, API_ACCOUNT_DEPOSIT_WITHDRAW_DETAIL, param, Auth.KEYED)

    def get_margin_account_details_isolated(self, symbol=None):
        """Get Margin Account Details(Isolated) (KEYED)
        Applicable for isolated margin account inquiries

        GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/account

        :param symbol: Trading pair (e.g. BMX_USDT)
        :return:
        """
        param = {}
        if symbol:
            param['symbol'] = symbol
        return self._request_with_params(GET, API_SPOT_MARGIN_ACCOUNT_DETAILS_ISOLATED, param, Auth.KEYED)

    def margin_asset_transfer(self, symbol: str, currency: str, amount: str, side: str):
        """Margin Asset Transfer (SIGNED)
        For fund transfers between a margin account and spot account

        POST https://api-cloud.bitmart.com/spot/v1/margin/isolated/transfer

        :param symbol: Trading pair (e.g. BMX_USDT)
        :param currency: Token symbol, e.g., 'BTC'
        :param amount: Amount of transfers (precision: 8 decimal places)
        :param side: Transfer direction
                - in=Transfer in
                - out=Transfer out
        :return:
        """
        param = {
            'symbol': symbol,
            'currency': currency,
            'amount': amount,
            'side': side
        }
        return self._request_with_params(POST, API_SPOT_MARGIN_ISOLATED_TRANSFER, param, Auth.SIGNED)

    def get_basic_fee_rate(self):
        """Get Basic Fee Rate (KEYED)
        For querying the base rate of the current user

        GET https://api-cloud.bitmart.com/spot/v1/user_fee
        """
        return self._request_without_params(GET, API_SPOT_BASIC_FEE_RATE, Auth.KEYED)

    def get_actual_trade_fee_rate(self, symbol: str):
        """Get Actual Trade Fee Rate (KEYED)
        For the actual fee rate of the trading pairs

        GET https://api-cloud.bitmart.com/spot/v1/trade_fee

        :param symbol: Trading pair (e.g. BMX_USDT)
        :return:
        """
        param = {
            'symbol': symbol
        }
        return self._request_with_params(GET, API_SPOT_ACTUAL_TRADE_FEE_RATE, param, Auth.KEYED)
