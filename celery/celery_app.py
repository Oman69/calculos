from celery import Celery
from celery_config import settings

celery_app = Celery(
    'worker',
    broker=settings.RABBITMQ_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=['app.tasks']
)

# Настройки Celery
celery_app.conf.update(
    timezone='Europe/Moscow',
    enable_utc=True,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
)