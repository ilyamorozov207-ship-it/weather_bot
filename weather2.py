from aiogram import Router
from aiogram.types import Message
from keyboards1 import menu
from speed_wind import get_wind_speed
from weather_api import get_coordinates, get_weather
from weather_description import get_weather_description

router = Router()

@router.message()
async def echo(message: Message):
    if message.text == "назад":
        await message.answer("Выбирите действие", reply_markup=menu
                             )
    elif  len(message.text) < 2:
        await message.answer("Не знаю такого города, попробуйте еще раз")
        await message.answer("Выбирите действие", reply_markup=menu
                             )

    else:
        city = message.text
        parts = city.split()
        name_city = " ".join(parts[0:])

        coordinates = get_coordinates(name_city)
        if coordinates is None:
            await message.answer("Город не найден. Попробуйте еще раз.")
            return

        latitude, longitude = coordinates
        weather_data = get_weather(latitude, longitude)

        await message.answer(
                            f"Погода в {name_city}:"
                            f"\nТемпература: {weather_data['temperature']}°C"
                            f"\nСкорость ветра: {weather_data['wind']} м/с"
                            f"\nОщущается как: {weather_data['apparent']}°C"
                            f"\nВлажность: {weather_data['humidity']}%"
                            f"\nОблачность: {weather_data['cloud_cover']}%"
                            f"\nОсадки: {weather_data['precipitation']} мм"
                            f"\nНаправление ветра: {get_wind_speed(weather_data['wind_direction'])}"
                            f"\nПогода: {get_weather_description(weather_data['weather_code'])}"
                            )