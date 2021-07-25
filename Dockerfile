FROM python:3.9.6-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

#ADD ./app

#RUN pip install -r requirements.txt

ADD ./requirements.txt /app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
ADD . /app

#RUN pip install django
