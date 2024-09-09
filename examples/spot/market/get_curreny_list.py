
import logging

from bitmart.api_spot import APISpot
from bitmart.lib.cloud_exceptions import APIException
from bitmart.lib.cloud_utils import config_logging

config_logging(logging, logging.INFO)
logger = logging.getLogger(__name__)

spotAPI = APISpot(logger=logger)

try:
    response = spotAPI.get_currencies()[0]
    logger.info(response)
except APIException as error:
    logger.error(
        "Found error. status: {}, error message: {}".format(
            error.status_code, error.response
        )
    )
