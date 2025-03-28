from django.conf import settings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Caminho absoluto
        }
    },
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'univesp-1pi',  # Nome do seu app (mesmo nome da pasta)
    ],  # Nome do módulo onde estão os modelos
    MEDIA_ROOT=os.path.join(BASE_DIR, 'media'),  # Pasta para fotos
    MEDIA_URL='/media/',
)