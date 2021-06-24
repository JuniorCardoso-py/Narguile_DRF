FROM python:latest


COPY . /var/www
WORKDIR /var/www


RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

ENTRYPOINT python manage.py migrate && python manage.py runserver 0:8000