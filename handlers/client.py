from aiogram import types, Dispatcher

from create_bot import bot,dp
from keyboards import kb_client
from  aiogram.types import ReplyKeyboardRemove
#@dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id,'Вітаємо, що бажаєте?',reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Спілкування з ботом проходить у особистих повідомленнях, \nнапишіть сюди: https://t.me/PizzaCheTestBot')

#@dp.message_handler(commands=['Графік_роботи'])
async def schedule(message: types.Message):
    await bot.send_message(message.from_user.id,"Пн-Пт - З 08:00 До 22:00\n Сб-Нд - З 12:00 До 24:00")

#@dp.message_handler(commands=['Розміщення'])
async def place_func(message: types.Message):
    await bot.send_message(message.from_user.id,"вул. Героїв Майдану 69",reply_markup=ReplyKeyboardRemove())

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start,commands=['start','help'])
    dp.register_message_handler(schedule,commands=['Графік_роботи'])
    dp.register_message_handler(place_func,commands=['Розміщення'])
