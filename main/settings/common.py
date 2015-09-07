import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

ROOT_URLCONF = 'main.urls'
WSGI_APPLICATION = 'main.wsgi.application'

LANGUAGE_CODE = 'es-PE'
USE_I18N = True
USE_L10N = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"),],
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
