try:
    from django.conf import settings  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover
    settings = None

DEBUG = True
ALLOWED_HOSTS = ['*']

if settings is not None and 'core' not in settings.INSTALLED_APPS:
    settings.INSTALLED_APPS.append('core')

if settings is not None:
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'simple_lms',
        'USER': 'simple_user',
        'PASSWORD': 'simple_password',
        'HOST': 'simpledb',
        'PORT': '5432',
    }
