# Produkciona konfiguracija
# U produkciji je potrebno da se preimenuje u config.py

HOST_NAME = None # TODO
SERVER_PORT = -1 # TODO
BACKEND_BASE_ADDRESS = None # TODO
BACKEND_WEB_SOCKET_URI = f'ws://{BACKEND_BASE_ADDRESS}/ws'

PRINT_PREFIX = "(script)     "

ENVIRONMENT = 'production'
