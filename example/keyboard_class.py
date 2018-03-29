# -*- coding: utf-8 -*-

import telebot
import config
#Кнопки
class Keyboard:
    def __init__(self, bot):
        self.bot = bot

    def menu(self,message):
        menu_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        menu_markup.row("Главное меню")
        return menu_markup

    def technique_staining(self,message):
        tech_markup = telebot.types.InlineKeyboardMarkup()

        tech_markup.add(telebot.types.InlineKeyboardButton(text = 'AirTouch', callback_data = 'AirTouch'))
        tech_markup.add(telebot.types.InlineKeyboardButton(text = 'Балаяж', callback_data = 'Балаяж'))
        tech_markup.add(telebot.types.InlineKeyboardButton(text = 'Омбрэ', callback_data = 'Омбрэ'))
        tech_markup.add(telebot.types.InlineKeyboardButton(text = 'Шатуш', callback_data = 'Шатуш'))
        tech_markup.add(telebot.types.InlineKeyboardButton(text = 'Мелирование', callback_data = 'Мелирование'))
        tech_markup.add(telebot.types.InlineKeyboardButton(text = 'Растяжка и тонирование', callback_data = 'Растяжка и тонирование'))
        tech_markup.add(telebot.types.InlineKeyboardButton(text = 'Абсолютное счастье для волос', callback_data = 'Абсолютное счастье для волос'))
        tech_markup.add(telebot.types.InlineKeyboardButton(text = 'Керопластика Paul Mitchel', callback_data = 'Керопластика Paul Mitchel'))
        tech_markup.add(telebot.types.InlineKeyboardButton(text = 'Ламинирование', callback_data = 'Ламинирование'))
        tech_markup.add(telebot.types.InlineKeyboardButton(text = 'Fabuloso', callback_data = 'Fabuloso'))
        tech_markup.add(telebot.types.InlineKeyboardButton(text = 'Я не могу самостоятельно выбрать',  url = "telegram.me/Eksprovokator"))

        return tech_markup

    def hair_length(self, message):
        length_markup = telebot.types.InlineKeyboardMarkup()

        length_markup.add(telebot.types.InlineKeyboardButton(text = 'Короткие', callback_data = 'short'))
        length_markup.add(telebot.types.InlineKeyboardButton(text = 'Средние', callback_data = 'middle'))
        length_markup.add(telebot.types.InlineKeyboardButton(text = 'Длинные', callback_data = 'long'))
        length_markup.add(telebot.types.InlineKeyboardButton(text = 'Вернуться в главное меню', callback_data = 'menu'))
        return length_markup

    def master_category(self, message):
        master_markup = telebot.types.InlineKeyboardMarkup()
        master_markup.add(telebot.types.InlineKeyboardButton(text = 'Ведущие колористы', callback_data = 'leaders'))
        master_markup.add(telebot.types.InlineKeyboardButton(text = 'Мастера стилисты', callback_data = 'masters'))
        return master_markup

    def contacts(self, message):
        contacts_markup = telebot.types.InlineKeyboardMarkup()
        contacts_markup.add( telebot.types.InlineKeyboardButton(text = 'Instagram', url = config.instagram_site))
        contacts_markup.add(telebot.types.InlineKeyboardButton(text = 'Наш сайт', url = config.main_site))
        return contacts_markup

    def enroll(self,message):
        master_markup = telebot.types.InlineKeyboardMarkup()
        master_markup.add(telebot.types.InlineKeyboardButton(text = 'Наш администратор в Telegram', url = config.telegram_site))

        return master_markup

    def examples(self,message):
        master_markup = telebot.types.InlineKeyboardMarkup()
        master_markup.add(telebot.types.InlineKeyboardButton(text = 'Instagram', url =  config.instagram_site))
        master_markup.add(telebot.types.InlineKeyboardButton(text = 'Наш сайт', url = config.main_site))
        return master_markup

    def main_menu(self, message):
        menu_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        menu_markup.row("Узнать стоимость окрашивания на свои волосы")
        menu_markup.row("Записаться")
        menu_markup.row("Примеры наших работ")
        menu_markup.row("Контакты")

        return menu_markup
