from os import environ as env
from os.path import abspath, basename, dirname, join, normpath
from sys import path
import dj_database_url


DJANGO_ROOT = dirname(abspath(__file__))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)

path.append(DJANGO_ROOT)

DEBUG = True if env.get('DEBUG', False) == 'True' else False
TEMPLATE_DEBUG = DEBUG

# heroku suggested setting
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


ADMINS = [(admin.split('@')[0], admin) for admin in env.get('ADMINS', 'tyler@starkravingsane.org').split(',')]
MANAGERS = ADMINS

# dj_database_url will pull from the DATABASE_URL environment variable
DATABASES = {
        'default': dj_database_url.config(default='postgres://localhost:5432/tyler'),
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = env.get('SITE_ID', 1)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


EMAIL_BACKEND = env.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')

######################## Third party app configurations ##
DEFAULT_FROM_EMAIL = env.get('DEFAULT_FROM_EMAIL', 'devtyler@codersquid.com')
ENVELOPE_CONTACT_CHOICES = (
    ('',    u"Choose"),
    (10,    u"A general question regarding the website"),
    (20,    u"Something else"),
    (None,   u"Other"),
)
HONEYPOT_FIELD_NAME = 'relatedtopics2'

MAILGUN_ACCESS_KEY = env.get('MAILGUN_ACCESS_KEY')
MAILGUN_SERVER_NAME = env.get('MAILGUN_SERVER_NAME')

#AWS_STORAGE_BUCKET_NAME = 'org.starkravingsane.testing'
#AWS_ACCESS_KEY_ID = env.get('AWS_ACCESS_KEY_ID')
#AWS_SECRETE_ACCESS_KEY= env.get('AWS_SECRETE_ACCESS_KEY')
#AWS_HEADERS = {}
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# REST_FRAMEWORK = { }

ACCOUNT_ACTIVATION_DAYS = 2
##################################


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'
 

# Additional locations of static files
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = env.get('SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'companionpages.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'companionpages.wsgi.application'

TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'envelope',
    'gunicorn',
    'honeypot',
    'profiles',
    'registration',
    #'rest_framework',
    'south',
    #'storages',
)

# Apps specific for this project go here.
LOCAL_APPS = (
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

if DEBUG:
    # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
    INSTALLED_APPS += (
        'debug_toolbar',
        'django.contrib.webdesign',
        'django.contrib.admin',
        'django.contrib.admindocs',
        'django_extensions',
    )
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

