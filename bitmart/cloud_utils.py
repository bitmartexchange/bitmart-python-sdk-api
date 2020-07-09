import hmac
import datetime

from . import cloud_consts as c


def sign(message, secret_key):
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    return mac.hexdigest()


# timestamp + "#" + memo + "#" + queryString
def pre_substring(timestamp, memo, body):
    return f'{str(timestamp)}#{memo}#{body}'


def get_header(api_key, sign, timestamp):
    header = dict()
    header[c.CONTENT_TYPE] = c.APPLICATION_JSON
    header[c.USER_AGENT] = c.VERSION

    if api_key:
        header[c.X_BM_KEY] = api_key
    if sign:
        header[c.X_BM_SIGN] = sign
    if timestamp:
        header[c.X_BM_TIMESTAMP] = str(timestamp)

    return header


def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        url = url + str(key) + '=' + str(value) + '&'

    return url[0:-1]


def get_timestamp():
    return str(datetime.datetime.now().timestamp() * 1000).split('.')[0]
