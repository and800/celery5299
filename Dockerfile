FROM python:3.8.2-slim-buster
RUN apt-get update && apt-get install --no-install-recommends -y \
        build-essential libcurl4-openssl-dev libssl-dev htop strace
COPY requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /host
#CMD exec celery worker -A background -Q ${QUEUE} --concurrency 1 --loglevel=info
CMD exec python debugentry.py
