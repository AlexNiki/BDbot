import telebot
import psycopg2

# main variables
TOKEN = "1661150170:AAFxO9tIQlwpSB0QgJzgkHjQjBUP_jiylEM"
bot = telebot.TeleBot(TOKEN)

SQLALCHEMY_DATABASE_URI = 'postgresql://rc1b-zyki2np4f2xdinrv.mdb.yandexcloud.net'

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, я предосталяю информацию о днях рождениях!')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text
    chat_id = message.chat.id

    conn = psycopg2.connect("""
        host=rc1b-zyki2np4f2xdinrv.mdb.yandexcloud.net
        port=6432
        sslmode=verify-full
        dbname=hbd-bot
        user=av-nikiforov
        password=Pozitiv123
        target_session_attrs=read-write
    """)

    q = conn.cursor()
    q.execute('SELECT version()')
    bot.send_message(message.chat.id, q.fetchone())
    conn.close()

bot.polling()
