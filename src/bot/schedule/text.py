from enum import StrEnum


class ScheduleRange(StrEnum):
    TODAY = "today"
    WEEK = "week"
    ALL = "all"


class ScheduleText:
    BUTTON_LABELS = {
        ScheduleRange.TODAY: "Today",
        ScheduleRange.WEEK: "Week",
        ScheduleRange.ALL: "ALL",
    }

    RESPONSES = {
        ScheduleRange.TODAY: "Сегодня игры:",
        ScheduleRange.WEEK: "Игры на неделю:",
        ScheduleRange.ALL: "Все игры:",
    }
