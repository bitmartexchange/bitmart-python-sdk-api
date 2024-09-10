import hmac
import datetime
import time
import zlib

from bitmart.lib import cloud_consts as c


def sign(message, secret_key):
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    return mac.hexdigest()


# timestamp + "#" + memo + "#" + queryString
def pre_substring(timestamp, memo, body):
    return f'{str(timestamp)}#{memo}#{body}'


def get_header(api_key, sign, timestamp, headers=None):
    header = headers if headers is not None else {}

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


def single_stream(stream):
    if isinstance(stream, str):
        return True
    elif isinstance(stream, list):
        return False
    else:
        raise ValueError("Invalid stream name, expect string or array")


def inflate(data):
    decompress = zlib.decompressobj(
        -zlib.MAX_WBITS
    )
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated.decode('UTF-8')


def config_logging(logging, logging_level, log_file: str = None):
    """Configures logging to provide a more detailed log format, which includes date time in UTC
    Example: 2021-11-02 19:42:04.849 UTC <logging_level> <log_name>: <log_message>

    Args:
        logging: python logging
        logging_level (int/str): For logging to include all messages with log levels >= logging_level. Ex: 10 or "DEBUG"
                                 logging level should be based on https://docs.python.org/3/library/logging.html#logging-levels
    Keyword Args:
        log_file (str, optional): The filename to pass the logging to a file, instead of using console. Default filemode: "a"
    """

    logging.Formatter.converter = time.gmtime  # date time in GMT/UTC
    logging.basicConfig(
        level=logging_level,
        filename=log_file,
        format="%(asctime)s.%(msecs)03d UTC %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
