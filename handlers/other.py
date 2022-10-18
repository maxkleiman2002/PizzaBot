import json
import string

from aiogram import types,Dispatcher
from create_bot import dp,bot

#@dp.message_handler()
async def obscene_word_filter(message: types.Message):
    if {i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply("Нецензурна брань заборонена")
        await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(obscene_word_filter)

