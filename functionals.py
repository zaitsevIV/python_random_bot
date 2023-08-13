import random


def dice_photo(number):
    text = 'photo/' + str(number) + '.jpg'
    img = open(text, 'rb')
    return img


def password_creater(length):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '1234567890'
    string = lower + upper + number
    password = ''.join(random.sample(string, int(length)))
    return password
