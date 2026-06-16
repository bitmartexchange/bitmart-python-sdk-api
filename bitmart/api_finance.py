from bitmart.lib.cloud_client import CloudClient
from bitmart.lib.cloud_consts import *


class APIFinance(CloudClient):

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

    # ---------- Assets ----------

    def get_earn_assets(self):
        """Get Earn Account Holdings (KEYED)
        Query the holdings of the finance (earn) account

        GET https://api-cloud.bitmart.com/newearn/cloud/v1/earn

        :return:
        """
        return self._request_without_params(GET, API_FINANCE_EARN_URL, Auth.KEYED)

    # ---------- Flexible Savings ----------

    def get_savings_product(self, current_page: int, size_page: int, coin_name: str = None):
        """Get Flexible Savings Product List (KEYED)
        Query the flexible savings product list

        GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/product

        :param current_page: Current page number
        :param size_page: Records per page, max 100
        :param coin_name: Filter by coin name (e.g. USDT)
        :return:
        """
        param = {
            'currentPage': current_page,
            'sizePage': size_page
        }

        if coin_name:
            param['coinName'] = coin_name

        return self._request_with_params(GET, API_FINANCE_SAVING_PRODUCT_URL, param, Auth.KEYED)

    def post_savings_subscribe(self, product_id: str, amount: str, request_no: str):
        """Subscribe Flexible Savings (SIGNED)
        Subscribe to a flexible savings product

        POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/subscribe

        :param product_id: Product ID
        :param amount: Subscribe amount
        :param request_no: Unique request number, 20-digit numeric, used for idempotency
        :return:
        """
        param = {
            'productId': product_id,
            'amount': amount,
            'requestNo': request_no
        }
        return self._request_with_params(POST, API_FINANCE_SAVING_SUBSCRIBE_URL, param, Auth.SIGNED)

    def post_savings_redeem(self, earn_id: str, amount: str, request_no: str):
        """Redeem Flexible Savings (SIGNED)
        Redeem a flexible savings holding

        POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/redeem

        :param earn_id: Earn order ID
        :param amount: Redeem amount
        :param request_no: Unique request number, 20-digit numeric, used for idempotency
        :return:
        """
        param = {
            'earnId': earn_id,
            'amount': amount,
            'requestNo': request_no
        }
        return self._request_with_params(POST, API_FINANCE_SAVING_REDEEM_URL, param, Auth.SIGNED)

    def get_savings_holdings(self, current_page: int, size_page: int, coin_name: str = None, product_id: str = None):
        """Get Flexible Savings Holdings (KEYED)
        Query flexible savings holdings

        GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/earn

        :param current_page: Current page number
        :param size_page: Records per page, max 100
        :param coin_name: Filter by coin name (e.g. USDT)
        :param product_id: Filter by product ID
        :return:
        """
        param = {
            'currentPage': current_page,
            'sizePage': size_page
        }

        if coin_name:
            param['coinName'] = coin_name

        if product_id:
            param['productId'] = product_id

        return self._request_with_params(GET, API_FINANCE_SAVING_EARN_URL, param, Auth.KEYED)

    def get_savings_records(self, type: str, current_page: int, size_page: int,
                            start_time: int = None, end_time: int = None, coin_name: str = None):
        """Get Flexible Savings History Records (KEYED)
        Query flexible savings history records

        GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/record

        :param type: Record type
                    - subscribe
                    - redeem
                    - interest
        :param current_page: Current page number
        :param size_page: Records per page, max 100
        :param start_time: Start time in milliseconds
        :param end_time: End time in milliseconds
        :param coin_name: Filter by coin name (e.g. USDT)
        :return:
        """
        param = {
            'type': type,
            'currentPage': current_page,
            'sizePage': size_page
        }

        if start_time:
            param['startTime'] = start_time

        if end_time:
            param['endTime'] = end_time

        if coin_name:
            param['coinName'] = coin_name

        return self._request_with_params(GET, API_FINANCE_SAVING_RECORD_URL, param, Auth.KEYED)

    # ---------- Fixed Savings ----------

    def get_fixed_product(self, current_page: int, size_page: int, coin_name: str = None):
        """Get Fixed Savings Product List (KEYED)
        Query the fixed savings product list

        GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/product

        :param current_page: Current page number, default 1
        :param size_page: Records per page, default 1, max 100
        :param coin_name: Coin name
        :return:
        """
        param = {
            'currentPage': current_page,
            'sizePage': size_page
        }

        if coin_name:
            param['coinName'] = coin_name

        return self._request_with_params(GET, API_FINANCE_FIXED_PRODUCT_URL, param, Auth.KEYED)

    def post_fixed_subscribe(self, product_id: str, amount: str, request_no: str, auto_subscribe: str):
        """Subscribe Fixed Savings (SIGNED)
        Subscribe to a fixed savings product

        POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/subscribe

        :param product_id: Product ID
        :param amount: Subscribe amount
        :param request_no: Unique request number, length 20, numeric 0-9
        :param auto_subscribe: Auto subscribe type
                    - OFF
                    - REINVEST_FLEXIBLE
                    - REINVEST_FIXED
        :return:
        """
        param = {
            'productId': product_id,
            'amount': amount,
            'requestNo': request_no,
            'autoSubscribe': auto_subscribe
        }
        return self._request_with_params(POST, API_FINANCE_FIXED_SUBSCRIBE_URL, param, Auth.SIGNED)

    def get_fixed_holdings(self, current_page: int, size_page: int, coin_name: str = None, product_id: str = None):
        """Get Fixed Savings Holdings (KEYED)
        Query fixed savings holdings

        GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/earn

        :param current_page: Current page number, default 1
        :param size_page: Records per page, default 1, max 100
        :param coin_name: Coin name
        :param product_id: Product ID
        :return:
        """
        param = {
            'currentPage': current_page,
            'sizePage': size_page
        }

        if coin_name:
            param['coinName'] = coin_name

        if product_id:
            param['productId'] = product_id

        return self._request_with_params(GET, API_FINANCE_FIXED_EARN_URL, param, Auth.KEYED)

    def get_fixed_records(self, type: str, current_page: int, size_page: int,
                          start_time: int = None, end_time: int = None, coin_name: str = None):
        """Get Fixed Savings History Records (KEYED)
        Query fixed savings history records

        GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/record

        :param type: Record type
                    - subscribe
                    - redeem
                    - interest
        :param current_page: Current page number, default 1
        :param size_page: Records per page, default 1, max 100
        :param start_time: Start time in milliseconds (e.g. 1681701557927)
        :param end_time: End time in milliseconds (e.g. 1681701557927)
        :param coin_name: Coin name
        :return:
        """
        param = {
            'type': type,
            'currentPage': current_page,
            'sizePage': size_page
        }

        if start_time:
            param['startTime'] = start_time

        if end_time:
            param['endTime'] = end_time

        if coin_name:
            param['coinName'] = coin_name

        return self._request_with_params(GET, API_FINANCE_FIXED_RECORD_URL, param, Auth.KEYED)

    def post_fixed_redeem(self, earn_id: str, request_no: str):
        """Early Redeem Fixed Savings (SIGNED)
        Redeem a fixed savings holding ahead of maturity

        POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/redeem

        :param earn_id: Earn order ID
        :param request_no: Unique request number, length 20, numeric 0-9
        :return:
        """
        param = {
            'earnId': earn_id,
            'requestNo': request_no
        }
        return self._request_with_params(POST, API_FINANCE_FIXED_REDEEM_URL, param, Auth.SIGNED)

    def post_fixed_modify_auto_renewal(self, earn_id: str, auto_subscribe: str):
        """Modify Fixed Savings Auto-Renewal (SIGNED)
        Modify the auto-renewal (auto reinvest) setting of a fixed savings order

        POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/fixed/subscribe/operate

        :param earn_id: Earn order ID
        :param auto_subscribe: Auto subscribe type
                    - OFF
                    - REINVEST_FLEXIBLE
                    - REINVEST_FIXED
        :return:
        """
        param = {
            'earnId': earn_id,
            'autoSubscribe': auto_subscribe
        }
        return self._request_with_params(POST, API_FINANCE_FIXED_SUBSCRIBE_OPERATE_URL, param, Auth.SIGNED)

    # ---------- Auto Earn ----------

    def post_auto_subscribe_toggle(self, auto_subscribe: str):
        """Toggle Global Auto Earn (SIGNED)
        Enable or disable the global auto subscribe for flexible savings

        POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/subscribe/batch/operate

        :param auto_subscribe: Auto subscribe switch
                    - open
                    - close
        :return:
        """
        param = {
            'autoSubscribe': auto_subscribe
        }
        return self._request_with_params(POST, API_FINANCE_SAVING_SUBSCRIBE_BATCH_OPERATE_URL, param, Auth.SIGNED)

    def get_auto_subscribe_status(self):
        """Get Global Auto Earn Status (KEYED)
        Query the global auto subscribe status

        GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/subscribe/batch

        :return:
        """
        return self._request_without_params(GET, API_FINANCE_SAVING_SUBSCRIBE_BATCH_URL, Auth.KEYED)

    def post_flexible_auto_subscribe_toggle(self, product_id: str, auto_subscribe: str):
        """Toggle Flexible Product Auto Subscribe (SIGNED)
        Enable or disable auto subscribe for a specific flexible savings product

        POST https://api-cloud.bitmart.com/newearn/cloud/v1/saving/subscribe/operate

        :param product_id: Product ID
        :param auto_subscribe: Auto subscribe switch
                    - open
                    - close
        :return:
        """
        param = {
            'productId': product_id,
            'autoSubscribe': auto_subscribe
        }
        return self._request_with_params(POST, API_FINANCE_SAVING_SUBSCRIBE_OPERATE_URL, param, Auth.SIGNED)

    def get_flexible_auto_subscribe_status(self, product_id: str):
        """Get Flexible Product Auto Subscribe Status (KEYED)
        Query the auto subscribe status of a specific flexible savings product

        GET https://api-cloud.bitmart.com/newearn/cloud/v1/saving/subscribe/status

        :param product_id: Product ID
        :return:
        """
        param = {
            'productId': product_id
        }
        return self._request_with_params(GET, API_FINANCE_SAVING_SUBSCRIBE_STATUS_URL, param, Auth.KEYED)
