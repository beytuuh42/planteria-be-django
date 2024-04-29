#!/bin/ash
echo "Generate migrations"
python manage.py makemigrations

echo "Apply changes to db"
python manage.py migrate

echo "Creating superuser"
python manage.py createsuperuser --noinput --name ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL}

echo "Load fixtures for plants"
python manage.py loaddata plants

echo "Load fixtures for plants_images"
python manage.py loaddata plants_images

echo "Load fixtures for users"
python manage.py loaddata users

exec "$@"