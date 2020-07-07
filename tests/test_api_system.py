# system api
from bitmart.api_system import APISystem

systemAPI = APISystem()


def test_get_system_time():
    """GET https://api-cloud.bitmart.com/system/time"""
    assert systemAPI.get_system_time()[0]['code'] == 1000
    assert systemAPI.get_system_time()[0]['data']['server_time'] > 0


def test_get_system_service():
    """GET https://api-cloud.bitmart.com/system/service"""
    assert systemAPI.get_system_service()[0]['code'] == 1000
