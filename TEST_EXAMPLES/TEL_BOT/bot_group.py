import random

from config import token
import telebot
from bs4 import BeautifulSoup as bs
import requests

bot = telebot.TeleBot(token)
name = ''
spisok_films = []


def spisok_500():
    global spisok_films
    if len(spisok_films) == 0:
        for i in range(1, 2):
            response_get = requests.get(f'https://www.kinopoisk.ru/lists/movies/top500/?page={i}')
            soup = bs(response_get.text, features='html.parser')
            quotes_film = soup.find_all('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj')
            for film in quotes_film:
                spisok_films.append(film.text)
        return random.choice(spisok_films)
    else:
        return random.choice(spisok_films)


@bot.message_handler(commands=['start'])
def start_com(message):
    poem = 'Приветствуем в нашем боте!!!\nКак тебя зовут?'
    bot.send_message(message.chat.id, poem)
    bot.register_next_step_handler(message, reg_name)


@bot.message_handler(commands=['help'])
def help_com(message):
    help_text = '''
    "Для того чтобы начать введите команду /pusk" \
    "Для получения помощи введите команду /help" \
    "Для того чтобы заново запустить бота введите /start" \
    "При работе с ботом используйте клавиатуру, которая появится после отправки команды pusk"
    '''
    bot.send_message(message.chat.id, help_text)


def keyboard_pusk():
    keyb_markup = telebot.types.ReplyKeyboardMarkup()
    button_genre = telebot.types.KeyboardButton('Жанры фильмов')
    button_rand_popular = telebot.types.KeyboardButton('Случайный фильм из популярного')
    button_rand_500 = telebot.types.KeyboardButton('Случайный фильм из 500 лучших')
    keyb_markup.row(button_genre)
    keyb_markup.row(button_rand_popular)
    keyb_markup.row(button_rand_500)
    return keyb_markup


def keyboard_genre():
    keyb_genre_reply = telebot.types.InlineKeyboardMarkup()
    key_comedy = telebot.types.InlineKeyboardButton(text='Комедии', callback_data='comedy')
    key_mult = telebot.types.InlineKeyboardButton(text='Мультфильмы', callback_data='mult')
    key_fantasy = telebot.types.InlineKeyboardButton(text='Фэнтези', callback_data='fantasy')
    key_horror = telebot.types.InlineKeyboardButton(text='Ужасы', callback_data='horror')
    keyb_genre_reply.add(key_comedy, key_mult, key_fantasy, key_horror)
    return keyb_genre_reply


@bot.message_handler(commands=['pusk'])
def pusk_com(message):
    bot.send_message(message.chat.id, 'Поехали!', reply_markup=keyboard_pusk())


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, f'Приятно познакомиться {name} \nЧтобы начать отправь /pusk\n'
                                      f'Если тебе нужна помощь, то отправь /help')


@bot.message_handler(content_types=['text'])
def genre_repl(message):
    if message.text == 'Жанры фильмов':
        bot.send_message(message.chat.id, 'Выберите один из жанров:', reply_markup=keyboard_genre())
    if message.text == 'Случайный фильм из популярного':
        pass
    if message.text == 'Случайный фильм из 500 лучших':
        bot.send_message(message.chat.id, spisok_500())


@bot.callback_query_handler(func=lambda call: True)
def genre_reply_but(call):
    if call.data == 'comedy':
        bot.send_message(call.message.chat.id, 'Вы выбрали Комедии')
    if call.data == 'mult':
        bot.send_message(call.message.chat.id, 'Вы выбрали Мультфильмы')
    if call.data == 'fantasy':
        bot.send_message(call.message.chat.id, 'Вы выбрали Фэнтези')
    if call.data == 'horror':
        bot.send_message(call.message.chat.id, 'Вы выбрали Ужасы')


bot.polling()
