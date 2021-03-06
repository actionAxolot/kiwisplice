# -*- coding: utf-8 -*-
# Django settings for pctv project.
import os
import socket

# Set up variables used in the configuration file
if socket.gethostname() == "ignomium":
    DEBUG = False
    LOCAL_DEV = False
else:
    DEBUG = True
    LOCAL_DEV = True

TEMPLATE_DEBUG = DEBUG
DIRNAME = os.path.abspath(__file__)
PROJECT_DIRNAME = os.path.abspath(os.path.join(DIRNAME, '..', '..', '..'))

LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'

# Configuration about commission percentage
# COMMISSION_PERCENT = 0.10

ADMINS = (
    ('Mario R. Vallejo', 'mario.r.vallejo@gmail.com'),
)

MANAGERS = ADMINS

if LOCAL_DEV:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'kiwisplice',                      # Or path to database file if using sqlite3.
            'USER': 'root',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'kiwisplice',                      # Or path to database file if using sqlite3.
            'USER': 'kiwisplice',                      # Not used with sqlite3.
            'PASSWORD': 'mediaGartorifa21',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Mexico_City'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


INTERNAL_IPS = ('127.0.0.1',)


# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-mx'

ugettext = lambda s: s
LANGUAGES = (
    ('es-mx', ugettext('Spanish')),
    ('en-us', ugettext('English')),
)

# LOCALE_PATHS = (
#     os.path.join(PROJECT_DIRNAME, "pctv", "locale"),
# )

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
if LOCAL_DEV:
    MEDIA_ROOT = os.path.join(PROJECT_DIRNAME, 'assets', 'media')
else:
    MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_DIRNAME, "..", "media", "media"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
if LOCAL_DEV:
    MEDIA_URL = '/media/'
else:
    MEDIA_URL = '/static/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
if LOCAL_DEV:
    STATIC_ROOT = os.path.join(PROJECT_DIRNAME, 'static')
else:
    STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_DIRNAME, "..", "media",
                                               "static"))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIRNAME, 'assets', 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'o9f+$p545yk&amp;po9$8g6(2_s7_o(%+v*+sl^(020m*3ni9c@$oe'

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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pctv.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pctv.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIRNAME, 'templates'),
)


# TEMPLATE_CONTEXT_PROCESSORS = (
#     # default template context processors
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.media',
#     # required by django-admin-tools
#     'django.core.context_processors.request',
# )


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Uncomment the next line to enable the admin:
    # 'grappelli.dashboard',
    # 'grappelli',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django_extensions',
    'apps.home',
    'apps.inventory',  # translated
    'apps.prospection',  # translated
    'apps.client',  # translated
    'apps.comment',  # translated
    'apps.commission',
    'apps.payment',  # translated
    'apps.finance',
    'apps.document',
    'apps.utils',
    'rosetta',
    'south',
    'debug_toolbar',
    'gunicorn',
    'apps.account',
)


# Django debug toolbar config
DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}


# GRAPPELLI CONFIGS
# GRAPPELLI_ADMIN_TITLE = u"PCTV"
# GRAPPELLI_INDEX_DASHBOARD = 'pctv.dashboard.CustomIndexDashboard'

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
