from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from tokens.bot_tokens import bot_token
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
TOKEN = bot_token()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
