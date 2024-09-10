import logging

import requests
import json
from bitmart.lib import cloud_utils, cloud_exceptions
from . import cloud_consts as c
from bitmart.__version__ import __version__
from .cloud_consts import Auth


class CloudClient(object):

    def __init__(self, api_key, secret_key, memo, url, timeout, headers=None, logger=None):
        """
        :param api_key: Get from bitmart API page.
        :param secret_key: Get from bitmart API page.
        :param memo: Get from bitmart API page.
        :param url: Request Domain URL.
        :param timeout: (connection timeout, read timeout).
        :param headers: Custom request headers
        :param logger: Logging
        """
        self.API_KEY = api_key
        self.SECRET_KEY = secret_key
        self.MEMO = memo
        self.URL = url
        self.TIMEOUT = timeout
        self.HEADERS = headers
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "User-Agent": "bitmart-python-sdk-api/" + __version__,
            }
        )

        if not logger:
            self._logger = logging.getLogger(__name__)
        else:
            self._logger = logger

    def _request(self, method, request_path, params, auth):
        if method == c.GET or method == c.DELETE:
            url = self.URL + request_path + cloud_utils.parse_params_to_str(params)
        else:
            url = self.URL + request_path

        # set body
        body = json.dumps(params) if method == c.POST else ""

        # set header
        if auth == Auth.NONE:
            header = cloud_utils.get_header(api_key=None, sign=None, timestamp=None, headers=self.HEADERS)
        elif auth == Auth.KEYED:
            header = cloud_utils.get_header(self.API_KEY, sign=None, timestamp=None, headers=self.HEADERS)
        else:
            timestamp = cloud_utils.get_timestamp()
            sign = cloud_utils.sign(cloud_utils.pre_substring(timestamp, self.MEMO, str(body)), self.SECRET_KEY)
            header = cloud_utils.get_header(self.API_KEY, sign, timestamp, headers=self.HEADERS)

        self._logger.debug(f"[{method}] url={url}")
        if body:
            self._logger.debug(f"[PARAMS]:\nheader: {header}\nbody: {body}\n")

        # send request
        response = None
        if method == c.GET:
            response = self.session.get(url, headers=header, timeout=self.TIMEOUT)
        elif method == c.POST:
            response = self.session.post(url, data=body, headers=header, timeout=self.TIMEOUT)
        elif method == c.DELETE:
            response = self.session.delete(url, headers=header, timeout=self.TIMEOUT)

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
                r['Mode'] = res_header['X-BM-RateLimit-Mode']
            except:
                pass
            result = response.json()
            self._logger.debug(f"response: {result}\n")
            return result, r

        except ValueError:
            raise cloud_exceptions.RequestException('Invalid Response: %s' % response.text)

    def _request_without_params(self, method, request_path, auth=Auth.NONE):
        return self._request(method, request_path, {}, auth)

    def _request_with_params(self, method, request_path, params, auth=Auth.NONE):
        return self._request(method, request_path, params, auth)
