from aiogram import types
from loader import dp, bot
from utils.db_api.db_test import send_ex
from states.postUchun import PostState
# from aiogram.types import 


@dp.message_handler(chat_id=5235865310, commands='users')
async def users(msg: types.Message):
	users = send_ex("SELECT user_id FROM users_art")
	await msg.answer(f"🫂 All Users : {len(users)}")






# @dp.message_handler(chat_id=5235865310, commands='post')
# async def users(msg: types.Message):
# 	await msg.answer("Post uchun rasm yuboring!")
# 	await PostState.photo.set()


# @dp.message_handler(state=PostState.photo, content_type='photo')
# async def 
# 	users = send_ex("SELECT user_id FROM users_art")

# 	for i in users :

# 		try:
# 			bot.send_message(chat_id=i[0], )
