import environ

from core.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    'default': {},
    'mrplatofixed': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "d4v2i06c2qbh1n",
        'USER': "oykesrrufxvjnr",
        'PASSWORD':"b85e260cec3a65069aa2a16cea511772c2625afbbd36db2ebe372f2a1b1ca126",
        'HOST':"ec2-44-207-133-100.compute-1.amazonaws.com",
        # 'PORT':5432
    },
    
    'mrplatoflexible': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "d6a3klv5pdnorm",
        'USER': "fhmkwviotlezwg",
        'PASSWORD':"82194719fbd4c6adc22ccee8675f28930ec0487c8b6fc30183cd65e99a36d109",
        'HOST':"ec2-34-200-205-45.compute-1.amazonaws.com",
        # 'PORT':5432
    }
}