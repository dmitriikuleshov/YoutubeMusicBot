import os
import asyncio

import validators
from aiogram import types, Dispatcher

from create_bot import dp, bot
from keyboards import kb_client
from download_audio import download_audio


# @dp.message_handler(commands=['start', "help"])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               text="Hello! I can send you audio, if you give me youtube link.",
                               reply_markup=kb_client)
        # await message.delete()
    except Exception:
        await message.reply("Общение с ботом через ЛС. Напишите ему: "
                            "https://t.me/Y_o_u_t_u_b_e_M_u_s_i_c_Bot")


async def check_for_youtube_link(message: types.Message):
    if validators.url(message.text):
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id,
                               disable_notification=True,
                               text='Trying to get audio.')

        file_name = download_audio(message.text)
        await bot.send_audio(message.from_user.id,
                             disable_notification=True,
                             audio=open(file_name, 'rb'))
        os.remove(file_name)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
    dp.register_message_handler(check_for_youtube_link)
