import asyncio
from aiogram.dispatcher import FSMContext

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    # print(users[0][0])
    await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="Test qılıp kórvatpan..")
        await asyncio.sleep(0.05)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tazalandı!")

@dp.message_handler(text="/all_birthdays", user_id=ADMINS)
async def get_all_birthdays(message: types.Message):

    birthdays = db.select_all_birthdays()
    await message.answer(birthdays)