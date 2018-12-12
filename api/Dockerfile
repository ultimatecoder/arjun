FROM python:latest

# Ensure that Python outputs everything that's printed inside # the application
# rather than buffering it.
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && \
    apt-get -y upgrade

#RUN apk update && \
#    apk upgrade && \
#    apk add supervisor && \
#    apk add bash

EXPOSE 8000 8000

WORKDIR /srv/app

COPY Pipfile Pipfile

COPY Pipfile.lock Pipfile.lock

#RUN apt-get install -y pipenv

RUN pip install pipenv

RUN python -m pipenv install

COPY manage.py manage.py

COPY api api

COPY team team

COPY scripts/start.sh start.sh

RUN export PATH="/root/.local/bin:${PATH}"

ENTRYPOINT ["./start.sh"]
