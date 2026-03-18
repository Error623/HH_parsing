from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from keyboards.menu import jobs_menu

from database.session import SessionLocal
from database.crud import get_user, create_user, subscribe_user, unsubscribe_user

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(
        "Привет! Я бот вакансий. Ищу вакансии с HeadHunter по запросам",
        reply_markup=jobs_menu()
    )



@router.callback_query(F.data == "subscribe")
async def subscribe(callback: CallbackQuery):

    async with SessionLocal() as session:

        user = await get_user(session, callback.from_user.id)

        if not user:
            await create_user(session, callback.from_user.id)

        await subscribe_user(session, callback.from_user.id)

    await callback.message.answer("✅ Вы подписались на рассылку")



@router.callback_query(F.data == "unsubscribe")
async def unsubscribe(callback: CallbackQuery):

    async with SessionLocal() as session:
        await unsubscribe_user(session, callback.from_user.id)

    await callback.message.answer("❌ Вы отписались от рассылки")



@router.callback_query(F.data == "support")
async def support(callback: CallbackQuery):
    await callback.message.answer("Поддержать бота можно здесь:\nhttps://www.donationalerts.com/r/error623326")