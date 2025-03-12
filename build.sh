#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Create superuser if not exists
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username="user").exists():
    User.objects.create_superuser("user", "admin@example.com", "user12345")
    print("Superuser created")
else:
    print("Superuser already exists")
EOF
