import logging

HOST_NAME = 'localhost' # TODO
SERVER_PORT = 10003 # TODO
BACKEND_BASE_ADDRESS = 'localhost:10004' # TODO
BACKEND_WEB_SOCKET_URI = f'ws://{BACKEND_BASE_ADDRESS}/ws'

LOG_LVL_DEV = logging.DEBUG
LOG_LVL_PROD = logging.INFO
LOG_CONFIG_PATH = 'src/config/logging.conf'

ENVIRONMENT = 'development'