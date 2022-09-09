from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from telegram import ReplyKeyboardRemove


menu1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Ovoz berish")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# ovoz_berish_tugma = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton("Telefon raqamni yuborish",request_contact=True)]
#     ],
#     resize_keyboard=True
# )

back = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Bekor qilish")]
    ],
    resize_keyboard=True
)