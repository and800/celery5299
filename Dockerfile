# dependencies copypasted from pypi/warehouse, see https://github.com/celery/celery/issues/5299#issuecomment-619030695
FROM python:3.8.2-slim-buster
RUN apt-get update && apt-get install --no-install-recommends -y \
        build-essential libffi-dev libxml2-dev libxslt-dev libpq-dev libcurl4-openssl-dev libssl-dev
COPY requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /host
CMD exec celery worker -A background -Q ${QUEUE} --concurrency 1 --loglevel=info
