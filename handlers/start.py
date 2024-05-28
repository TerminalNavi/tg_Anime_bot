from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from utils.models import *
from keyboards.random_kb import kb_find_random


router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    '''Без этого куска кода придётся ручками вбивать старт'''
    User.get_or_create(user_id = message.from_user.id)
    await message.answer(f"Привет, {message.from_user.full_name},"+
                          " я бот для поиска случайного аниме.", reply_markup=kb_find_random)
