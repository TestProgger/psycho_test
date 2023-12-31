import os
from config.settings.env import env, BASE_DIR

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
os.environ["CORS_ALLOW_CREDENTIALS"] = "true"

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = env.list("DJANGO_CSRF_TRUSTED_ORIGINS", default=['http://127.0.0.1', ], cast=str)

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "OPTIONS"
)
CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "x-secret"
)

DJANGO_ALLOW_ASYNC_UNSAFE = True

DJANGO_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'subject.apps.SubjectConfig',
    'psycho_test.apps.PsychoTestConfig',
    'utils'
]

THIRD_PARTY_APPS = [
    "rest_framework",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'utils.middlewares.SetSubjectMiddleware',
    'utils.middlewares.DisableCSRFMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


if env.str('DATABASE_URL', None):
    DATABASES = {
        "default": env.db('DATABASE_URL'),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        },
    }

# DATABASE_ROUTERS = ['routers.db_router.DataMartRouter', 'routers.db_router.DefaultAppRouter']

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = env.str('DJANGO_LANGUAGE_CODE', 'ru-ru')

TIME_ZONE = env.str('DJANGO_TIME_ZONE', 'Europe/Moscow')

USE_I18N = True

USE_TZ = True

STATIC_URL = env.str('DJANGO_STATIC_URL', default='static/')
STATIC_ROOT = BASE_DIR / STATIC_URL

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

COOKIE_EXPIRATION_HOURS = 24
COOKIE_KEY = 'Token'
COOKIE_HEADER_KEY = 'HTTP_COOKIE'
SECRET_HEADER = 'X-Secret'
