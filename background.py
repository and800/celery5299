from celery import Celery
import logging


celery = Celery()
celery.config_from_object('celeryconfig')


@celery.task
def run_job(x):
    logging.warning(f'Task received; x={x}')
    for a in range(10**8):
        b = a % x
    logging.warning('Task completed')
