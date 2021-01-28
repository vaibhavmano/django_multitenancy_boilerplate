FROM python:3.8-slim

RUN apt-get update && apt-get install -y gcc python3-dev

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
RUN mkdir /app/tmp

COPY migrate_and_run.sh /app/migrate_and_run.sh
COPY gunicorn.conf.py /app/gunicorn.conf.py
COPY manage.py /app/manage.py
COPY django_boilerplate /app/django_boilerplate
COPY multi_tenancy /app/multi_tenancy
# COPY additionally created apps


WORKDIR /app

CMD ["sh", "migrate_and_run.sh"]
