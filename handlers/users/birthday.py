import logging
import sqlite3
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state, Text
from data.aylar import aylar
from loader import dp, db, bot
from states.birthdayData import BirthdayData
from keyboards.inline.check_birthday import checkBirthday
from keyboards.inline.months_key import keyMonths
from aiogram.types import Message, CallbackQuery
from data.config import ADMINS
from keyboards.inline.callback_data import add_callback, edit_callback


@dp.message_handler(text="✏️Tuwılǵan kún kiritiw", state='*')
async def start_birthday(msg: types.Message):
    text = f"<b>Tuwılǵan kún iyesiniń atın kiritiń</b>\n" \
           f"Mısalı: <b>Bazarbay</b>"
    await msg.answer(text)
    await BirthdayData.fullname.set()


@dp.message_handler(state=BirthdayData.fullname)
async def answer_fullname(msg: types.Message, state: FSMContext):
    fullname = msg.text
    await state.update_data(
        {"name": fullname}
    )

    text = f"<b>Tuwılǵan jılın 4 xanalı tártipte kiritiń</b>\n" \
           f"Mısalı: <b>1994</b>"
    await msg.answer(text)
    await BirthdayData.next()


@dp.message_handler(state=BirthdayData.year)
async def answer_year(msg: types.Message, state: FSMContext):
    year = msg.text
    await state.update_data(
        {"year": year}
    )

    text = f"<b>Tuwılǵan ayın kiritiń</b>\n" \
        # f"<b>Mısalı:</b> Iyul"

    await msg.answer(text, reply_markup=keyMonths)
    await BirthdayData.next()


@dp.callback_query_handler(state=BirthdayData.month)
async def callback_gen(call: CallbackQuery, state: FSMContext):
    month = call.data
    await state.update_data(
        {"month": month}
    )

    text = f"<b>Tuwılǵan kúnin kiritiń</b>\n" \
           f"Mısalı: <b>7</b>"

    await call.message.answer(text)
    await BirthdayData.next()


@dp.message_handler(state=BirthdayData.day)
async def answer_day(msg: types.Message, state: FSMContext):
    day = msg.text
    await state.update_data(
        {"day": day}
    )

    data = await state.get_data()
    name = data.get('name')
    year = int(data.get('year'))
    month = int(data.get('month'))
    day = int(data.get('day'))


    answer = f"Maǵlıwmatlar durıs kiritildime:\n"
    answer += f"👼Atı - {name}\n"
    answer += f"🗓Tuwılǵan jılı - {year}-jıl\n"
    answer += f"🎂Tuwılǵan kúni - {day}-{aylar[month]}"

    await msg.answer(answer, reply_markup=checkBirthday)


@dp.callback_query_handler(text_contains="add", state=BirthdayData.day)
async def add_birthday(call: CallbackQuery, state: FSMContext):
    # callback_data = call.data
    # logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer("🥳Tuwılǵan kún bazaǵa kiritildi!")
    await call.answer(cache_time=60)

    data = await state.get_data()
    name = data.get('name')
    year = data.get('year')
    month = data.get('month')
    day = data.get('day')

    # date_birthday = f"{day}-{month} {year}"
    # print(date_birthday)
    id = call.from_user.id
    # print(id)

    try:
        db.add_birthday(name_f=name, day_b=day, month_b=month, year_b=year, id=id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await state.finish()

@dp.callback_query_handler(text_contains="edit", state=BirthdayData)
async def edit_birthday(call: CallbackQuery):
    # callback_data = call.data
    # logging.info(f"{callback_data=}")x
    text = f"<b>Tuwılǵan kún iyesiniń tolıq atın kiritiń</b>\n" \
           f"<b>Mısalı:</b> Bazarbay"
    await call.message.answer(text)
    await call.message.delete()
    await BirthdayData.fullname.set()