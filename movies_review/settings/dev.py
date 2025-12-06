from .settings import *

DEBUG = True

SECRET_KEY = 'django-insecure-a**d24r3moc1i!^^=1n*xv6=khsa443#7!=lb2+8^qn-qi9(tg'

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