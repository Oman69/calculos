ПРОЕКТ НЕ РАБОТАЕТ

1. Войти в виртуальное окружение source env/bin/activate
2. Перезапустить сервер systemctl restart nginx
3. Остановить процессы sudo lsof -t -i tcp:8080 | xargs kill -9
4. Запустить проект uvicorn api:app 0.0.0.0 8080

RabbitMQ
Инструкция по установке:
https://www.cherryservers.com/blog/how-to-install-and-start-using-rabbitmq-on-ubuntu-22-04
Открыть порт 15672 для интерфейса


CELERY
Запуск Celery из папки "proj": celery -A celery_app worker --pool=solo -l info
Запуск задач Celery из папки "proj": celery -A celery_app beat -l info