import os
from celery.schedules import crontab
from .celery_app import app


def delete_files_in_folder(folder):
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    folder_path = os.path.join(parent_dir, folder)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                print(file_path)
                os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении файла {file_path}. {e}')


@app.task
def send_daily_report():
    print("[DAILY REPORT] Отправка ежедневного отчета")
    return "Отчет отправлен"


@app.task
def clear_folders():
    delete_files_in_folder("uploads")
    delete_files_in_folder("output")
    return {"message": "Task completed"}


# Schedule configuration
app.conf.beat_schedule = {
    'send-report-every-day': {
        'task': 'tasks.send_daily_report',
        'schedule': crontab(hour=9, minute=30),  # Каждый день в 9:30
    },

    'run-every-60-minutes': {
        'task': 'tasks.clear_folders',
        # 'schedule': timedelta(seconds=60),
        'schedule': crontab(minute='*/60'),  # every 60 minutes
    },
}