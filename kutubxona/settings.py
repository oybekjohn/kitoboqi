import os

import environ                     # .env file parser
from datetime import timedelta     # for JWT expiration   
# import sys                       # for sys.path.append( ... )

from pathlib import Path



env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['44.206.255.60', 'localhost', '0.0.0.0', '*']

LOGIN_URL = "users:login"            # url to redirect to if not logged in


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    # this is also need required for serving Swagger UI's css/js files

    # internal apps [local] 
    'books',
    'users',
    'api',

    # external apps [3rd-party]
    'rest_framework',
    'drf_yasg',                       # Swagger UI
    "corsheaders",                    # cors for other domains for example React (frontchi uchun)
    "crispy_forms",                   # forms bootstrap
    "crispy_bootstrap5",              # forms bootstrap

]


# bootstrap5 crispy forms uchun
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"



# Middleware sozlamalari
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",                # CORS uchun
    "django.middleware.common.CommonMiddleware",            # CORS uchun
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'kutubxona.middleware.SimpleMiddleware',                 #middleware py ni shu yerda qo'shamiz va u ishlaydi
]


# qolda yozilgan SimpleMiddleware ni ishlatish
ROOT_URLCONF = 'kutubxona.urls'


# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates", 
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            # swagger uchun
            'libraries' : {
                'staticfiles': 'django.templatetags.static', 
            }

        },
    },
]


#wsgi depolyment uchun
WSGI_APPLICATION = 'kutubxona.wsgi.application'



# Database
DATABASES = {

    # SQLite
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }


    # PostgreSQL
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'), 
        'USER': env('DB_USER'), 
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }


    # MongoDB
    # 'default': {
    #     'ENGINE': 'django.db.backends.mongodb',
    #     'NAME': env('DB_NAME'),
    #     'USER': env('DB_USER'),
    #     'PASSWORD': env('DB_PASSWORD'),
    #     'HOST': env('DB_HOST'),
    #     'PORT': '27017',
    # }


    # MySQL
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': env('DB_NAME'),
    #     'USER': env('DB_USER'),
    #     'PASSWORD': env('DB_PASSWORD'),
    #     'HOST': env('DB_HOST'),
    #     'PORT': '3306',
    # }


}



# SWAGGER_SETTINGS
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {

        'basic': {
            'type': 'basic'
        },


        # 'api_key': {
        #     'type': 'apiKey',
        #     'in': 'header',
        #     'name': 'Authorization'
        # },
        
    },

    # 'VALIDATOR_URL': 'http://localhost:8000',             #swagger uchun validator ni ishlatish
}



# Rest Framework settings
REST_FRAMEWORK = {

    # Swagger settings
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',


    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.BasicAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    # ),


    # User permissions
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),


    # JWT AUTHENTICATION settings
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ),


    # API Pagination settings
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,


    # 'DEFAULT_FILTER_BACKENDS': (
    #     'django_filters.rest_framework.DjangoFilterBackend',
    # ),


    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    #     'rest_framework.renderers.BrowsableAPIRenderer',
    # ),


    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    #     'rest_framework.parsers.FormParser',
    #     'rest_framework.parsers.MultiPartParser',
    # ),
} 



# # JWT settings
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': True,
#     'UPDATE_LAST_LOGIN': False,

#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,
#     'JWK_URL': None,
#     'LEEWAY': 0,

#     'AUTH_HEADER_TYPES': ('Bearer', 'JWT'),
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
#     # 'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',
#     # 'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

#     'JTI_CLAIM': 'jti',

#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(days=1),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }



# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    }, 
]



# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True



# User Model overwrite or Custom User Model
AUTH_USER_MODEL = "users.CustomUser"


# Static files (CSS, JavaScript, Images)
MEDIA_URL = "/media/"
MEDIA_ROOT = "media-files"     # yuklangan media fayllar saqlanadigan folder

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = 'static-files'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


# # Celery uchun sozlama
# CELERY_BROKER_URL = "something"


# Front va Backend settings
CORS_ALLOWED_ORIGINS = [
    # "https://example.com",
    # "https://sub.example.com",
    # "http://localhost:3000",            # frontendni ishlatish uchun 
]
