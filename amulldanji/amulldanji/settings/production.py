import os

from .partials import *

DEBUG = False

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'amulldanji.storage.S3PipelineManifestStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_ACCESS_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")

STATIC_URL = "https://dwjzjxaefl5j9.cloudfront.net/"
