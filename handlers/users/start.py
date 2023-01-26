from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from utils.db_api.db_test import send_ex
import sqlite3

# #Define the connection

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
	user_id = message.from_user.id
	user_name = message.from_user.full_name
	username = message.from_user.username

	await message.answer("💡 The bot available only in this group:\n https://t.me/DeepNetworkUz", disable_web_page_preview=True)

	try:
		test = send_ex("CREATE TABLE IF NOT EXISTS users_art(user_id INTEGER PRIMARY KEY, username TEXT)")

		user = send_ex(f"""INSERT INTO users_art (user_id, username) 
				VALUES ({user_id},'{username}')""")
		
		
		print(f"|INFO| - {message.from_user.full_name.upper()} ADDED TO DATABASE")
		# await message.answer(f"Hello, {message.from_user.full_name}!")
	except Exception as ex:
		await message.answer(f'Assalom alaykum {message.from_user.full_name}\nSizni yana ko\'rib turganimdan xursandman!')
		# await message.answer()
	# 