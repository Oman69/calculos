import os

from celery.schedules import crontab

from api import UPLOAD_DIR, OUTPUT_DIR
from celery_app import celery_app
from datetime import timedelta


async def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении файла {file_path}. {e}')


@celery_app.task
async def clear_folders():
    await delete_files_in_folder(UPLOAD_DIR)
    await delete_files_in_folder(OUTPUT_DIR)
    return "Task completed"


# Schedule configuration
celery_app.conf.beat_schedule = {
    'send-report-every-day': {
        'task': 'app.tasks.send_daily_report',
        'schedule': crontab(hour=9, minute=30),  # Каждый день в 9:30
    },

    'run-every-60-seconds': {
        'task': 'app.tasks.clear_folders',
        'schedule': timedelta(seconds=60),
        # 'schedule': crontab(minute='*/15'),  # every 15 minutes
    },
}