import telebot
import os
import schedule
import time
from time import sleep
from threading import Thread

from creds import TOKEN

bot = telebot.TeleBot(TOKEN)
birthdayFile = script_dir = os.path.dirname(__file__) + '/res/bd16.txt'

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, я предосталяю информацию о днях рождениях!')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text
    chat_id = message.chat.id

    fileName = open(birthdayFile, 'r', encoding="utf-16")
    flag = 0
    for line in fileName:
        if text in line:
            line = line.split(';')
            flag = 1
            msg = line[0] + ' ' + line[1]
            bot.send_message(message.chat.id, msg)
    if flag == 0:
        bot.send_message(message.chat.id, 'Ничего не найдено')


def check_birthday():
    today = time.strftime('%d') + '.' + time.strftime('%m')
    fileName = open(birthdayFile, 'r', encoding="utf-16")
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(';')
            flag = 1
            msg = line[0] + ' ' + line[1]
            bot.send_message('462203157', msg)
    if flag == 0:
        bot.send_message('462203157', 'Сегодня дней рождений нет')

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

if __name__ == "__main__":
    schedule.every().day.at("07:00").do(check_birthday)
    Thread(target=schedule_checker).start()

bot.polling()
