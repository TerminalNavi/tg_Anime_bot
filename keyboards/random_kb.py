from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb_find_random = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text='Найти')],
    [KeyboardButton(text='Задать время рассылки')]
    ],
    resize_keyboard=True
    )
