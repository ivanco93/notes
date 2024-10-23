# create_superuser.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get('SUPERUSER_USERNAME', 'administrator')
email = os.environ.get('SUPERUSER_EMAIL', 'administrator@email.com')
password = os.environ.get('SUPERUSER_PASSWORD', '123456')

# Crea el superusuario si no existe
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
