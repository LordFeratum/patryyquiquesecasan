FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/opt/
WORKDIR /opt
ADD requirements.txt /opt/
RUN pip install -r /opt/requirements.txt
ADD . /code/