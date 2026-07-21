from aiogram import Router
from aiogram.types import Message
from keyboards1 import menu

router = Router()

@router.message()
async def echo(message: Message):
    if message.text == "назад":
        await message.answer("Выбирите действие", reply_markup=menu
                             )
    else:
        await message.answer(f"Погода в {message.text.strip()} составляет 25°C. Влажность: 60%. Ветер: 5 м/с.")