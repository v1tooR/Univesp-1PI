import os
from pathlib import Path

# Diretórios base
BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_PRODUTOS_DIR = os.path.join(MEDIA_DIR, 'produtos')

# Certifique-se de que os diretórios existam
os.makedirs(MEDIA_PRODUTOS_DIR, exist_ok=True)

# Configurações para Django
DJANGO_SECRET_KEY = 'django-insecure-praado123456789store-key'
DJANGO_DEBUG = True

# Configurações para Flask
FLASK_SECRET_KEY = 'praado-store-flask-key'
FLASK_DEBUG = True