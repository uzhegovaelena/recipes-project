
# installed app
# middleware
# root_urlconf
# templates
# wsgi
# database
# AUTH_PASSWORD_VALIDATORS
# LANGUAGE_CODE
# TIME_ZONE
#STATIC_URL
# DEFAULT_AUTO_FIELD


import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'app.yaml'

def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

config = get_config(config_path)
