Запуск Celery из папки "proj": celery -A celery_app worker --pool=solo -l info
Запуск задач Celery из папки "proj": celery -A celery_app beat -l info