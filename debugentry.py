import sys
sys.argv = [
    '/usr/local/bin/celery',
    'worker',
    '-A',
    'background',
    '-Q',
    'celery5299',
    '--concurrency',
    '1',
    '--loglevel=info',
]

from celery.__main__ import main
sys.exit(main())
