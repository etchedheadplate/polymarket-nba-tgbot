from aiogram import Bot, Dispatcher

from src.bot.schedule import schedule_router
from src.bot.start import start_router
from src.config import settings

TOKEN = settings.TG_BOT_TOKEN


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(schedule_router)
    dp.include_router(start_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
