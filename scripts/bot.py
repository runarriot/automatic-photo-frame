#!/usr/bin/python
import subprocess
import shlex
import telebot
import json

with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['telegram.TOKEN']
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['status'])
def screenoff(message):
		bot.reply_to(message, "photo delay: " + config["shideshow.delay"] )
		bot.reply_to(message, "random: " + config["shideshow.random"] )


@bot.message_handler(commands=['soff'])
def screenoff(message):
		subprocess.call(shlex.split('./test.sh param1 param2'))
		bot.reply_to(message, "Screen is off")

@bot.message_handler(commands=['on'])
def screenon(message):
        bot.reply_to(message, "Screen on")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)



bot.polling()
