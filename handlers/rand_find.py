"""Модули типов, БД и другой не менее важной фигни"""
import requests
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from models import *
from keyboards.random_kb import kb_find_random


router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    '''Без этого куска кода придётся ручками вбивать старт'''
    User.get_or_create(user_id = message.from_user.id)
    await message.answer(f"Привет, {message.from_user.full_name},"+
                          " я бот для поиска случайного аниме.", reply_markup=kb_find_random)

@router.message(F.text.lower() == 'найти')
async def with_puree(message: Message):
    '''Этот... кусок отвечает за поиск и выдачу рандомного аниме.
    А так же за создание новых и обновление старых записей в БД, проверкой на повторы'''
    ani_url = requests.get('https://animego.org/anime/random', timeout=6).url
    user = User.get(user_id = message.from_user.id)
    for i in user.animes.join(Anime):
        if ani_url == i.anime.url:
            ani_url = requests.get('https://animego.org/anime/random', timeout=6).url
    anime = Anime.create(url = ani_url)
    UserAnime.create(user = user, anime = anime)
    await message.answer(ani_url)  