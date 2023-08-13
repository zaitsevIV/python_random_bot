import telebot
import numpy as np
from data_for_bot import bot_functional
from functionals import password_creater
from dotenv import load_dotenv
import os

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


def int_error(value):
    try:
        value = int(value.text)
    except (TypeError, ValueError):
        return static_errors(value)
    else:
        return True


def random_number_error(f_value, s_value):
    try:
        np.random.randint(int(f_value), int(s_value.text))
    except ValueError:
        return static_errors(s_value)
    else:
        return True


def random_password_error(value):
    try:
        password_creater(value.text)
    except ValueError:
        return static_errors(value)
    else:
        return True


def static_errors(message):
    bot.send_message(message.from_user.id, f'Error! Try again!')
    for functional in range(len(bot_functional)):
        bot.send_message(message.from_user.id, f'{bot_functional[functional]}')
