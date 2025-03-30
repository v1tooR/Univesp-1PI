#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line
from config import BASE_DIR, TEMPLATE_DIR, MEDIA_DIR, DJANGO_SECRET_KEY, DJANGO_DEBUG

def main():
    # Configurações do Django
    if not settings.configured:
        settings.configure(
            BASE_DIR=BASE_DIR,
            SECRET_KEY=DJANGO_SECRET_KEY,
            DEBUG=DJANGO_DEBUG,
            ALLOWED_HOSTS=['localhost', '127.0.0.1'],
            INSTALLED_APPS=[
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'app',
            ],
            MIDDLEWARE=[
                'django.middleware.security.SecurityMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ],
            ROOT_URLCONF=[],  # Não usamos URLs do Django, apenas Flask
            TEMPLATES=[
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [TEMPLATE_DIR],
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
            ],
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            },
            MEDIA_URL='/media/',
            MEDIA_ROOT=MEDIA_DIR,
            STATIC_URL='/static/',
            LANGUAGE_CODE='pt-br',
            TIME_ZONE='America/Sao_Paulo',
            USE_I18N=True,
            USE_TZ=True,
            DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
        )
        django.setup()

    # Executar comandos do Django
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()