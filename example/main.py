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
            #bot.send_message(call.message.chat.id,
            #            text="AirTouch\n20000 – 24000 рублей")
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Выбрать AirTouch', callback_data = 'accept')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="AirTouch\n20000 – 24000 рублей",reply_markup = master_markup)
        if call.data == "Балаяж":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Выбрать Балаяж', callback_data = 'accept')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Балаяж\nКороткие – 9500 – 10900 рублей\nСредние – 9900 – 11500 рублей\nДлинные – 10900 – 12900 рублей",reply_markup = master_markup)
            #bot.send_message(call.message.chat.id,
            #            text="Балаяж\nКороткие – 9500 – 10900 рублей\nСредние – 9900 – 11500 рублей\nДлинные – 10900 – 12900 рублей")
        if call.data == "Омбрэ":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Выбрать Омбрэ', callback_data = 'accept')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Омбрэ\nКороткие – 9500 – 10900 рублей\nСредние – 9900 – 11500 рублей\nДлинные – 10900 – 12900 рублей",reply_markup = master_markup)
            #bot.send_message(call.message.chat.id,
            #            text="Омбрэ\nКороткие – 9500 – 10900 рублей\nСредние – 9900 – 11500 рублей\nДлинные – 10900 – 12900 рублей")
        if call.data == "Шатуш":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Выбрать Шатуш', callback_data = 'accept')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Шатуш\nКороткие – 9500 – 10900 рублей\nСредние – 9900 – 11500 рублей\nДлинные – 10900 – 12900 рублей",reply_markup = master_markup)
            #bot.send_message(call.message.chat.id,
            #            text="Шатуш\nКороткие – 9500 – 10900 рублей\nСредние – 9900 – 11500 рублей\nДлинные – 10900 – 12900 рублей")
        if call.data == "Мелирование":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Выбрать Мелирование', callback_data = 'accept')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Мелирование\nКороткие – 9500 – 10900 рублей\nСредние – 9900 – 11500 рублей\nДлинные – 10900 – 12900 рублей",reply_markup = master_markup)
            #bot.send_message(call.message.chat.id,
            #            text="Мелирование\nКороткие – 9500 – 10900 рублей\nСредние – 9900 – 11500 рублей\nДлинные – 10900 – 12900 рублей")
        if call.data == "Растяжка и тонирование":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Выбрать Растяжку и тонирование', callback_data = 'accept')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Растяжка и тонирование\nКороткие – 7000 – 7500 рублей\nСредние – 7000 – 7500 рублей\nДлинные – 7500 – 8900 рублей",reply_markup = master_markup)
            
            #bot.send_message(call.message.chat.id,
            #            text="Растяжка и тонирование\nКороткие – 7000 – 7500 рублей\nСредние – 7000 – 7500 рублей\nДлинные – 7500 – 8900 рублей")
        if call.data == "Абсолютное счастье для волос":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Выбрать Абсолютное счастье для волос', callback_data = 'accept')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Абсолютное счастье для волос\nКороткие – 3000 рублей\nСредние – 4500 рублей\nДлинные – 6000 рублей\nОчень длинные – 7000 рублей",reply_markup = master_markup)
            #bot.send_message(call.message.chat.id,
            #            text="Абсолютное счастье для волос\nКороткие – 3000 рублей\nСредние – 4500 рублей\nДлинные – 6000 рублей\nОчень длинные – 7000 рублей")
        if call.data == "Керопластика Paul Mitchel":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Выбрать Керопластику Paul Mitchel', callback_data = 'accept')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Керопластика Paul Mitchel\nКороткие – 10500 рублей\nСредние – 11500 рублей\nДлинные – 13000 рублей",reply_markup = master_markup)
            #bot.send_message(call.message.chat.id,
            #            text="Керопластика Paul Mitchel\nКороткие – 10500 рублей\nСредние – 11500 рублей\nДлинные – 13000 рублей")
        if call.data == "Ламинирование":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Выбрать Ламинирование', callback_data = 'accept')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Ламинирование\nКороткие – 3500 рублей\nСредние – 4500 рублей\nДлинные – 5500 рублей",reply_markup = master_markup)
            #bot.send_message(call.message.chat.id,
            #            text="Ламинирование\nКороткие – 3500 рублей\nСредние – 4500 рублей\nДлинные – 5500 рублей")
        if call.data == "Fabuloso":
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Выбрать Fabuloso', callback_data = 'accept')
            master_markup.add(btn_master)
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Fabuloso\nКороткие и средние – 5000 рублей\nДлинные – +30%",reply_markup = master_markup)
            #bot.send_message(call.message.chat.id,
            #            text="Fabuloso\nКороткие и средние – 5000 рублей\nДлинные – +30%")
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
            #bot.send_contact(chat_id=call.message.chat.id, phone_number = "+79823112313",
            #            first_name = "Мастер N")
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
        if call.data == "accept": #главное меню
            bot.edit_message_text(chat_id=call.message.chat.id,
                        message_id=call.message.message_id, text = "Выберите длину волос" , reply_markup = keyboard.hair_length(call))
            #bot.answer_callback_query()

        if call.data == "short": #главное меню
            bot.edit_message_text(chat_id=call.message.chat.id,
                        message_id=call.message.message_id, text = "Выберите категорию мастера" , reply_markup = keyboard.master_category(call))
        if call.data == "middle": #главное меню
            bot.edit_message_text(chat_id=call.message.chat.id,
                        message_id=call.message.message_id, text = "Выберите категорию мастера", reply_markup = keyboard.master_category(call))
        if call.data == "long": #главное меню
            bot.edit_message_text(chat_id=call.message.chat.id,
                        message_id=call.message.message_id, text = "Выберите категорию мастера", reply_markup = keyboard.master_category(call))
        if call.data == "leaders": #главное меню
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : ",reply_markup = master_markup)
        if call.data == "masters": #главное меню
            master_markup = telebot.types.InlineKeyboardMarkup()
            btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
            master_markup.add(btn_master)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Стоимость услуг : ",reply_markup = master_markup)

if __name__ == "__main__":
    bot.polling(none_stop=True)
