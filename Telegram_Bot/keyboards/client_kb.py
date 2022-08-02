from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Jokes')
b2 = KeyboardButton('Help')
b3 = KeyboardButton('Horoscope')
b4 = KeyboardButton('Weather')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1, b4).row(b3, b2)
