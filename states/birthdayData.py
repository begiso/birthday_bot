from aiogram.dispatcher.filters.state import StatesGroup, State

class BirthdayData(StatesGroup):
    fullname = State()
    year = State()
    month = State()
    day = State()