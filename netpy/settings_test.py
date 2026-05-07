import os
from netpy.settings import *  # noqa: F401, F403

# Pointe sur le conteneur db_test (port 5433, sans persistence)
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'HOST':     os.environ.get('TEST_DB_HOST',     'localhost'),
        'PORT':     os.environ.get('TEST_DB_PORT',     '5433'),
        'NAME':     os.environ.get('TEST_DB_NAME',     'test_netpy'),
        'USER':     os.environ.get('DB_USER',          'netpy'),
        'PASSWORD': os.environ.get('DB_PASSWORD',      'netpy'),
    }
}
