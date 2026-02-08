#config.py
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_URL = os.getenv("DB_URL")
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set in .env")

if not DB_URL:
    raise RuntimeError("DB_URL not set in .env")
