import os
import json

CLIENT_ID = ''
CLIENT_SECRET = ''
HOST = ''

_settings_locals = locals()


def update_config_from_json(filename):
    if os.path.exists(filename):
        with open(filename) as json_file:
            _settings_locals.update(json.loads(json_file.read()))

update_config_from_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json'))