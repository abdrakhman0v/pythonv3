import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup as bs

bot = telebot.TeleBot('7728899922:AAFIc1qPkRT1wOjutDFZqkE2HsjL5W-e6v0')

enumerate_news = []
@bot.message_handler(commands=['start'])
def start_parser(message):
    URL = 'https://kaktus.media/?lable=8&date=2025-06-13&order=time'

    response = requests.get(URL)
    html = response.text
    soup = bs(html, 'lxml')

    news = soup.find_all('div', class_='ArticleItem')

    enumerate_news.clear() 

    for new in news[:20]:
        description = new.find('a', class_='ArticleItem--name').text.strip()
        image = new.find('img').get('src')

        enumerate_news.append({
            'description':description,
            'image':image
        })
    
    bot.send_message(message.chat.id,
                     'Введите "Новости" для просмотра новостей.')

@bot.message_handler(content_types=['text'])
def user_input(message):
    if message.text.lower() == 'новости':
        markup = types.InlineKeyboardMarkup()
        for i, news in enumerate(enumerate_news):
            btn = types.InlineKeyboardButton(text =f"{i+1}. {news['description'][:30]}...", callback_data= str(i))
            markup.add(btn)
        bot.send_message(message.chat.id,
                         'Выберите новость:',
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         'Неправильный ввод. Попробуйте ещё раз!')
                
@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def handle_news(call):
    news_index = int(call.data)
    news = enumerate_news[news_index]

    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton('Описание', callback_data=f'desc_{news_index}'),
        types.InlineKeyboardButton('Фото', callback_data=f'photo_{news_index}'),
               )
    bot.send_message(call.message.chat.id, 
                     'Вы можете посмотреть описание этой новости и фото.',
                     reply_markup=markup)
    
@bot.callback_query_handler(func= lambda call: call.data.startswith('desc_') or call.data.startswith('photo_'))
def send_detail(call):
    index = int(call.data.split('_')[1])
    news = enumerate_news[index]

    if call.data.startswith('desc_'):
        bot.send_message(call.message.chat.id,
                     f"📰 {news['description']}")
    elif call.data.startswith('photo_'):
        bot.send_photo(call.message.chat.id,
                       news['image'])
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Выйти", callback_data='quit'))
    bot.send_message(call.message.chat.id,
                     'Желаете выйти?',
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'quit')
def quit(call):
    bot.send_message(call.message.chat.id,
                     'До свидания!')

bot.polling(non_stop=True)
        
