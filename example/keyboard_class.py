# -*- coding: utf-8 -*-

import telebot

#Кнопки 
class Keyboard:
    def __init__(self, bot):
        self.bot = bot
    
    def menu(self,message):
        menu_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        menu_markup.row("Главное меню")
        
        #user_markup.row('Обновления', 'Обратная связь')
        self.bot.send_message(message.from_user.id, 'Выберите пункт меню:',
                             reply_markup=user_markup)

    def technique_staining(self,message):
        tech_markup = telebot.types.InlineKeyboardMarkup()
        btn_tech = telebot.types.InlineKeyboardButton(text = 'AirTouch', callback_data = 'AirTouch')
        tech_markup.add(btn_tech)
        btn_tech = telebot.types.InlineKeyboardButton(text = 'Балаяж', callback_data = 'Балаяж')
        tech_markup.add(btn_tech)
        btn_tech = telebot.types.InlineKeyboardButton(text = 'Омбрэ', callback_data = 'Омбрэ')
        tech_markup.add(btn_tech)
        btn_tech = telebot.types.InlineKeyboardButton(text = 'Шатуш', callback_data = 'Шатуш')
        tech_markup.add(btn_tech)
        btn_tech = telebot.types.InlineKeyboardButton(text = 'Мелирование', callback_data = 'Мелирование')
        tech_markup.add(btn_tech)
        btn_tech = telebot.types.InlineKeyboardButton(text = 'Растяжка и тонирование', callback_data = 'Растяжка и тонирование')
        tech_markup.add(btn_tech)
        btn_tech = telebot.types.InlineKeyboardButton(text = 'Абсолютное счастье для волос', callback_data = 'Абсолютное счастье для волос')
        tech_markup.add(btn_tech)
        btn_tech = telebot.types.InlineKeyboardButton(text = 'Керопластика Paul Mitchel', callback_data = 'Керопластика Paul Mitchel')
        tech_markup.add(btn_tech)
        btn_tech = telebot.types.InlineKeyboardButton(text = 'Ламинирование', callback_data = 'Ламинирование')
        tech_markup.add(btn_tech)
        btn_tech = telebot.types.InlineKeyboardButton(text = 'Fabuloso', callback_data = 'Fabuloso')
        tech_markup.add(btn_tech)
        btn_tech = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
        tech_markup.add(btn_tech)
        return tech_markup
        #self.bot.send_message(message.from_user.id,
        #    "Спасибо, теперь выберите, пожалуйста, технику окрашивания или ухода за Вашими волосами:",
        #    reply_markup=tech_markup)

    def hair_length(self, message):
        length_markup = telebot.types.InlineKeyboardMarkup()
        btn_lng = telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'short')
        length_markup.add(btn_lng)
        btn_lng = telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'middle')
        length_markup.add(btn_lng)
        btn_lng = telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'long')
        length_markup.add(btn_lng)
        btn_lng = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
        length_markup.add(btn_lng)
        return length_markup
        #bot.send_message(message.from_user.i,
        #    "Выберите длину волос",reply_markup=length_markup)

    def master_category(self, message):
        master_markup = telebot.types.InlineKeyboardMarkup()
        btn_master = telebot.types.InlineKeyboardButton(text = 'Ведущие колористы',
                                                         callback_data = 'leaders')
        master_markup.add(btn_master)
        btn_master = telebot.types.InlineKeyboardButton(text = 'Мастера стилисты',
                                                         callback_data = 'masters')
        master_markup.add(btn_master)
        btn_master = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
        master_markup.add(btn_master)
        return master_markup
        #self.bot.send_message(message.from_user.id,'Выберите категорию специалиста',reply_markup=master_markup)

    def contacts(self, message):
        contacts_markup = telebot.types.InlineKeyboardMarkup()
        btn_contacts = telebot.types.InlineKeyboardButton(text = 'Vk',
                                url = 'https://vk.com/id')
        contacts_markup.add(btn_contacts)
        btn_contacts = telebot.types.InlineKeyboardButton(text = 'Instagram',
                                url = 'https://Instagram.com/id')
        contacts_markup.add(btn_contacts)
        btn_contacts = telebot.types.InlineKeyboardButton(text = 'Наш сайт',
                                url = 'https://yandex.com')
        contacts_markup.add(btn_contacts)
        btn_contacts = telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu')
        contacts_markup.add(btn_contacts)
        return contacts_markup
        #self.bot.send_message(message.from_user.id,
        #    "Мы расположены по адресу ...\n наш телефон ...", reply_markup=contacts_markup)
        

    def main_menu(self, message):
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

        return user_markup
        #bot.send_message(message.from_user.id, 'Выберите пункт меню:', 
        #               reply_markup=user_markup)



