"""Промежуточный файл"""
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# для хранения данных из fsm
storage = MemoryStorage()

TOKEN = 'your token from telgram bot'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)