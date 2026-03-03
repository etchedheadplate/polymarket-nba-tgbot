from collections.abc import Sequence

import aiofiles
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, Message

from src.bot.reports.keyboards import get_reports_keyboard
from src.bot.reports.text import ReportName
from src.queue import RabbitMQConnection
from src.tasks import Registry, ReportWorker

router = Router()


@router.message(Command("reports"))
async def reports_command_handler(message: Message):
    await message.answer("Select report:", reply_markup=get_reports_keyboard())


@router.callback_query(F.data.in_([name.value for name in ReportName]))
async def handle_click(callback: CallbackQuery, connection: RabbitMQConnection, registry: Registry):
    if callback.message is None:
        return

    report_name = ReportName(callback.data)
    worker = ReportWorker(connection=connection, registry=registry)
    dummy_query = {"team": "Celtics", "team_vs": "Knicks", "limit": "4"}
    payload = await worker.run(name=report_name, query=dummy_query)

    async with aiofiles.open(payload["summary"]) as f:
        summary_text = await f.read()

    media = [FSInputFile(path) for path in payload["visuals"]]
    media_group: Sequence[InputMediaPhoto] = [InputMediaPhoto(media=photo) for photo in media]
    media_group[0] = InputMediaPhoto(media=media[0], caption=summary_text)

    await callback.message.answer_media_group(media=media_group)  # pyright: ignore[reportArgumentType]
