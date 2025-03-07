import hmac
import datetime
import os
import time
import zlib
from logging.handlers import TimedRotatingFileHandler

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
    """Configures logging with UTC timestamp and optional daily rotating log files.

    Example log format:
        2025-03-07 19:42:04.849 UTC DEBUG my_logger: Log message

    Args:
        logging: Python logging module
        logging_level (int/str): Log level (e.g., 10 for DEBUG, 20 for INFO)
        log_file (str, optional): Base filename for logs (e.g., "my_log.log"). If provided, logs will rotate daily.
    """

    # Set UTC time format
    logging.Formatter.converter = time.gmtime

    # Define log format
    log_format = "%(asctime)s.%(msecs)03d UTC %(levelname)s %(name)s: %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # Create log formatter
    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

    # Configure logging to console
    logging.basicConfig(level=logging_level, format=log_format, datefmt=date_format)

    # If a log file is provided, enable daily log rotation
    if log_file:
        log_dir = os.path.dirname(log_file) or "."  # Ensure log directory exists
        os.makedirs(log_dir, exist_ok=True)

        # Create a rotating file handler (daily rotation)
        file_handler = TimedRotatingFileHandler(
            filename=log_file,  # This will be the base filename
            when="midnight",  # Rotate at midnight
            interval=1,  # Rotate every 1 day
            backupCount=30,  # Keep the last 7 days of logs
            encoding="utf-8",  # Support Unicode logs
            utc=True  # Use UTC for time-based rotation
        )

        file_handler.setFormatter(formatter)
        file_handler.suffix = "%Y-%m-%d"  # Filename suffix pattern
        logging.getLogger().addHandler(file_handler)

