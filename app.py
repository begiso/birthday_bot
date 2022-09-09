from aiogram import executor
import asyncio
from loader import dp, db
from handlers.users.user_birthday import check_db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

async def on_startup(dispatcher):
    # Birlamchi komandalar (/start va /help)
    await set_default_commands(dispatcher)
    try:
        db.create_table_users()
        db.create_table_birthdays()
    except Exception as err:
        print(err)
    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    # scheduler.add_job(check_db, "cron", hour=17, minute=38, args=(dp, ))
    scheduler.add_job(check_db, "cron", hour=17, minute=55, args=(dp, ))


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)