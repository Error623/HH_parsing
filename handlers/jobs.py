from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from database.crud import get_user, create_user
from database.session import SessionLocal
from services.hh_api import get_vacancies, format_vacancies

router = Router()


@router.message(Command("jobs"))
async def jobs_cmd(message: Message):
    await message.answer("Введите запрос для поиска вакансий")


# поиск вакансий
@router.message(F.text & ~F.text.startswith("/"))
async def search_jobs(message: Message):

    query = message.text

    vacancies = await get_vacancies(query)

    if not vacancies:
        await message.answer("К сожалению, вакансий не найдено.")
        return

    text = format_vacancies(vacancies)

    await message.answer(text)


# установка запроса (отдельная команда)
@router.message(Command("setquery"))
async def set_query(message: Message):

    query = message.text.replace("/setquery ", "")

    async with SessionLocal() as session:
        user = await get_user(session, message.from_user.id)

        if not user:
            user = await create_user(session, message.from_user.id)

        user.query = query
        await session.commit()

    await message.answer(f"✅ Запрос сохранён: {query}")