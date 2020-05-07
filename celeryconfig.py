import os as _os


broker_url = 'sqs://'
broker_transport_options = {
    'region': _os.getenv('REGION', 'us-east-1'),
}
task_acks_late = True
task_reject_on_worker_lost = True
worker_prefetch_multiplier = 1
worker_max_tasks_per_child = 1
task_routes = {
    'background.run_job': {'queue': _os.getenv('QUEUE', 'celery5299')}
}
