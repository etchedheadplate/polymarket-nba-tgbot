from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from src.bot.schedule.keyboards import get_schedule_keyboard
from src.bot.schedule.text import ScheduleRange
from src.queue import RabbitMQConnection
from src.tasks import Registry, ScheduleWorker

router = Router()


@router.message(Command("schedule"))
async def schedule_command_handler(message: Message):
    await message.answer("Select schedule range:", reply_markup=get_schedule_keyboard())


@router.callback_query(F.data.in_([range.value for range in ScheduleRange]))
async def handle_click(callback: CallbackQuery, connection: RabbitMQConnection, registry: Registry):
    if callback.message is None:
        return

    range_selected = ScheduleRange(callback.data)
    worker = ScheduleWorker(connection=connection, registry=registry)
    payload = await worker.run(schedule=range_selected)

    text_response: list[str] = []
    for date, game in payload.items():
        game_lines: list[str] = []
        for game_id, teams in game.items():
            game_line = f" - {teams['guest']}:{teams['host']} | {game_id}"
            game_lines.append(game_line)
        date_section = f"# {date}\n{'\n'.join(game_lines)}\n\n"
        text_response.append(date_section)

    formatted_text = f"```\n{'\n'.join(text_response)}```"
    await callback.message.answer(formatted_text, parse_mode="MarkdownV2")
