import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db
from data.aylar import aylar

@dp.message_handler(text="📄Kiritilgen adamlar", state='*')
async def list_birthday(msg: types.Message, state: FSMContext):
    id = msg.from_user.id

    birthdays = db.select_user_birthday(id)
    # await msg.answer(birthdays)

    if birthdays == []:
        await msg.answer("Siz ele tuwılǵan kún kiritpedińiz🙃")
    bth = []
    for i, birthday in enumerate(birthdays):
        answer = f"<b>{i+1}. {birthday[0]}</b> – {birthday[1]}-{aylar[birthday[2]]} {birthday[3]}-jıl"
        bth.append(answer)
    await msg.answer('\n'.join(bth))

    await state.finish()