from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyMonths = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Yanvar", callback_data="01"),
        InlineKeyboardButton(text="Fevral", callback_data="02"),
        InlineKeyboardButton(text="Mart", callback_data="03"),
    ],
    [
        InlineKeyboardButton(text="Aprel", callback_data="04"),
        InlineKeyboardButton(text="May", callback_data="05"),
        InlineKeyboardButton(text="Iyun", callback_data="06"),
    ],
[
        InlineKeyboardButton(text="Iyul", callback_data="07"),
        InlineKeyboardButton(text="Avgust", callback_data="08"),
        InlineKeyboardButton(text="Sentyabr", callback_data="09"),
    ],
[
        InlineKeyboardButton(text="Oktyabr", callback_data="10"),
        InlineKeyboardButton(text="Noyabr", callback_data="11"),
        InlineKeyboardButton(text="Dekabr", callback_data="12"),
    ],
])