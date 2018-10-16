from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'boong_bank',
        'USER': 'boong_teller',
        'PASSWORD': '9bEoYmBgnyLnFA4P2Zn0dlNUNIu6wt2KddpHKv86gggXUhjoWyDstUvNSRVHhqg',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
