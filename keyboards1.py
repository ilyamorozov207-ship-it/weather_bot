from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Погода", callback_data="weather")],
        [InlineKeyboardButton(text="Профиль", callback_data="profile")]
    ]
)