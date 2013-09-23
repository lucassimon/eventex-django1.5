from .base import *
import os

########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': 'postgres',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}
########## END DATABASE CONFIGURATION

INSTALLED_APPS += (
    'gunicorn',
)

##########  AMAZON S3 CONFIGURATION

# 1 - Create the variables envoirement
# AWS_STORAGE_BUCKET_NAME='test'
# 2 - Export the varables
# export AWS_STORAGE_BUCKET_NAME
# 3 - Get the secret and access key in https://console.aws.amazon.com/iam/home?#security_credential

if not DEBUG:
    COMPRESS_ENABLED = not DEBUG
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    STATICFILES_STORAGE = COMPRESS_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    STATIC_URL = COMPRESS_URL = S3_URL
########## END AMAZON S3 CONFIGURATION

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '.eventexlucassimon.com.br'
]
