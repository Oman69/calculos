from celery import Celery

app = Celery(
    'celery',
    broker='amqp://guest:guest@localhost:5672//',
    backend='rpc://',
    include=['proj.tasks']
)

# Настройки Celery
app.conf.update(
    timezone='Europe/Moscow',
    enable_utc=True,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
)