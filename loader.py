from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.misc.connection import Database
from utils.misc.mail_sender.sender import SendMail
from utils.misc.google_sheets.gsheets import Gsheets


# AIOgram
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# DB
db = Database()


# MailJet
mail = SendMail(config.API_KEY, config.API_SECRET)


# Google sheets
gs = Gsheets('SharkRegBot')