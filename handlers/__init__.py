from aiogram import Dispatcher

from handlers import rand_find, start, likes, set_time

def include_routers(dp: Dispatcher):
    dp.include_routers(
        likes.router,
        rand_find.router,
        start.router,
        set_time.router
    )