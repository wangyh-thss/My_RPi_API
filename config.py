# encoding=utf-8

import os
import logging
BASEDIR = os.path.abspath(os.path.dirname(__file__))
LOGGING_LEVEL = logging.DEBUG

# flask
WTF_CSRF_ENABLED = False
SECRET_KEY = '135j@$^J@EQTH135u@$Q^jh^$UJ#U'

HEARTBEAT_DATA_FILE = os.path.join(BASEDIR, 'heartbeat_data.json')
