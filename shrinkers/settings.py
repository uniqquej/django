from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--hwc2a(x^c0o%-t105#h1dhv1#b$xgg^2uwj=-jc(%@$x%(=b%"

# SECURITY WARNING: don't run with debug turned on in production!

ENV = os.environ.get('DJANGO_ENV', 'dev')
if ENV == 'dev':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = []

# Application definition
LOGIN_URL='/users/login'
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # install
    "debug_toolbar",
    "django_seed",
    "django_user_agents",
    "rest_framework",
    "drf_yasg",
    
    # apps
    "shortener"
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE' : 20
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    
    "django_user_agents.middleware.UserAgentMiddleware"
]

# INTERNAL_IPS=[
#     '127.0.0.1',
# ]

GEOIP_PATH = os.path.join(BASE_DIR, 'geolite2')

ROOT_URLCONF = "shrinkers.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "shrinkers.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "app_db",
        "USER" : "root",
        "PASSWORD" : "wjdsldb27985!",
        "HOST" : "34.64.203.205",
        "POSRT" : 3306,
        "OPTIONS": {
            "autocommit" : True,
            "charset" : "utf8mb4"
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
