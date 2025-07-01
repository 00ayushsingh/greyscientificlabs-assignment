#!/usr/bin/env python
import os
import django
from django.conf import settings
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_api.settings')
    django.setup()
    
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin1234',
            role='admin'
        )
        print('Superuser created successfully')
    else:
        print('Superuser already exists')
