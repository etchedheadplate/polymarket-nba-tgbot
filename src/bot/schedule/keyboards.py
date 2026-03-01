from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.bot.schedule.text import ScheduleRange, ScheduleText


def get_schedule_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=ScheduleText.BUTTON_LABELS[range_enum], callback_data=range_enum.value)
        for range_enum in ScheduleRange
    ]
    return InlineKeyboardMarkup(inline_keyboard=[buttons])


schedule_keyboard = get_schedule_keyboard()
