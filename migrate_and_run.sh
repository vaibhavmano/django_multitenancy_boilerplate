# python3 manage.py run_huey &
python3 manage.py migrate
python3 manage.py collectstatic --no-input --clear
# python3 manage.py runserver 0:8000
gunicorn django_boilerplate.wsgi --log-level=DEBUG -c gunicorn.conf.py