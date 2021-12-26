from .base import *
ALLOWED_HOSTS = ['15.164.78.65']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends,postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'Database-1',
        'PASSWORD': 'VPzeQKD4De0WwbX+2W(R?PN`KOUpAAHG',
        'HOST': 'ls-a9c73b1d47e0286622fb5bbae69cfa6a15a6002e.ckgdtqvxpuki.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
