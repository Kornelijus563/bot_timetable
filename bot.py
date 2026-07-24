from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from logic import *
import schedule
import threading
import time
from config import *

bot = TeleBot(API_TOKEN)

def gen_markup(id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Получить!", callback_data=id))
    return markup

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, f"Привет, {message.from_user.first_name}! Добро пожаловать в наш бот! ")

bot.polling(none_stop=True)