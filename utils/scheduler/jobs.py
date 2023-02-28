import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from loader import bot

scheduler = AsyncIOScheduler()

async def send_scheduled_notification():
    pass


    
def schedule_jobs():
    scheduler.add_job(send_scheduled_notification, trigger='cron', hour='10', timezone=pytz.timezone('Europe/Moscow'))