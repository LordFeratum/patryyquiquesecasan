FROM python:2.7.12

ENV PYTHONUNBUFFERED 1

EXPOSE 9000
WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn"]
CMD ["-c", "gunicorn_settings.py", "quiqueypatrysecasan.wsgi"]

COPY . /code/

RUN python manage.py collectstatic -c --no-input
#RUN python manage.py migrate
