import telebot
from config import *


bot = telebot.TeleBot(config.TOKEN)
bot.set_update_listener(listener) # register listener

@bot.message_handler(commands=['soff'])
def screenoff(message):
	bot.reply_to(message, "Screen off")

@bot.message_handler(commands=['on'])
def screenon(message):
	bot.reply_to(message, "Screen on")

bot.polling()