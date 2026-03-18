from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def jobs_menu():
    keyboard = [
        [InlineKeyboardButton(text="🔍 Вакансии", callback_data="vacancies")],
        [InlineKeyboardButton(text="📩 Подписаться на рассылку", callback_data="subscribe")],
        [InlineKeyboardButton(text="❌ Отписаться от рассылки", callback_data="unsubscribe")],
        [InlineKeyboardButton(text="💰Поддержать бота", callback_data="support", url="https://www.donationalerts.com/r/error623326")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)



