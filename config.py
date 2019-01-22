import os

DEBUG = os.getenv('DEBUG', False)
DEFAULT_DATA_DIR = os.getenv('ELIMAGE_DATA_DIR','/tmp')
DEFAULT_PORT = 8888
DB = 'elimage.db'

XHEADERS = True # you may set this to false if not behind another server
CLOUDFLARE = False

UPLOAD_PASSWORD = os.getenv('PASSWORD', '')
