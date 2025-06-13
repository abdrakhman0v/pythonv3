import telebot
from telebot import types
from datetime import datetime


MANAGER_ID = 825411310

bot = telebot.TeleBot('7297092697:AAGXVOVy1j3bv9_tgtMkkoaax3RcZFRHMxU')

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Хочу консультацию!',callback_data='consultation'))
    markup.add(types.InlineKeyboardButton('Хочу записаться на пробный урок!',callback_data='trial_lesson'))
    markup.add(types.InlineKeyboardButton('Хочу купить абонемент!',callback_data='subscription'))
    markup.add(types.InlineKeyboardButton('Хочу устроиться к вам!',callback_data='get_job'))
    bot.send_message(message.chat.id,
'Здравствуйте! Это танцевальная студия танца и фитнеса <b>"KGDance"!</b>\nЧем могу быть полезен?',
parse_mode='HTML',reply_markup=markup)
    

#-----------ФУНКЦИЯ ДЛЯ ОТПРАВКИ ЗАПИСИ---------
def notify_manager(data):
    text = f"""
    📥<b>Новая запись:</b>
    👤Имя: {data.get('name', '-')}
    🧑‍💻Username: @{data.get('username', '-')}
    📘Направление: {data.get('direction', '-')}
    🕒Время записи: {data.get('timestamp', '-')}
"""
    bot.send_message(MANAGER_ID,text,parse_mode='HTML')




#--------------------Консультация---------------------
@bot.callback_query_handler(func=lambda call:call.data == 'consultation')
def handle_consultation(call):
    bot.send_message(call.message.chat.id, 
                     '<b>Танцевальная студия танца и фитнеса KGDance - принимает от 4-х до 70-и лет.</b>\n\n<b>Дети от 4 до 6 лет:</b>\n- Гимнастика\n- Ритмика\n- Танцы всех направлений\n- ЛФК\n\n<b>Подростки от 7 до 18лет:</b>\n- Гимнастика\n- Танцы всех направлений\n- ЛФК\n\n<b>Взрослые от 14 до 70 лет:</b>\n- Фитнес\n- Йога\n- High heels\n- Зумба\n- Интимная гимнастика\n- Танец живота\n- Индивидуальные занятия\n- Постановка свадебных танцев, выпускного вальса, флешмоба\n- Принимаем заказы на ваши торжества (свадьбы, корпоративы т.д.)\n\n<b>Контактные данные: 0550245254; 0702661131\nАдрес: ул.Токтогула/Жусаева б/н 2-этаж(бывшее кафе "Караван")</b>',
                     parse_mode='HTML')
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton('Хочу записаться на пробный урок!', callback_data='trial_lesson'),
        types.InlineKeyboardButton('Хочу купить абонемент!',callback_data='subscription'),
    )
    bot.send_message(call.message.chat.id, 'Хотите записаться на пробный урок или же купить абонемент?',
                     reply_markup=markup)


# -------------------Пробный урок---------------------
@bot.callback_query_handler(func=lambda call:call.data == 'trial_lesson')
def handle_trial_lesson(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton('Для себя', callback_data='for_me'),
        types.InlineKeyboardButton('Для ребенка', callback_data='for_child')
    )
    bot.send_message(call.message.chat.id, 
                     'Понял! Вам нужно для себя или для ребенка?',
                     reply_markup=markup)

#ДЛЯ СЕБЯ
@bot.callback_query_handler(func=lambda call:call.data == 'for_me')
def handle_for_me(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton('Фитнес', callback_data='fitnes'),
        types.InlineKeyboardButton('Зумба', callback_data='zumba'),
    )
    markup.row(
        types.InlineKeyboardButton('Хай-хилс', callback_data='high-heels'),
        types.InlineKeyboardButton('Танец живота', callback_data='belly_dance'),
    )
    markup.row(
        types.InlineKeyboardButton('Йога', callback_data='yoga'),
        types.InlineKeyboardButton('Интимная гимнастика', callback_data='intimate_gym'),
    )
    bot.send_message(call.message.chat.id,
                     'Отлично! Выберите направление:',
                     reply_markup=markup)
    
# @bot.add_callback_query_handler(func=lambda call: call.data in ['fitnes','zumba','high-heels','belly_dance','yoga','intimate_gym'])
# def handle_adult(call):


#ДЛЯ РЕБЕНКА

@bot.callback_query_handler(func=lambda call:call.data == 'for_child')
def handle_for_child(call):
    bot.send_message(call.message.chat.id, 
                     'Отлично! Введите возраст ребенка:')
    bot.register_next_step_handler(call.message, handle_child_age)

def handle_child_age(message):
    try:
        age = int(message.text)
        if age in [2,3]:
            bot.send_message(message.chat.id, "Для вашего ребенка подходит группа 'Baby'\nРасписание:\nПн Ср Пт в 17:30")
        elif age in [4,5,6]:
            bot.send_message(message.chat.id, "Для вашего ребенка подходит группа 'Дети'\nРасписание:\nПн Ср Пт в 17:30\nСб Вс 12:30")
        elif age in range(7,13):
            bot.send_message(message.chat.id, "Для вашего ребенка есть группы:")
        elif age in range(13,19):
            bot.send_message(message.chat.id, "Для вашего ребенка есть группы:")
        else:
            bot.send_message(message.chat.id, 'Уточните возраст ребенка - доступные группы от 2 до 18 лет')
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите возраст числом')
    
    
bot.polling(non_stop=True)