from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from utils.models import *
from keyboards.like_keyboard import get_like


router = Router()

@router.callback_query(F.data.startswith('like_') | F.data.startswith('dislike_'))
async def like(callback_query: CallbackQuery):
    data = callback_query.data.split('_')
    user_anime_id = int(data[-1])
    reaction = data[0][0]
    user_anime: UserAnime = UserAnime.get_by_id(user_anime_id)
    like_value = user_anime.liked
    if reaction == 'l':
        user_anime.liked = 1 if like_value == 0 else 0
    if reaction == 'd':
        user_anime.liked = -1 if like_value == 0 else 0    
    user_anime.save()
    await callback_query.message.edit_reply_markup(
        reply_markup=get_like(user_anime)
    )
