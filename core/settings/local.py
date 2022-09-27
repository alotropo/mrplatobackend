
from core.settings.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "mrplatofixed",
        'USER': "postgres",
        'PASSWORD':"123",
        'HOST':"localhost",
        # 'PORT':5432
    },
    
    'mrplatoflexible': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "mrplatoflexible",
        'USER': "postgres",
        'PASSWORD':"123",
        'HOST':"localhost",
        # 'PORT':5432
    }
}