# encoding=utf-8

import logging
from config import LOGGING_LEVEL


def get_logger():
    _logger = logging.Logger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handle = logging.StreamHandler()
    handle.setFormatter(formatter)
    _logger.addHandler(handle)
    return _logger


logger = get_logger()
logger.setLevel(LOGGING_LEVEL)
