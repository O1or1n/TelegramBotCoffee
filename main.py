import telebot
from telebot import types
import os

bot = telebot.TeleBot('7069938356:AAHMhXXPD0l0Wwf23dwk3I-yV2gAXZAlHYc')#кирилла

lat = 0
cap = 0
isOtiv = False

@bot.message_handler(commands=['start'])
def answer_on_command(message):
    markup = types.ReplyKeyboardMarkup()
    button_menu = types.KeyboardButton('Меню')
    button_payment = types.KeyboardButton('Оплата')
    button_basket = types.KeyboardButton('Корзина')
    button_review = types.KeyboardButton('Отзыв')
