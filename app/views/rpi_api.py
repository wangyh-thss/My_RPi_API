# encoding=utf-8

from flask import Blueprint, request, g
from app.common.views_helper import authenticate, load_data, save_data
from app.common.logger import get_logger
from app.common.json_builder import error_result, success_result
from app.common.error_code import ErrorCode
from config import HEARTBEAT_DATA_FILE


rpi_api_blueprint = Blueprint('rpi_api', __name__)
logger = get_logger()


@rpi_api_blueprint.route('/api/heartbeat', methods=['GET', 'POST'])
def heartbeat():
    params = request.args or request.get_json() or request.form
    try:
        key = params['key']
        name = params['name']
    except KeyError:
        return error_result(ErrorCode.ERROR_INVALID_PARAM)
    if authenticate(key):
        return error_result(ErrorCode.ERROR_INVALID_KEY)
    remote_addr = request.remote_addr
    logger.debug('Receive heartbeat from %s(%s)' % (remote_addr, name))
    data = load_data(HEARTBEAT_DATA_FILE)
    data['remote_ips'].update({name: remote_addr})
    save_data(data, HEARTBEAT_DATA_FILE)
    return success_result()


@rpi_api_blueprint.route('/api/heartbeat/data', methods=['GET'])
def get_heartbeat_data():
    data = load_data(HEARTBEAT_DATA_FILE)
    return success_result(data)
