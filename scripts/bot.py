#!/usr/bin/python
import subprocess
import json
import telebot

with open('config.json', 'r') as f:
    conf = json.load(f)

TOKEN = conf['TOKEN']
bot = telebot.TeleBot(TOKEN)


def get_command(text):
    return text.split()[0]

def get_params(text):
    return text.replace(get_command(text)+' ', '')


@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "photo delay: " + conf["delay"])
    bot.reply_to(message, "random: " + conf["random"])


#screen on
@bot.message_handler(commands=['on'])
def screenon(message):
    env = {
        "DISPLAY": ":0",
    }
    subprocess.Popen('../commands/screen.sh auto', env=env).wait()
    bot.reply_to(message, "Screen on")

#screen off
@bot.message_handler(commands=['off'])
def screenoff(message):
    env = {
        "DISPLAY": ":0",
    }
    subprocess.Popen('../commands/screen.sh off', env=env).wait()
    bot.reply_to(message, "Screen off")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    command = get_command(message.text)
    params = get_params(message.text)
    if command == "show":
        subprocess.Popen('../commands/slideshow.sh ').wait()
    else:
        if command == "refreshdb":
            cmd = "../commands/refreshdb.sh '" + params + ", " + conf["dbfile"]
            subprocess.Popen(cmd).wait()
            bot.reply_to(message, "Db refresh done.")
    bot.reply_to(message, "Command: " + command + "\nParams: " + params)

bot.polling()
