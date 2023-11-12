python manage.py migrate
python python manage.py collectstatic --noinput
python -m gunicorn -w 4 config.wsgi:application --bind 0.0.0.0:8000