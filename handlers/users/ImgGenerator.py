from aiogram import types
from aiogram.types import ChatType
import requests
from urllib.request import urlopen, HTTPError, URLError
from requests.structures import CaseInsensitiveDict
from aiogram.dispatcher.filters import Command
from loader import dp, bot
import openai
from aiogram.dispatcher import FSMContext
openai.api_key = "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"
from time import process_time
import time
import asyncio
s = time.time()
import urllib.parse
from aiogram.types import InputMediaPhoto, MediaGroup
from aiogram.dispatcher.filters.builtin import Text, Regexp
from states.imgGenerate import GenereateImg

QUERY_URL = "https://api.openai.com/v1/images/generations"

api_key = "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"

# Define the prompt
prompt = ""


@dp.message_handler(chat_id=[-1001761383966], commands=['art'])
async def get_prompt(message: types.Message, state: FSMContext):
    global prompt
    arguments = message.get_args()
    prompt = arguments

  
    
    # Define the model
    model = "image-alpha-001"


    # Define the headers for the request
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {api_key}"

    # Define the data for the request
    data = """
    {
        """
    data += f'"model": "{model}",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":4,
        "size":"1024x1024",
        "response_format":"url"
    }
    """

    # Send the request
    response = requests.post(QUERY_URL, headers=headers, data=data)

    if response.status_code == 200:
        urls = response.json()['data']
        await message.reply(f'<i>@{message.from_user.username}  #{message.from_user.username}</i>\n<b>🟢Please wait. Image Generating...</b>\n\n<code>{arguments}</code>')
        media_files = []

        for url1 in urls:
            media_files.append(InputMediaPhoto(url1['url']))

        media_group = MediaGroup(medias=media_files)
        await bot.send_media_group(chat_id=message.chat.id, media=media_group)

    else:
        print('Error:', response.status_code)
        await message.reply(f'<i>@{message.from_user.username}</i>   <i>#ID{message.from_user.id}</i>\n<b>🚫 Queue full -  GENERATION FAILED</b>\n 🟢Please check your words. Please wait for a job to finish first, then resubmit this one.\n\n<code>{arguments}</code>')
        return


    # asyncio.sleep(5)


# @dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands='art')
# async def echo(message: types.Message):
#     arguments = message.get_args()
#     await message.reply(arguments)
#     await message.answer('Bot only works in group or suoergroup')


# @dp.message_handler(chat_type='private')
# async def none(message: types.Message):
#     await message.answer('Bot works Only group')