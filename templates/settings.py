# -*- coding: utf-8 -*-
import os
from django.utils.translation import ugettext_lazy as _

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('{{admin.name}}', '{{admin.email}}'),
)

MANAGERS = ADMINS

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': '{{agora.user}}',
         'USER': '{{agora.user}}',
         'PASSWORD': '',
         'HOST': '',
         'PORT': '',
     }
}

AGORA_FNMT_BASE_URL = 'https://fnmt.{{hostname}}'
AGORA_BASE_URL = 'https://{{hostname}}'

ALLOWED_HOSTS = [
    '.{{hostname}}',
]

AUTHENTICATION_BACKENDS = (
    #'agora_site.agora_core.backends.idcat.idCATBackend',
    #'agora_site.agora_core.backends.fnmt.FNMTBackend',
    'userena.backends.UserenaAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

AGORA_CREATION_PERMISSIONS = 'superusers-only'
AGORA_USE_HTTPS = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

ANONYMIZE_USERS = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

CELERY_ALWAYS_EAGER = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_DOMAIN = '.{{hostname}}'

from django.core.exceptions import SuspiciousOperation

def skip_suspicious_operations(record):
    if record.exc_info:
        exc_value = record.exc_info[1]
        if isinstance(exc_value, SuspiciousOperation):
            return False
    return True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'skip_suspicious_operations': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_suspicious_operations,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

{% if not agora.api_mode %}
SITE_NAME = '{{agora.name}}'

{% if agora.auto_join %}
AGORA_REGISTER_AUTO_JOIN = [ {{agora.auto_join}} ]
{% endif %}
{% endif %}

{% if agora.email %}
EMAIL_BACKEND = '{{agora.email.backend}}'
EMAIL_HOST = '{{agora.email.host}}'
EMAIL_HOST_PASSWORD = '{{agora.email.password}}'
EMAIL_HOST_USER = '{{agora.email.user}}'
SERVER_EMAIL = DEFAULT_FROM_EMAIL = '{{agora.email.from|default(agora.email.user)}}'
EMAIL_PORT = '{{agora.email.port}}'
{% endif %}

AGORA_ALLOW_API_AUTO_ACTIVATION = True


