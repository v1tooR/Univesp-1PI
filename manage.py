import os
import django
from django.conf import settings
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

# Popula os apps manualmente
from django.apps import apps
apps.populate(settings.INSTALLED_APPS)  # Linha crítica

if __name__ == '__main__':
    execute_from_command_line()