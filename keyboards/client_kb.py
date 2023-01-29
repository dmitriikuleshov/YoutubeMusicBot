from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton('/start')
button2 = KeyboardButton('/help')
button3 = KeyboardButton('Поделиться номером', request_contact=True)
button4 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True,
                                one_time_keyboard=True)
# also can use insert, row, col
kb_client.row(button1, button2)
kb_client.row(button3, button4)
