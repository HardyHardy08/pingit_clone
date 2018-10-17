from .base import *

DEBUG = False

ALLOWED_HOSTS = ['172.104.61.45', 'boongbank.com', ]

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
