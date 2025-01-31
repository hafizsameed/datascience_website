from __future__ import absolute_import
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dango_project.settings')

from django.conf import settings  # noqa

app = Celery('dango_project',broker='amqp://localhost//')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# argv = [
#     'worker',
#     '-l=DEBUG',
#     '-P',
#     'eventlet',
#     '-c=100',
#     '--without-gossip',
#     '--without-mingle',
#     '--without-heartbeat',
#     '-Ofair',
# ]
# app.worker_main(argv)