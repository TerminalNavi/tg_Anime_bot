import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import include_routers
from utils.config_reader import config
from handlers.newsletter import sending_messages

bot = Bot(token=config.bot_token.get_secret_value())
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()

async def on_startup():
    """Обертка что бы запустить параллельный процесс"""
    asyncio.create_task(sending_messages(bot))

async def main():
    '''Старт бота'''
    dp.startup.register(on_startup)
    include_routers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())