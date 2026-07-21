from aiogram import Router
from aiogram.types import CallbackQuery, Message

router = Router()


@router.callback_query(lambda call: call.data == "weather")
async def weather(callback: CallbackQuery):

    await callback.message.answer("Введите город, чтобы узнать погоду или назад для возвращения в меню:")