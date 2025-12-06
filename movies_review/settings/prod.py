import os
from .settings import *

DEBUG = False
SECRET_KEY = os.environ["APP_SECRET_KEY"]
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "movies_review",
        "USER": "root",
        "PASSWORD": "nassim",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}