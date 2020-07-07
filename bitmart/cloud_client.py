import requests
import json
from . import cloud_consts as c, cloud_utils, cloud_exceptions
from .cloud_consts import Auth
from .cloud_log import CloudLog, log


class CloudClient(object):

    def __init__(self, api_key, secret_key, memo, url: str = c.API_URL):

        self.API_KEY = api_key
        self.SECRET_KEY = secret_key
        self.MEMO = memo
        self.URL = url

    @log
    def _request(self, method, request_path, params, auth):
        if method == c.GET or method == c.DELETE:
            url = self.URL + request_path + cloud_utils.parse_params_to_str(params)
        else:
            url = self.URL + request_path

        # set body
        body = json.dumps(params) if method == c.POST else ""

        # set header
        if auth == Auth.NONE:
            header = cloud_utils.get_header(api_key=None, sign=None, timestamp=None)
        elif auth == Auth.KEYED:
            header = cloud_utils.get_header(self.API_KEY, sign=None, timestamp=None)
        else:
            timestamp = cloud_utils.get_timestamp()
            sign = cloud_utils.sign(cloud_utils.pre_substring(timestamp, self.MEMO, str(body)), self.SECRET_KEY)
            header = cloud_utils.get_header(self.API_KEY, sign, timestamp)

        if CloudLog.is_debug():
            print("------------------------------------------")
            print("[", method, "]", url)
            print("request")
            print("\theaders:", header)
            if body:
                print("\tbody:", body)

        # send request
        response = None
        if method == c.GET:
            response = requests.get(url, headers=header)
        elif method == c.POST:
            response = requests.post(url, data=body, headers=header)
        elif method == c.DELETE:
            response = requests.delete(url, headers=header)

        # exception handle
        if not str(response.status_code) == '200':
            raise cloud_exceptions.APIException(response)
        try:
            res_header = response.headers
            r = dict()
            try:
                r['Remaining'] = res_header['X-BM-RateLimit-Remaining']
                r['Limit'] = res_header['X-BM-RateLimit-Limit']
                r['Reset'] = res_header['X-BM-RateLimit-Reset']
            except:
                pass
            return response.json(), r

        except ValueError:
            raise cloud_exceptions.RequestException('Invalid Response: %s' % response.text)

    def _request_without_params(self, method, request_path, auth=Auth.NONE):
        return self._request(method, request_path, {}, auth)

    def _request_with_params(self, method, request_path, params, auth=Auth.NONE):
        return self._request(method, request_path, params, auth)
