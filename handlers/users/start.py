import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu1
from data.config import ADMINS
from loader import dp, db, bot
from states.ovoz import OvozBerish

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"Xush kelibsiz! {name}\n\n<b>Urganch tumani 35-son maktabning atrofini (Beton) devor bilan o'rash</b> uchun ovoz berasizmi?",reply_markup=menu1)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
   
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"Xush kelibsiz! {name}\n\n<b>Urganch tumani 35-son maktabning atrofini (Beton) devor bilan o'rash</b> uchun ovoz berasizmi?",reply_markup=menu1)
        