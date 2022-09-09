from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):

    text = f"👨‍💻Developer: <a href='https://t.me/begys'>Begis Orınbaev</a>"

    await message.answer(text)