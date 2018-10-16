from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'boong_bank',
        'USER': 'boong',
        'PASSWORD': get_env_variable('BOONG_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
