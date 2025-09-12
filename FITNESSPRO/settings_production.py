"""Production settings for FITNESSPRO project."""

# Import base settings
from .settings import *

# Override base settings for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Update this with your PythonAnywhere username
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# Database
# Uncomment and configure this section if you want to use MySQL on PythonAnywhere
# (available in paid accounts)

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$fitnesspro',
        'USER': 'yourusername',
        'PASSWORD': 'your-database-password',
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}
'''

# Keep the SQLite configuration as default
# SQLite is sufficient for small applications with limited traffic
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECURE_SSL_REDIRECT = False  # Set to True if you have HTTPS configured
SESSION_COOKIE_SECURE = False  # Set to True if you have HTTPS configured
CSRF_COOKIE_SECURE = False  # Set to True if you have HTTPS configured

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django_error.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}