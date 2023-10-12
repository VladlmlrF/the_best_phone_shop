import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_best_phone_shop.settings')

app = Celery('the_best_phone_shop')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()
