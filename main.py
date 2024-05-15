'''Несколько жизненно необходимых модулей'''
import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, BotCommand, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from db import User


bot_token = open('config.txt', encoding='UTF-8').readline().replace('\n', '')
logging.basicConfig(level=logging.INFO)
bot = Bot(bot_token)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    '''Без этого куска кода придётся ручками вбивать старт'''
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота')])
    inline_markup = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton(text = 'Найти', callback_data = 'find')]])
    await message.answer(f"Привет, {message.from_user.full_name},"+
                          "я бот для поиска случайного аниме.", reply_markup=inline_markup)

@dp.callback_query(F.data == "find")
async def with_puree(callback_query: CallbackQuery):
    '''Этот... кусок отвечает за поиск и выдачу рандомного аниме.
    А так же за создание новых и обновление старых записей в БД, проверкой на повторы'''
    ani_url = requests.get('https://animego.org/anime/random', timeout=6).url
    u = User.get_or_create(user_id = callback_query.message.from_user.id)
    while True:
        if ani_url == u[0].anime_url:
            ani_url = requests.get('https://animego.org/anime/random', timeout=6).url
        else:
            u[0].anime_url = ani_url
            u[0].save()
            break
    await callback_query.message.answer(ani_url)

async def main():
    '''Мэин это мэин. Заставляет бота крутиться.'''
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
