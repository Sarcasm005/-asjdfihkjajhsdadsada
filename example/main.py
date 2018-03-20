# -*- coding: utf-8 -*-
"""
main created 15.03.2018 by brdsky
"""


import telebot
import config
from keyboard_class import Keyboard

bot = telebot.TeleBot(config.token)
keyboard = Keyboard(bot)

#В самом начале появляется
@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.InlineKeyboardMarkup()
    btn_main = telebot.types.InlineKeyboardButton(text = "Узнать стоимость окрашивания на свои волосы",
                                                    callback_data = "staining_cost")
    user_markup.add(btn_main)
    btn_main = telebot.types.InlineKeyboardButton(text = "Записаться",
                                                    callback_data = "enroll")
    user_markup.add(btn_main)
    btn_main = telebot.types.InlineKeyboardButton(text = "Примеры наших работ",
                                                    callback_data = "examples")
    user_markup.add(btn_main)
    btn_main = telebot.types.InlineKeyboardButton(text = "Контакты",
                                                    callback_data = "contacts")
    user_markup.add(btn_main)
    bot.send_message(message.from_user.id, 'Выберите пункт меню:', 
                        reply_markup=user_markup)

#обработчик коллбеков
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "AirTouch":
            bot.send_message(call.message.chat.id,
                        text="AirTouch\n20000 – 24000 рублей")
        if call.data == "Балаяж":
            bot.send_message(call.message.chat.id,
                        text="Балаяж\nКороткие – 9500 – 10900 рублей\nСредние – 9900 – 11500 рублей\nДлинные – 10900 – 12900 рублей")
        if call.data == "contacts": #контакты 
            bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                        message_id=call.message.message_id, reply_markup = keyboard.contacts(call))
        if call.data == "staining_cost": #стоимость покраски
            bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                        message_id=call.message.message_id, reply_markup = keyboard.technique_staining(call))
        if call.data == "enroll": #записаться
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup = master_markup)
            bot.send_contact(chat_id=call.message.chat.id, phone_number = "+79823112313",
                        first_name = "Мастер N")
        if call.data == "menu": #главное меню
            bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                        message_id=call.message.message_id, reply_markup = keyboard.main_menu(call))

if __name__ == "__main__":
    bot.polling(none_stop=True)
