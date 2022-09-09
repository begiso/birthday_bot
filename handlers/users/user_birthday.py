from loader import dp, db, bot
from datetime import datetime
from aiogram import Dispatcher, types
from data.config import ADMINS

@dp.message_handler(text="/check")
async def check_db(msg: types.Message):
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    today = f"{now.month}-{now.day}"

    birthdays = db.select_all_birthdays()
    bth = []
    for birthday in birthdays:
        answer = (f"{birthday[2]}-{birthday[3]}")
        bth.append(answer)
    # await message.answer(bth)

    if today in bth:
        select_birthday = db.select_user_birthday_by_date(day, month)
        for birth in select_birthday:
            id = birth[2]
            answers = f"🥳🥳🥳<b>Búgin {birth[0]} tuwılǵan kúni.</b> \n\nOl búgin <b>{int(year)-birth[1]}</b> jasqa toldı. Onı qutlıqlawdı umıtpań!!!"
            await bot.send_message(id, answers)
        # await bot.send_message(ADMINS[0], select_birthday)
    else:
        pass