# -*- coding: utf-8 -*-
"""
main created 15.03.2018 by brdsky

upgraded by monsherko 29.03.2018
"""


import telebot
import config
import random
import time
import preparatgun
import os

from keyboard_class import Keyboard

bot = telebot.TeleBot(config.token)
keyboard = Keyboard(bot)
knownUsers = {}


@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.from_user.id, config.great, reply_markup=keyboard.main_menu(message))

@bot.message_handler(func=lambda mess: "Главное меню" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=keyboard.main_menu(message))

@bot.message_handler( content_types=['photo'])
def up_photo(message):
    try:
        if knownUsers[message.from_user.id] == 1:
            file_info = bot.get_file(message.photo[0].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
        #    src = config.path_name + file_info.file_path;
            with open(config.path_name + file_info.file_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            knownUsers[message.from_user.id] += 1
#                botan.track(config.botan_key, message.from_user.id, 'Узнали стоимость')
            time.sleep(2)
            bot.send_message(message.from_user.id, 'Пришлите, пожалуйста, фото ожидаемого результата')
        elif knownUsers[message.from_user.id] == 2:
            file_info = bot.get_file(message.photo[0].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = config.path_name + file_info.file_path;
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            knownUsers[message.from_user.id] =  str(src)
#                botan.track(config.botan_key, message.from_user.id, 'Узнали стоимость')
            time.sleep(2)
            bot.send_message(message.from_user.id, 'Спасибо, теперь выберите, пожалуйста, технику окрашивания или ухода за Вашими волосами:', reply_markup=keyboard.technique_staining(message))

    except Exception as e:
        bot.reply_to(message,e)

@bot.message_handler(func=lambda mess: "Узнать стоимость окрашивания на свои волосы" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Пришлите, пожалуйста, фото Ваших волос")
    knownUsers[message.from_user.id] = 1



@bot.message_handler(func=lambda mess: "Контакты" == mess.text, content_types=['text'])
def handle_text(message):
#    botan.track(config.botan_key,message.from_user.id, 'просмотр адреса магазина')

    bot.send_message(message.from_user.id, 'Скопируйте адрес в навигатор\n\nЗнаменка 13 стр 4\n\nИли воспользуйтесь меткой ниже', reply_markup=keyboard.contacts(message))
#    bot.send_message(message.from_user.id, 'Скопируйте адрес в навигатор\n\nЗнаменка 13 стр 4\n\nИли воспльзуйтесь меткой ниже')
    bot.send_location(message.from_user.id,latitude=55.7497765, longitude=37.6040817);


@bot.message_handler(func=lambda mess: "Записаться" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'Записаться можно связавшись с нашим администратором, пришлите ему фото ваших волос и фото желаемого результата.', reply_markup=keyboard.enroll(message))
#    bot.send_message(message.from_user.id, 'Записаться можно связавшись с нашим администратором', reply_markup=keyboard.enroll(message))


@bot.message_handler(func=lambda mess: "Примеры наших работ" == mess.text,  content_types=['text'])
def handle_text(message):
#    botan.track(config.botan_key,message.from_user.id, 'Просмотр Instagram профиля')
    bot.send_message(message.from_user.id, 'Посмотреть примеры работ можно в нашем Instagram, а также на сайте', reply_markup=keyboard.examples(message))


#обработчик коллбеков
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "AirTouch":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_airtouch_leaders'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_airtouch_masters'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "Балаяж" or call.data == "Омбрэ" or call.data == "Шатуш" or call.data == "Мелирование":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_bal_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_bal_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_bal_long'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)
        if call.data == "Растяжка и тонирование":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_rast_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_rast_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_rast_long'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)
        if call.data == "Абсолютное счастье для волос":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_happy_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_happy_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_happy_long'))

            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Очень длинные', callback_data = 'accept_happy_verylong'))

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)
        if call.data == "Керопластика Paul Mitchel":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_ker_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_ker_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_ker_long'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)
        if call.data == "Ламинирование":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_lam_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_lam_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_lam_long'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)
        if call.data == "Fabuloso":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_fab_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_fab_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_fab_long'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)

        if call.data == "accept_airtouch_leaders": #главное меню
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 20000 – 24000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_airtouch_masters": #главное меню
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 20000 – 24000 рублей ", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)


        if call.data == "accept_bal_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_bal_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_bal_short'))

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_bal_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_bal_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_bal_middle'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_bal_long":

            master_markup = telebot.types.InlineKeyboardMarkup()

            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_bal_long'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_bal_long'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)



        if call.data == "accept_leaders_bal_short":
            master_markup = telebot.types.InlineKeyboardMarkup()

            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 9500 – 10900 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_bal_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 9500 – 10900 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_bal_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 9900 – 11500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_bal_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 9900 – 11500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_bal_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 10900 – 12900 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_bal_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 10900 – 12900 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == 'accept_rast_short':
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_rast_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_rast_short'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_rast_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_rast_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_rast_middle'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_rast_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_rast_long'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_rast_long'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_leaders_rast_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 7000 – 7500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_rast_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 7000 – 7500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_rast_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 7000 – 7500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_rast_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 7000 – 7500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_rast_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 7500 – 8900 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_rast_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 7500 – 8900 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)

        if call.data == "accept_happy_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_happy_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_happy_short'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_happy_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_happy_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_happy_middle'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_happy_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_happy_long'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_happy_long'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_happy_verylong":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_happy_verylong'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_happy_verylong'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)


        if call.data == "accept_leaders_happy_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 3000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_happy_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 3000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_happy_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 4500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_happy_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 4500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_happy_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 6000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_happy_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 6000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_happy_verylong":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 7000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_happy_verylong":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 7000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_ker_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_ker_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_ker_short'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_ker_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_ker_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_ker_middle'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_ker_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_ker_long'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_ker_long'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)


        if call.data == "accept_leaders_ker_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 10500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_ker_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 10500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_ker_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 11500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_ker_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 11500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_ker_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 13000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_ker_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 13000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)



        if call.data == "accept_lam_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_lam_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_lam_short'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_lam_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_lam_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_lam_middle'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_lam_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_lam_long'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_lam_long'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)


        if call.data == "accept_leaders_lam_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 3500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_lam_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 3500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_lam_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 4500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_lam_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 4500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_lam_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 5500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_lam_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 5500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)



        if call.data == "accept_fab_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_fab_short'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_fab_short'))

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_fab_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_fab_middle'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_fab_middle'))

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_fab_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_fab_long'))
            master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_fab_long'))
            #master_markup.add(telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu'))

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)


        if call.data == "accept_leaders_fab_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 5000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_fab_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 5000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_fab_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 5000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_fab_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 5000 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_masters_fab_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 6500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)
        if call.data == "accept_leaders_fab_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            bot.send_photo(chat_id=call.message.chat.id,caption="Ориентировочная стоимость услуг : 6500 рублей", photo=open(str(knownUsers[call.message.chat.id]), 'rb'))
            bot.send_message(chat_id=call.message.chat.id, text = config.text_end)

if __name__ == "__main__":
    preparatgun.prepare(config.path_name + 'photos/')

    bot.polling(none_stop=True)
