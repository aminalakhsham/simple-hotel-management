import random
from django.conf import settings
from django.core.mail import send_mail
from celery.task import task


@task(name="add_two_numbers")
def add():
    return send_mail('amin', 'hi, this is from hotel project',
                     'aminking140@gmail.com', ['aminking140@gmail.com'], fail_silently=True)
