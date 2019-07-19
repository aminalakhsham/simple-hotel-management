import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'index.settings')

app = Celery('index')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'print_sum_of_two_numbers': {
        'task': 'add_two_numbers',
        'schedule': 5.0,
        'args': (16, 16)
    },
}
