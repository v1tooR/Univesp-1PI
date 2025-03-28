from flask import Flask
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Configura o Django
settings.configured or settings.configure()

app = Flask(__name__)
app.wsgi_app = get_wsgi_application()  # Integra Django ao Flask

# Cria a pasta media se não existir
import os
if not os.path.exists(settings.MEDIA_ROOT):
    os.makedirs(settings.MEDIA_ROOT)