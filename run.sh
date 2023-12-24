python manage.py migrate
python manage.py collectstatic --noinput
export DJANGO_SETTINGS_MODULE=mikelegal.settings
daphne -b 0.0.0.0 -p 8000 mikelegal.asgi:application