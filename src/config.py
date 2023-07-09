"""
This file is responsible for reading and writing the config.json file.
"""

import json

CONFIG_PATH = __file__.replace('config.py', '../config.json')

config = None

def get_config(reload_json = False):
    global config
    if (config == None or reload_json):
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
    return config

def set_config(parameter, value = None):
    global config
    if (value == None):
        if (parameter in config):
            config.pop(parameter)
        else:
            return False
    else:
        config[parameter] = value
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=4)
    return True