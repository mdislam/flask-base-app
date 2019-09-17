# VERSION 1.0
# MAINTAINER mesba mesbahul.islam@dreambroker.com

FROM python:2.7-slim

WORKDIR /webapp

COPY . /webapp

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:5000","run:app","--reload", "--log-level", "DEBUG"]