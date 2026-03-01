from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from src.bot.schedule.keyboards import get_schedule_keyboard
from src.bot.schedule.text import ScheduleRange, ScheduleText
from src.workers import get_games_schedule

router = Router()


@router.message(Command("schedule"))
async def schedule_command_handler(message: Message):
    await message.answer("Выберите диапазон:", reply_markup=get_schedule_keyboard())


@router.callback_query(F.data.in_([range.value for range in ScheduleRange]))
async def handle_click(callback: CallbackQuery):
    if callback.message is None:
        return

    range_selected = ScheduleRange(callback.data)
    await get_games_schedule(range_selected)
    response_text = ScheduleText.RESPONSES[range_selected]
    await callback.message.answer(response_text)
