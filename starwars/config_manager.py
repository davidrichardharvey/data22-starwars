from definitions import PROJECT_ROOT_DIR
import configparser

_config = configparser.ConfigParser()

_config.read(PROJECT_ROOT_DIR + 'config.ini')

SWAPI_URL = _config['default']['url']
