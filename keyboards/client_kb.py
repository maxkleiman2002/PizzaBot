from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove

b1 = KeyboardButton("/Графік_роботи")
b2 = KeyboardButton("/Розміщення")
b3 = KeyboardButton("/Меню")
b4 = KeyboardButton("Поділитись номером",request_contact=True)
b5 = KeyboardButton("Відправити геолокацію",request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).insert(b3).row(b4,b5)