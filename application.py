from aiogram import Bot, Dispatcher, executor, types
import logging
from Database import Function
from googletrans import Translator
from config import TOKEN
from buttons import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)
translator = Translator()
temp = 0
lst = []
setup = ''
user_id = 0


@dispatcher.message_handler(commands=["help"])
async def help_(message: types.Message):
    await message.reply(translator.translate(
        "Assalomu alaykum, bu botda ko'p ham hatolik yuz beravermaydi, lekin botni qayta ishga tushirish iloji bor >>> /restart",
        dest=setup).text)


@dispatcher.message_handler(commands=["restart"])
async def restart(message: types.Message):
    global user_id, setup, temp
    user_id -= user_id
    setup = ''
    temp -= temp
    lst.clear()
    await message.reply("Reloaded successfully!!!")


@dispatcher.message_handler(commands=["admin"])
async def show_users(message: types.Message):
    if message.from_user.id == 2003049919:
        fun1 = Function()
        for i in range(1, 8):
            try:
                await message.answer(fun1.search()[i])
            except IndexError:
                break


@dispatcher.message_handler(commands=["start"])
async def start(message: types.Message):
    global user_id
    user_id += message.from_user.id
    hello = f"Assalomu alaykum {message.from_user.first_name}!\n Dasturlash olamiga hush kelibsiz, yordamkerak bo'las /help ni bosing. Ona tilingizni tanlang"
    await message.reply(hello)
    await message.reply(translator.translate(hello, dest="ru").text, reply_markup=language_setup)


@dispatcher.message_handler()
async def register(message: types.Message):
    global temp, setup, user_id
    try:
        if user_id == message.from_user.id:
            if message.text == "Biz haqimizda":
                await message.reply("Sayt linki: https://it-park.uz\nYouTube: https://youtu.be/kHJr_Az4ZAs")
            if message.text == "Boshidan boshlash 🔁":
                lst.clear()
                temp -= temp
                user_id -= user_id
            if temp == 0:
                setup = ''
                setup += message.text[0:2].lower()
                await message.reply(translator.translate("Qaysi kursga yozilmoqchisiz?", dest=setup).text,
                                    reply_markup=adduz)
                lst.append(message.text)
                print(lst)
            elif temp == 1:
                await message.reply(translator.translate("Ismingiz-Familiyangizni kiriting", dest=setup).text,
                                    reply_markup=retry)
                lst.append(message.text)
                print(lst)
            elif temp == 2:
                await message.reply(
                    translator.translate("Telefon raqamingizni kiriting: (+998 __ ___ __ __)", dest=setup).text,
                    reply_markup=retry)
                lst.append(message.text)
                print(lst)
            elif temp == 3:
                await message.reply(
                    translator.translate("Tug'ilgan kun oy yilingizni kiriting: (dd.mm.yyyy)", dest=setup).text,
                    reply_markup=retry)
                lst.append(message.text)
                print(lst)
            elif temp == 4:
                await message.reply(
                    translator.translate("Kursga qaysi payt kelmoqchiligingizni tanlang", dest=setup).text,
                    reply_markup=time_table)
                lst.append(message.text)
                print(lst)
            elif temp == 5:
                await message.reply(
                    translator.translate(
                        "Ro'yxatdan o'tish uchun ma'lumotlaringiz tayyor! Quyidagi tugmani bosing").text,
                    reply_markup=eventually)
                lst.append(message.text)
                print(lst)
            if message.text == "📓 Ro'yxatdan o'tish 📓":
                lst.remove(lst[0])
                fun = Function()
                await message.reply(translator.translate(fun.signup(lst), dest=setup).text, reply_markup=retry)
                user_id -= user_id
            temp += 1
        else:
            await message.reply(translator.translate(
                "Mingbor uzr, lekin bot yana boshqa foydalanuvchiga xizmat ko'rsatmoqda. Iltimos bir ozdan so'ng yozing").text,
                                reply_markup=retry)
    except ValueError:
        await message.reply(
            translator.translate("Iltimos, ona tilingizni kiriting, shunda biz ham shu tilda gapiramiz").text,
            reply_markup=language_setup)
        print(setup)
        setup += message.text
        temp -= temp


if __name__ == '__main__':
    fun2 = Function()
    fun2.tables()
    executor.start_polling(dispatcher, skip_updates=True)
