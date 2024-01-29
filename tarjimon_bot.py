# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:11:43 2024

@author: User
"""
from transliterate import to_cyrillic, to_latin
from googletrans import Translator
import telebot

botapi = '6921859104:AAEeDeMw-NLyidrMZEVxlkmsKg174PuOq7c'
bot = telebot.TeleBot(botapi, parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum, xush kelibsiz! \nSiz buyerda matnlaringizni \
Lotin-Kiril yoki Kiril-Lotinga o'girishingiz, qolaversa google translator orqali \
ingliz rus va o'zbek tillariga tarjima qilishingiz mumkin.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    tarjima = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # if msg.isascii():
    #     tarjima = to_cyrillic(msg)
    # else:
    #     tarjima = to_latin(msg)
    bot.reply_to(message, tarjima(msg))
    
bot.polling()
# matn = input("Matn kiriting: \n>>>")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
# tarjimon = Translator()
# matn = input("Tarjima qilinadigan matnni kiriting: ")
# tarjima = tarjimon.translate(matn, src='uz', dest='en')
# print(tarjima.text)