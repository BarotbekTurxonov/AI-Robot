from aiogram.dispatcher.filters.state import State, StatesGroup


class GenereateImg(StatesGroup):
    text = State()