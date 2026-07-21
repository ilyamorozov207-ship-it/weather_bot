import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.client.session.aiohttp import AiohttpSession

from config1 import TOKEN
from start1 import router as start_router
from profile import router as profile_router
from weather import router as weather_router
from weather2 import router as weather_router_v2

session = AiohttpSession(
    proxy="socks5://127.0.0.1:10808"
)

bot = Bot(
    token=TOKEN,
    session=session
)

dp = Dispatcher()


dp.include_router(start_router)
dp.include_router(profile_router)
dp.include_router(weather_router)
dp.include_router(weather_router_v2)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())