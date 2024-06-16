#!/usr/bin/bash

echo "Change to working directory $(pwd)"

# Run database migrations
python manage.py migrate

# if [ ${DJANGO_ENV} = 'development' ]; then
#     # Create superuser if not exists
#     export DJANGO_SUPERUSER_USERNAME="admin"
#     export DJANGO_SUPERUSER_PASSWORD="admin"
#     export DJANGO_SUPERUSER_EMAIL="admin@admin.com"
#     python manage.py createsuperuser --noinput || echo "Superuser already exists."
#     done
# fi

# Start API server
python manage.py runserver 0.0.0.0:${DJANGO_PORT}
