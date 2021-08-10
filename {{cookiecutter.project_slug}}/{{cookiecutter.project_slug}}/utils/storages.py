{% if cookiecutter.cloud_provider in ['AWS', "MinIO"] %}
from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "dcodexmedia"
    default_acl = 'private'
    file_overwrite = False
    {% if cookiecutter.cloud_provider == 'MinIO' %}
    custom_domain = ""
    {% endif %}
    
{%- elif cookiecutter.cloud_provider == 'GCP' -%}
from storages.backends.gcloud import GoogleCloudStorage


class StaticRootGoogleCloudStorage(GoogleCloudStorage):
    location = "static"
    default_acl = "publicRead"


class MediaRootGoogleCloudStorage(GoogleCloudStorage):
    location = "dcodexmedia"
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False
{%- endif %}
