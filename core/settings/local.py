
from core.settings.base import *


import environ

env = environ.Env()
environ.Env.read_env()


EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

DATABASES = {
    'default':{},
    'mrplatofixed': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "mrplatofixed",
        'USER': "postgres",
        'PASSWORD':"postgres",
        'HOST':"db",
        # 'PORT':5432
    },
    
    'mrplatoflexible': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "mrplatoflexible",
        'USER': "postgres",
        'PASSWORD':"postgres",
        'HOST':"db",
        # 'PORT':5432
    }
}

