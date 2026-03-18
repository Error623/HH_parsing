from celery_app import celery
from database.session import SessionLocal
from database.crud import get_subscribed_users
from services.hh_api import get_vacancies, format_vacancies

from aiogram import Bot
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))


async def send_jobs_async():

    async with SessionLocal() as session:
        users = await get_subscribed_users(session)

    # группируем пользователей по запросам
    queries = {}

    for user in users:
        queries.setdefault(user.query, []).append(user.telegram_id)

    # делаем запросы к API
    for query, user_ids in queries.items():
        jobs = await get_vacancies(query)
        text = format_vacancies(jobs)

        for user_id in user_ids:
            try:
                await bot.send_message(user_id, text)
            except Exception as e:
                print(f"Ошибка отправки {user_id}: {e}")


@celery.task
def send_daily_jobs():
    asyncio.run(send_jobs_async())