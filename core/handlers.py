from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from sqlalchemy import select
from core.db import Session
from core.models import User

async def start_handler(bot: AsyncTeleBot, message: Message):
    async with Session() as session:
        user = await session.get(User, message.from_user.id)

        if not user:
            user = User(
                id=message.from_user.id,
                language=message.from_user.language_code or "ru"
            )
            session.add(user) 
            await session.commit()

    await bot.send_message(
        message.chat.id,
        "Привет 👋\n\n"
        "Я мультисервисный музыкальный бот.\n"
        "Отправь ссылку — и я всё скачаю 😈"
    )