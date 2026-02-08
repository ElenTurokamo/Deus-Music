import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot import asyncio_filters

from core.config import BOT_TOKEN
from core.handlers import start_handler
from core.db import engine
from core.models import Base

bot = AsyncTeleBot(BOT_TOKEN, parse_mode="HTML")

@bot.message_handler(commands=["start"])
async def start(message):
    await start_handler(bot, message)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def main():
    print("Initializing database...")
    await init_db()

    bot.add_custom_filter(asyncio_filters.StateFilter(bot))

    print("Bot started asynchronously.")
    await bot.infinity_polling()