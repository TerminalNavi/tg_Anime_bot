from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from models import *
from keyboards.like_keyboard import get_like


router = Router()

@router.callback_query(F.data.startswith('like_'))
async def like(callback_query: CallbackQuery):
    user_anime_id = int(callback_query.data.split('_')[-1])
    user_anime: UserAnime = UserAnime.get_by_id(user_anime_id)
    user_anime.liked = 1
    user_anime.save()
    await callback_query.message.edit_reply_markup(
        reply_markup=get_like(user_anime)
    )

@router.callback_query(F.data.startswith('dislike_'))
async def dislike(callback_query: CallbackQuery):
    user_anime_id = int(callback_query.data.split('_')[-1])
    user_anime: UserAnime = UserAnime.get_by_id(user_anime_id)
    user_anime.liked = -1
    user_anime.save()
    await callback_query.message.edit_reply_markup(
        reply_markup=get_like(user_anime)
    )