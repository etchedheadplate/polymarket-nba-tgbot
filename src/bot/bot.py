from aiogram import Bot, Dispatcher

from src.bot.schedule import schedule_router
from src.bot.start import start_router


async def create_bot(token: str):
    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_router(schedule_router)
    dp.include_router(start_router)

    return bot, dp
