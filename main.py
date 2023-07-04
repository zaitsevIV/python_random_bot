import functionals
from data_for_bot import bot_text, bot_functional
from errors import int_error, random_number_error, random_password_error, static_errors
import telebot
import random
from dotenv import load_dotenv
import os


load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, f'{bot_text[0]}, '
                                               f'{message.from_user.first_name}!')
        for text in range(1, 3):
            bot.send_message(message.from_user.id, f'{bot_text[text]}')
    elif message.text == '/functional':
        for functional in range(len(bot_functional)):
            bot.send_message(message.from_user.id, f'{bot_functional[functional]}')
    elif message.text == '/random_number':
        msg = bot.send_message(message.from_user.id, f'Input your first number ')
        bot.register_next_step_handler(msg, first_random_number)
    elif message.text == '/random_dice_number':
        number = random.randint(1, 6)
        bot.send_photo(message.from_user.id, functionals.dice_photo(number))
    elif message.text == '/random_password':
        msg = bot.send_message(message.from_user.id, f'Input length of password')
        bot.register_next_step_handler(msg, password)
    else:
        static_errors(message)


def first_random_number(message):
    if int_error(message) is True:
        msg = bot.send_message(message.from_user.id, f'Input your second number ')
        bot.register_next_step_handler(msg, second_random_number, message.text)


def second_random_number(message, value):
    if int_error(message) is True and random_number_error(value, message) is True:
        bot.send_message(message.from_user.id, f'Number can be in the range(from {value} to {message.text})\n'
                                               f'Your random number: '
                                               f'{random.randint(int(value), int(message.text))}')


def password(message):
    if int_error(message) is True and random_password_error(message) is True:
        bot.send_message(message.from_user.id, f'{functionals.password_creater(int(message.text))}')


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
