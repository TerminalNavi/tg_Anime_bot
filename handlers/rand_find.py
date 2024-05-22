"""Модули типов, БД и другой не менее важной фигни"""
import requests
from aiogram import F, Router
from aiogram.types import Message
from models import *


router = Router()

@router.message(F.text.lower() == 'найти')
async def with_puree(message: Message):
    '''Этот... кусок отвечает за поиск и выдачу рандомного аниме.
    А так же за создание новых и обновление старых записей в БД, проверкой на повторы'''
    user = User.get(user_id = message.from_user.id)
    while True:
        anime_url = requests.get('https://animego.org/anime/random', timeout=6).url
        anime, _ = Anime.get_or_create(url=anime_url)
        notify = UserAnime.filter(user=user, anime=anime)
        if notify.count() == 0:
            UserAnime.create(user = user, anime = anime)
            await message.answer(anime_url)
            break
