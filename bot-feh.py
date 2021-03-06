#!/usr/bin/python
import subprocess
import json
import telebot
import requests
import sys, os

pathname = os.path.dirname(sys.argv[0])
path = os.path.abspath(pathname) + '/'
 
#test

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
#    env = {
#        "DISPLAY": ":0",
#    }
#    subprocess.Popen('../commands/screen.sh auto', env=env).wait()
    bot.reply_to(message, "Screen on")

#screen off
@bot.message_handler(commands=['off'])
def screenoff(message):
#    env = {
#        "DISPLAY": ":0",
#    }
#    subprocess.Popen('../commands/screen.sh off', env=env).wait()
    bot.reply_to(message, "Screen off")

@bot.message_handler(content_types=["photo"])
def downloadfile(message):
#    bot.reply_to(message, message.photo[0].file_id)
    file_info = bot.get_file(message.photo[-1].file_id)
    url = 'https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path)
#    bot.reply_to(message,req)
 #   file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
    image_name = str(message.message_id) + '.jpg'
    dst = path + 'upload/' + image_name
    r = requests.get(url, stream=True)
    with open(image_name, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)
    os.rename(path + image_name, path + 'upload/' + image_name)
    cmd = path + "showphoto.sh " + dst
    subprocess.Popen(cmd, env={"DISPLAY":":0"}, shell = True).wait()


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    command = get_command(message.text)
    params = get_params(message.text)
    if command == "show":
	cmd = path + "slideshow.sh " + params
        subprocess.Popen(cmd, env={"DISPLAY":":0"}, shell = True).wait()
    else:
        if command == "refreshdb":
            cmd = path + "refreshdb.sh " + path+"pics/" + " " + path + conf["dbfile"]
            p = subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE).wait()
#            bot.reply_to(message, "Db refresh done.")

bot.polling() 