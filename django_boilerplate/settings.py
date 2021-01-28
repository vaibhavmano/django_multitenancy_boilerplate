SECRET_KEY = '-3wb@c+t)1xc_khg0nm-8^(f!i85l&9@fwblfryz3uny^!1duq'
from django_boilerplate.config import DjangoConfig

if DjangoConfig.ENVIRONMENT == "TEST":
    from django_boilerplate.environments.test import *

if DjangoConfig.ENVIRONMENT == "PRODUCTION":
    from django_boilerplate.environments.production import *

if DjangoConfig.ENVIRONMENT == "DEBUG":
    from django_boilerplate.environments.debug import *
