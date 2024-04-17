import requests
# response = requests.get('https://animego.org/anime/random')
# print(response.url)

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command



# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7139324581:AAHa2UuMR_EmPahumk8mf7trmUNObe06IAA")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Hello!")
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Найти")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Привет, я бот, ищущий случайное аниме", reply_markup=keyboard)



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Найти")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer("Привет, я бот для поиска случайного аниме.", reply_markup=keyboard)

@dp.message(F.text.lower() == "найти")
async def with_puree(message: types.Message):
    await message.reply(requests.get('https://animego.org/anime/random').url)

if __name__ == "__main__":
    asyncio.run(main())