from django.conf import settings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'app.apps.AppConfig',  # Nome do app (pasta "app")
    ],
    MEDIA_ROOT=os.path.join(BASE_DIR, 'media'),
    MEDIA_URL='/media/',
)