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
    elif message.text == 'Корзина':
        isOtiv = False
        markup1 = types.InlineKeyboardMarkup()
        markup2 = types.InlineKeyboardMarkup()
        s1 = "Капучино: " + str(cap)
        s2 = "Латте: " + str(lat)
        cappuccino_add = types.InlineKeyboardButton('Добавить', callback_data='cappuccino_add')
        cappuccino_del = types.InlineKeyboardButton('Удалить все', callback_data='cappuccino_del')
        cappuccino_del_one = types.InlineKeyboardButton('Удалить', callback_data='cappuccino_del_one')
        latte_del = types.InlineKeyboardButton('Удалить все', callback_data='latte_del')
        latte_add = types.InlineKeyboardButton('Добавить', callback_data='latte_add')
        latte_del_one = types.InlineKeyboardButton('Удалить', callback_data='latte_del_one')
        markup1.row(cappuccino_del, cappuccino_del_one, cappuccino_add)
        markup2.row(latte_del, latte_del_one, latte_add)
        bot.reply_to(message, s1, reply_markup=markup1)
        bot.reply_to(message, s2, reply_markup=markup2)
    elif message.text == 'Оплата':
        isOtiv = False
        markup = types.InlineKeyboardMarkup()
        op = types.InlineKeyboardButton('Оплатил', callback_data='pay')
        markup.row(op)
        bot.reply_to(message, 'Переведите по номеру 89289851280', reply_markup=markup)
    elif message.text == 'Отзыв':
        isOtiv = True
        bot.send_message(message.chat.id, 'Напишите отзыв:')
    elif isOtiv:
        call = f'echo "{message.text}" > {message.from_user.username}_otziv.txt'
        os.system(call)
        isOtiv = False
        bot.send_message(message.chat.id, 'Спасибо за отзыв')

@bot.callback_query_handler(func=lambda callback: True)
def callback_message_menu(callback):
    global lat
    global cap
    if callback.data == 'cappuccino':
        markup = types.InlineKeyboardMarkup()
        add = types.InlineKeyboardButton('Добавить в корзину', callback_data='add_capp')
        back = types.InlineKeyboardButton('Назад', callback_data='back_back')
        markup.row(add, back)
        photo = open("cappuchino.jpg", "rb")
        caption = 'Капучино\nСостав:\n    60мл эспрессо\n    200мл подогретое молоко\n    25мл молочная пена\nЦена:200р'
        # bot.send_photo(chat_id=callback.message.chat.id, photo=photo)
        bot.edit_message_text(text=caption, chat_id=callback.message.chat.id, message_id=callback.message.id, reply_markup = markup)
