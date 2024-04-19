import requests
from db import *
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command



bot_token = open('config.txt').readline()
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(bot_token)
# Диспетчер
dp = Dispatcher()


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
    await message.answer(f"Привет, {message.from_user.full_name}, я бот для поиска случайного аниме.", reply_markup=keyboard)

@dp.message(F.text.lower() == "найти")
async def with_puree(message: types.Message):
    ani_url = requests.get('https://animego.org/anime/random').url
    User.get_or_create(user_id = message.from_user.id)
    while True:
        if ani_url == User.get(User.user_id == message.from_user.id).anime_url:
            ani_url = requests.get('https://animego.org/anime/random').url
        else:
            User.update(anime_url=ani_url)
            break
    await message.reply(ani_url)

if __name__ == "__main__":
    asyncio.run(main())
