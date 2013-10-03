from .base import *
import os

########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '',
        'PORT': '5432',
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
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    STATICFILES_STORAGE = 'storage.CachedS3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_IS_GZIPPED = True
    AWS_QUERYSTRING_EXPIRE = 7200
    AWS_S3_SECURE_URLS = True
    STATIC_URL = S3_URL
########## END AMAZON S3 CONFIGURATION


##########  COMPRESS CONFIGURATION
if not DEBUG:
    COMPRESS_ENABLED = not DEBUG
    COMPRESS_OFFLINE = True
    COMPRESS_ROOT = STATIC_ROOT
    COMPRESS_STORAGE = 'storage.CachedS3BotoStorage'

    COMPRESS_URL = S3_URL
    COMPRESS_PRECOMPILERS = (
        ('text/coffeescript', 'coffee --compile --stdio'),
        ('text/less', 'lessc {infile} > {outfile}')
    )

##########  COMPRESS CONFIGURATION

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = '*'
