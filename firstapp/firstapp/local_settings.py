import os
from pathlib import Path
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "foo"

DEBUG = 1

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']


DATABASES = {
    'default': {
        'ENGINE': env("SQL_ENGINE", default="0"'django.db.backends.sqlite3'),
        "NAME": env("SQL_DATABASE", default= os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": env("SQL_USER", default="user"),
        "PASSWORD": env("SQL_PASSWORD", default="password"),
        "HOST": env("SQL_HOST", default="localhost"),
        "PORT": env("SQL_PORT", default="5432"),
    }
}


STATIC_ROOT = "/var/www/example.com/static/"
STATICFILES_DIRS = BASE_DIR / "main/static",