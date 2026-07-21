from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards1 import menu


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Выбери действие:",
        reply_markup=menu
    )