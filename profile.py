from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(lambda call: call.data == "profile")
async def profile(callback: CallbackQuery):
    user = callback.from_user

    await callback.message.answer(
        f"👤 Профиль\n\n"
        f"Имя: {user.first_name}\n"
        f"ID: {user.id}\n"
        f"Username: @{user.username}"
    )

    await callback.answer()