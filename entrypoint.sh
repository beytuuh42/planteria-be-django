#!/bin/ash



echo "Apply database migrations"
python manage.py migrate


echo "Creating superuser"
python manage.py createsuperuser --noinput --username ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL}

exec "$@"