from aiogram.dispatcher.filters.state import State, StatesGroup


class PostState(StatesGroup):
    photo = State()
    text = State()