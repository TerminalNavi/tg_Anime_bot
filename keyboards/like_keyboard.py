from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from models import UserAnime

def get_like(user_anime: UserAnime):
    return InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton(
                    text=f'{ "❌" if user_anime.liked == -1 else "👍"}', 
                    callback_data=f'like_{user_anime.id}'
                ),
                InlineKeyboardButton(
                    text=f'{ "❌" if user_anime.liked == 1 else "👎"}', 
                    callback_data=f'dislike_{user_anime.id}'
                )
            ]
        ]
    )
