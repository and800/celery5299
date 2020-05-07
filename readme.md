https://github.com/celery/celery/issues/5299

This is an (almost always) reproducible example of the 100%cpu issue.

`max_tasks_per_child` is `1` - and usually only one task is enough to break the main worker process
