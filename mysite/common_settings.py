import os
import os.path
MAIN_APP_PATH = os.path.realpath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(MAIN_APP_PATH, os.pardir))
COLLECT_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))

print "MAIN_APP_PATH", MAIN_APP_PATH
print "PROJECT_ROOT", PROJECT_ROOT
print "COLLECT_ROOT", COLLECT_ROOT


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django.db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

MEDIA_ROOT = COLLECT_ROOT + '/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = COLLECT_ROOT +"/static"
STATIC_URL = '/static/'
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT+"/static",
)




TEMPLATE_DIRS = (
    PROJECT_ROOT + '/templates/',
)


LOGIN_URL = '/my_restaurant'
LOGIN_REDIRECT_URL = '/my_restaurant'

ALLOWED_SIGNUP_DOMAINS = ['*']

#set email info
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'wangeen1985@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = '5tgbHU*ik,'
DEFAULT_FROM_EMAIL  = SERVER_EMAIL = 'wangeen1985@gmail.com'
EMAIL_PORT = 587

#EMAIL_USE_TLS = True
#EMAIL_HOST = 'stmp.exmail.qq.com'
#EMAIL_PORT = 465
#EMAIL_HOST_USER = 'support@wangeen.com'
#EMAIL_HOST_PASSWORD = '5rdxSW@'
#DEFAULT_FROM_EMAIL  = SERVER_EMAIL = 'support@wangeen.com'
## The next line is not required,  but may be useful.
#SEND_BROKEN_LINK_EMAILS = True


