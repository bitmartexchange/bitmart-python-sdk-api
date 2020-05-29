from .cloud_client import CloudClient
from .cloud_consts import *


class APISystem(CloudClient):

    def __init__(self, url=API_URL):
        CloudClient.__init__(self, '', '', '', url)

    # get system time
    def get_system_time(self):
        return self._request_without_params(GET, API_SYSTEM_TIME_URL)

    # get system service
    def get_system_service(self):
        return self._request_without_params(GET, API_SYSTEM_SERVICE_URL)