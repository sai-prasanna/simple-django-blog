from .base import *

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
