import telebot

from EXAMPLES.TEL_BOT.config import token

# TODO import    pip install BeautifulSoup4

mybot = telebot.TeleBot(token)


@mybot.message_handler(commands=['start'])
def start_mess(message):
    mybot.send_message(message.chat.id, 'Привіт... ')


mybot.infinity_polling()
