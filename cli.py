#!/usr/bin/env python
from celery import Celery, signature
import logging
import sys


if __name__ == '__main__':
    celery = Celery()
    celery.config_from_object('celeryconfig')

    task = signature('background.run_job')
    arg = int(sys.argv[1])
    logging.warning(f'Sending task; x={arg}')
    task.apply_async([arg])
    logging.warning('Task sent!')
