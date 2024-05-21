from aiogram import Dispatcher

from handlers import rand_find

def include_routers(dp: Dispatcher):
    dp.include_routers(
        rand_find.router,
    )