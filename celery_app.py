from celery import Celery 
from celery.schedules import crontab
from dotenv import load_dotenv
import os

load_dotenv()

celery = Celery (
    "tasks",
    broker=os.getenv("REDIS_URL"),
    backend=os.getenv("REDIS_URL")
)



celery.conf.beat_schedule = {
    "send-daily-jobs": {
        "task": "tasks.send_daily_jobs",
        "schedule": crontab(hour=10, minute=0) # каждый день в 10 утра
    }
}