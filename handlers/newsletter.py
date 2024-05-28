import asyncio
from datetime import time, timedelta, datetime
from aiogram import Bot
from utils.models import User
from utils.singleton import GlobalVars
from handlers.rand_find import random_anime
from keyboards.like_keyboard import get_like



async def get_time_notify():
    """Получить время ближайшего уведомления"""
    now = datetime.now()
    users = User.filter(User.time > now).order_by(User.time.asc())
    if users.count() > 0:
        return (users.first()).time

async def sending_messages(bot: Bot):
    """Рассылка сообщений"""

    GlobalVars.SEND_TIME = await get_time_notify()
    while True:
        now_time = datetime.now().time()
        now_time = time(now_time.hour, now_time.minute)
        if GlobalVars.SEND_TIME and GlobalVars.SEND_TIME == now_time:
            # рассылка уведомлений всем пользователям
            for user in User.filter(time=GlobalVars.SEND_TIME):
                url, ua = random_anime(user)
                await bot.send_message(
                    chat_id=user.user_id,
                    text=f'{url}\n Вам понравилось аниме?',
                    reply_markup=get_like(ua)
                )

            GlobalVars.SEND_TIME = await get_time_notify()

        now_time = (datetime.now() + timedelta(minutes=1))
        now_time = datetime(now_time.year, now_time.month, now_time.day,
                            now_time.hour, now_time.minute)
        seconds = (now_time - datetime.now()).seconds + 1
        await asyncio.sleep(seconds)
