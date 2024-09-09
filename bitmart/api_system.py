from bitmart.lib.cloud_client import CloudClient
from bitmart.lib.cloud_consts import *


class APISystem(CloudClient):

    def __init__(self,  url: str = API_URL, timeout: tuple = TIMEOUT, headers=None, logger=None):
        """
        :param url: https://api-cloud.bitmart.com
        :param timeout: (2, 10)
        """
        CloudClient.__init__(self, '', '', '', url, timeout, headers, logger)

    def get_system_time(self):
        """Get System Time
        Get system time

        GET https://api-cloud.bitmart.com/system/time

        :return:
        """
        return self._request_without_params(GET, API_SYSTEM_TIME_URL)

    def get_system_service(self):
        """Get System Service Status
        Get system service status

        GET https://api-cloud.bitmart.com/system/service

        :return:
        """
        return self._request_without_params(GET, API_SYSTEM_SERVICE_URL)