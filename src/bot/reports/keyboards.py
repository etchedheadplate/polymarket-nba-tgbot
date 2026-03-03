from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.bot.reports.text import ReportName, ReportText


def get_reports_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=ReportText.BUTTON_LABELS[range_enum], callback_data=range_enum.value)
        for range_enum in ReportName
    ]
    return InlineKeyboardMarkup(inline_keyboard=[buttons])


reports_keyboard = get_reports_keyboard()
