import telebot

# main variables
TOKEN = "1661150170:AAFxO9tIQlwpSB0QgJzgkHjQjBUP_jiylEM"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет c ВМ яндекса')


bot.polling()
