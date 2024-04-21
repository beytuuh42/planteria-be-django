#!/bin/ash



echo "Generate migrations"
python manage.py makemigrations

echo "Apply changes to db"
python manage.py migrate


echo "Creating superuser"
python manage.py createsuperuser --noinput --name ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL}

exec "$@"