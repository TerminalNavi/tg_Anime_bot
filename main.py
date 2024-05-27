import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import include_routers
from config_reader import config


bot = Bot(token=config.bot_token.get_secret_value())
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()

async def main():
    '''Функция для запуска бота'''
    include_routers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())