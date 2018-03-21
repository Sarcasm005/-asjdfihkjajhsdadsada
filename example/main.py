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
    bot.send_message(message.from_user.id, 'Выберите пункт меню', 
                        reply_markup=user_markup)

#обработчик коллбеков
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "AirTouch":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_airtouch_leaders')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_airtouch_masters')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "Балаяж" or call.data == "Омбрэ" or call.data == "Шатуш" or call.data == "Мелирование":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_bal_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_bal_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_bal_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)
        if call.data == "Растяжка и тонирование":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_rast_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_rast_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_rast_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)
        if call.data == "Абсолютное счастье для волос":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_happy_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_happy_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_happy_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Очень длинные', callback_data = 'accept_happy_verylong')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)
        if call.data == "Керопластика Paul Mitchel":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_ker_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_ker_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_ker_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)
        if call.data == "Ламинирование":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_lam_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_lam_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_lam_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)
        if call.data == "Fabuloso":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'accept_fab_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'accept_fab_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'accept_fab_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите длину волос",reply_markup = master_markup)
   

        if call.data == "contacts": #контакты 
            bot.edit_message_text(chat_id=call.message.chat.id,
                        message_id=call.message.message_id, text="Мы расположенны по адресу ...",reply_markup = keyboard.contacts(call))
   

        if call.data == "staining_cost": #стоимость покраски
            bot.edit_message_text(chat_id=call.message.chat.id,
                        message_id=call.message.message_id, text = "Спасибо, теперь выберите, пожалуйста, технику окрашивания или ухода за Вашими волосами:" ,reply_markup = keyboard.technique_staining(call))
   

        if call.data == "enroll": #записаться
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Наш менеджер в Telegram', url = "telegram.me/example")
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Наш менеджер в Instagram', url = "https://Instagram.com/id")
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Записаться можно связавшись с нашим менеджером",reply_markup = master_markup)
 

        if call.data == "examples":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Instagram', url = "https://Instagram.com/id")
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Посмотреть примеры работ можно в нашем Instagram",reply_markup = master_markup)



        if call.data == "menu": #главное меню
            bot.edit_message_text(chat_id=call.message.chat.id,
                        message_id=call.message.message_id,text = "Выберите пункт меню", reply_markup = keyboard.main_menu(call))


        if call.data == "accept_airtouch_leaders": #главное меню
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 20000 – 24000 рублей",reply_markup = master_markup)
        if call.data == "accept_airtouch_masters": #главное меню
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 20000 – 24000 рублей ",reply_markup = master_markup)
        


        if call.data == "accept_bal_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_bal_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_bal_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)        
        if call.data == "accept_bal_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_bal_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_bal_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)  
        if call.data == "accept_bal_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_bal_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_bal_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)  
       


        if call.data == "accept_leaders_bal_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 9500 – 10900 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_bal_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 9500 – 10900 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_bal_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 9900 – 11500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_bal_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 9900 – 11500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_bal_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 10900 – 12900 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_bal_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 10900 – 12900 рублей",reply_markup = master_markup)


        if call.data == 'accept_rast_short':
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_rast_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_rast_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)  
        if call.data == "accept_rast_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_rast_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_rast_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_rast_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_rast_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_rast_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)


        if call.data == "accept_leaders_rast_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 7000 – 7500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_rast_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 7000 – 7500 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_rast_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 7000 – 7500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_rast_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 7000 – 7500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_rast_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 7500 – 8900 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_rast_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 7500 – 8900 рублей",reply_markup = master_markup)


        if call.data == "accept_happy_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_happy_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_happy_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_happy_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_happy_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_happy_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_happy_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_happy_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_happy_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_happy_verylong":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_happy_verylong')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_happy_verylong')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)


        if call.data == "accept_leaders_happy_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 3000 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_happy_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 3000 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_happy_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 4500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_happy_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 4500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_happy_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 6000 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_happy_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 6000 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_happy_verylong": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 7000 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_happy_verylong": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 7000 рублей",reply_markup = master_markup)





        if call.data == "accept_ker_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_ker_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_ker_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_ker_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_ker_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_ker_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_ker_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_ker_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_ker_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)


        if call.data == "accept_leaders_ker_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 10500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_ker_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 10500 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_ker_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 11500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_ker_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 11500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_ker_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 13000 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_ker_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 13000 рублей",reply_markup = master_markup)




        if call.data == "accept_lam_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_lam_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_lam_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_lam_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_lam_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_lam_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_lam_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_lam_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_lam_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)


        if call.data == "accept_leaders_lam_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 3500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_lam_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 3500 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_lam_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 4500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_lam_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 4500 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_lam_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 5500 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_lam_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 5500 рублей",reply_markup = master_markup)




        if call.data == "accept_fab_short":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_fab_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_fab_short')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_fab_middle":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_fab_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_fab_middle')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)
        if call.data == "accept_fab_long":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'accept_leaders_fab_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'accept_masters_fab_long')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите категорию мастера",reply_markup = master_markup)


        if call.data == "accept_leaders_fab_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 5000 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_fab_short": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 5000 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_fab_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 5000 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_fab_middle": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 5000 рублей",reply_markup = master_markup)
        if call.data == "accept_masters_fab_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 6500 рублей",reply_markup = master_markup)
        if call.data == "accept_leaders_fab_long": 
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : 6500 рублей",reply_markup = master_markup)
if __name__ == "__main__":
    bot.polling(none_stop=True)
