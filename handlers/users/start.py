import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menuStart
from loader import dp, db, bot
from data.config import ADMINS
from datetime import datetime
from data.aylar import aylar
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.users.user_birthday import check_db


scheduler = AsyncIOScheduler()

@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    id = message.from_user.id
    name = message.from_user.full_name

    try:
        db.add_user(id=id, name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
    count = db.count_users()[0]

    await message.answer(f"Salem, <b>{name}</b>", reply_markup=menuStart)

    msg = f"{message.from_user.full_name} bazaǵa qosıldı.\nBazada {count} paydalanıwshı bar"
    await bot.send_message(chat_id=ADMINS[0], text=msg)
    await state.finish()

@dp.message_handler(text='/date')
async def get_date(message: types.Message):
    now = datetime.now()
    msg =f"📅Búgin: <b>{now.day}-{aylar[now.month]} {now.year}-jıl</b>\n"
    msg += f"🕐Saat: <b>{now.hour}-{now.minute}</b>"
    await message.answer(msg)