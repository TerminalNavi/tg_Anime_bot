import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import include_routers


bot_token = open('config.txt', encoding='UTF-8').readline().replace(' ', '')
logging.basicConfig(level=logging.INFO)
bot = Bot(bot_token)
dp = Dispatcher()

async def main():
    '''Функция для запуска бота'''
    include_routers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())