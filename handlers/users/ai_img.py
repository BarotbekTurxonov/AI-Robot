import replicate
import os
from aiogram import types
import requests
from loader import dp, bot
from io import BytesIO
os.environ["REPLICATE_API_TOKEN"] = "20b978882a010f5d63f54b2151fe913316cca993"

model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1")

@dp.message_handler(commands='sd')
async def sd(msg: types.Message):
    arguments = msg.get_args()

    # https://replicate.com/stability-ai/stable-diffusion/versions/f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1#input
    inputs = {
        # Input prompt
        'prompt': arguments,
        # Specify things to not see in the output
        # 'negative_prompt': ...,
        # Width of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'width': 768,
        # Height of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'height': 768,
        # Prompt strength when using init image. 1.0 corresponds to full
        # destruction of information in init image
        'prompt_strength': 0.8,
        # Number of images to output.
        # Range: 1 to 4
        'num_outputs': 2,
        # Number of denoising steps
        # Range: 1 to 500
        'num_inference_steps': 50,

        # Scale for classifier-free guidance
        # Range: 1 to 20
        'guidance_scale': 7.5,

        # Choose a scheduler.
        'scheduler': "DPMSolverMultistep",

        # Random seed. Leave blank to randomize the seed
        # 'seed': ...,
    }

    # https://replicate.com/stability-ai/stable-diffusion/versions/f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1#output-schema
    output = version.predict(**inputs)
    for i in output:
        print(i)
    # for i, url in enumerate(output):
    #     response = requests.get(url)
    #     await bot.send_photo(chat_id=msg.from_user.id, photo=BytesIO(response.content), caption=f"Art {i+1}")
    # print(output)