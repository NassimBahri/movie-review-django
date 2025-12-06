import os
from .settings import *

DEBUG = False
SECRET_KEY = os.environ["APP_SECRET_KEY"]
ALLOWED_HOSTS = [
    'movie-review-django-q2vd.onrender.com'
]
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "movies_review",
        "USER": "nassim",
        "PASSWORD": "vLsiFXxQmrdN3LHFHGEGlDbOkylsK1ry",
        "HOST": "dpg-d4q922je5dus73ejk6s0-a",
        "PORT": "5432",
    }
}