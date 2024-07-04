import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal.settings')
 
app = Celery('newsportal')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.conf.timezone = 'UTC'

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'news.tasks.weekly_send_emails',

        'schedule': crontab(hour=8, minute=00, day_of_week='monday'),

        'args': (),
    },
}