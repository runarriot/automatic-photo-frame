#!/usr/bin/python
import telebot
import cfg

TOKEN = cfg.TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['soff'])
def screenoff(message):
        bot.reply_to(message, "Screen off")

@bot.message_handler(commands=['on'])
def screenon(message):
        bot.reply_to(message, "Screen on")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)



bot.polling()
