import os


class DjangoConfig:
    DEBUG = os.environ.get('DEBUG', True)
    DJANGO_SECRET = os.environ.get('DJANGO_SECRET', 'django-s3cret')
    ENVIRONMENT = os.environ.get('ENVIRONMENT', 'DEBUG')


class AwsConfig:
    AWS_DEFAULT_ACL = None
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', None)
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
    AWS_DEFAULT_REGION = os.environ.get('AWS_DEFAULT_REGION', None)
    AWS_MAIL_REGION = os.environ.get('AWS_MAIL_REGION', None)
    AWS_MAIL_ACCESS_KEY_ID = os.environ.get('AWS_MAIL_ACCESS_KEY_ID', None)
    AWS_MAIL_SECRET_ACCESS_KEY = os.environ.get('AWS_MAIL_SECRET_ACCESS_KEY', None)
    AWS_SUPPORT_MAIL = os.environ.get('AWS_SUPPORT_MAIL_ID', None)


class DatabaseConfig:
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
    DB_NAME = os.environ.get('DB_NAME', 'test_db')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = int(os.environ.get('DB_PORT', 5432))

# Add other related config
# class RedisConfig:
#     HOST = os.environ.get('REDIS_HOST') or 'localhost'
    # PORT = int(os.environ.get('REDIS_PORT')) or 6379
