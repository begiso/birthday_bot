from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

checkBirthday = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="✅Awa", callback_data="add"),
        InlineKeyboardButton(text="✏️Qaytaldan kiritiw", callback_data="edit"),
    ],
])