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
    markup.row(button_menu)
    markup.row(button_payment)
    markup.row(button_basket)
    markup.row(button_review)
    bot.send_message(message.chat.id, f'Привет {message.from_user.username}', reply_markup=markup)

@bot.message_handler()
def lp(message):
    global cap, lat, isOtiv
    if message.text == 'Меню':
        isOtiv = False
        markup = types.InlineKeyboardMarkup()
        cappuccino = types.InlineKeyboardButton('Капучино', callback_data='cappuccino')
        latte = types.InlineKeyboardButton('Латте', callback_data='latte')
        markup.row(cappuccino, latte)
        bot.reply_to(message, 'Меню', reply_markup=markup)
