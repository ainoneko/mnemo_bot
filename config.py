#!/usr/bin/env python3
import logging

import yaml
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)

CONFIG_FILE = './config.yml'

def get_settings():
    # full_file_path = Path(file).parent.joinpath(CRED_FILE)
    full_file_path = Path(CONFIG_FILE)
    with open(full_file_path) as settings:
        settings_data = yaml.load(settings, Loader=yaml.Loader)
    return settings_data




if __name__ == '__main__':
    settings = get_settings()
    logging.debug(f'{settings=}')
    assert settings is not None
    assert settings is not {}
