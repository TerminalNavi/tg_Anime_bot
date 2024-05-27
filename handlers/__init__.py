from aiogram import Dispatcher

from handlers import rand_find, start, likes

def include_routers(dp: Dispatcher):
    dp.include_routers(
        likes.router,
        rand_find.router,
        start.router
    )