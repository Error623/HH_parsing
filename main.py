import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import start_router, jobs_router 


logging.basicConfig(level=logging.INFO)

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


async def main():
    dp.include_router(start_router)
    dp.include_router(jobs_router)

    await bot.delete_webhook(drop_pending_updates=True)

    logging.info("Bot started successfully!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())