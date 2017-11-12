# encoding=utf-8

import json

from config import SECRET_KEY


def authenticate(key):
    return key == SECRET_KEY


def load_data(data_file):
    data = {
        'remote_ips': dict()
    }
    try:
        with open(data_file, 'r') as f:
            stored_data = json.load(f)
        data.update(stored_data)
    except:
        pass
    return data


def save_data(data, data_file):
    init_data = {
        'remote_ips': dict()
    }
    init_data.update(data)
    with open(data_file, 'w') as f:
        json.dump(init_data, f)
