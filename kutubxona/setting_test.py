from .settings import *


SECRET_KEY = '(ex%$t037)pyxzt$2^v=q#dtqln*cyvff^w96h8b!@gv)yx_*%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ENV = 'testing'


ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'test'),
        'USER': 'admin',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# # Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tempkitob@gmail.com'
EMAIL_HOST_PASSWORD = 'hvqrgczmsjphfjvw'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False



# localhostda https ni ishlatish uchun
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True



print("Local settings loaded - this is a test")