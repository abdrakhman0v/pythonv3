import telebot
from telebot import types
from datetime import datetime


bot = telebot.TeleBot('7297092697:AAGXVOVy1j3bv9_tgtMkkoaax3RcZFRHMxU')

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('📅 Расписание по дням', callback_data='schedule'))
    markup.add(types.InlineKeyboardButton('💃 Направления (по возрасту и стилю)', callback_data='directions_styles'))
    markup.add(types.InlineKeyboardButton('📝 Записаться на пробный урок', callback_data='trial-lesson'))
    markup.add(types.InlineKeyboardButton('📍 Адрес и контакты', callback_data='adress_contacts'))
    markup.add(types.InlineKeyboardButton('❓ Частые вопросы', callback_data='questions'))
    bot.send_message(message.chat.id,
        '👋 Добро пожаловать в студию танца и фитнеса <b>KGDance</b>!\n\n'
        'Мы рады, что вы с нами 💃\n\n'
        'Выберите, что вас интересует:',
        parse_mode='HTML',
        reply_markup=markup)

# HELP COMMAND
bot.message_handler(commands=['help'])
def help_command(message):
    ...


# -----------Главное меню---------------
@bot.callback_query_handler(func=lambda call:call.data == 'menu')
def menu(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('📅 Расписание по дням', callback_data='schedule'))
    markup.add(types.InlineKeyboardButton('💃 Направления (по возрасту и стилю)', callback_data='directions_styles'))
    markup.add(types.InlineKeyboardButton('📝 Записаться на пробный урок', callback_data='trial-lesson'))
    markup.add(types.InlineKeyboardButton('📍 Адрес и контакты', callback_data='adress_contacts'))
    markup.add(types.InlineKeyboardButton('❓ Частые вопросы', callback_data='questions'))
    
    bot.edit_message_text(
        text = 'Выберите, что вас интересует:',
        chat_id = call.message.chat.id,
        message_id = call.message.message_id,
        parse_mode='HTML',
        reply_markup=markup)
   
#-----------------РАСПИСАНИЕ-------------------
@bot.callback_query_handler(func=lambda call:call.data == 'schedule')
def handle_days(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Пн / Ср / Пт',callback_data='mon_wed_fri'))
    markup.add(types.InlineKeyboardButton('Вт / Чт / Сб',callback_data='tue_thu_sat'))
    markup.add(types.InlineKeyboardButton('Сб / Вс',callback_data='sat_sun'))
    markup.add(types.InlineKeyboardButton('⬅️ Главное меню', callback_data='menu'))

    bot.edit_message_text(
        text = 'Выбери день, чтобы посмотреть расписание',
        chat_id = call.message.chat.id,
        message_id = call.message.message_id,
        reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call:call.data in ['mon_wed_fri','tue_thu_sat','sat_sun'])
def view_schedule(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Записаться',callback_data='trial-lesson'))
    markup.row(
        types.InlineKeyboardButton('⬅️ Назад', callback_data='schedule'),
        types.InlineKeyboardButton('⬅️ Главное меню', callback_data='menu'),
        )
    if call.data == 'mon_wed_fri':
        text = (
            "📅 Расписание на Пн / Ср / Пт:\n\n"
            "🕗 08:00 — Танец живота (14–70+ лет)\n"
            "🕘 09:00 — Народные танцы (7–10 лет)\n"
            "🕙 10:00 — ЛФК (лечебная физ-ра) (7-18 лет)\n"
            "🕚 11:00 — Гимнастика (7–10 лет)\n"
            "🕛 12:00 — Детская хореография (4–6 лет)\n"
            "🕔 17:00 — Детская хореография (4–6 лет)\n"
            "🕕 18:10 — Зумба + Фитнес (14–70+ лет)"
        )
        bot.edit_message_text(chat_id = call.message.chat.id,
                              message_id = call.message.message_id,
                              text = text,
                              reply_markup=markup)
    elif call.data == 'tue_thu_sat':
        text = (
        "📅 Вт / Чт / Сб\n\n"
        "🕗 08:00 — Йога + Фитнес (14–70+ лет)\n"
        "🕘 09:00 — Народные танцы (12–18 лет)\n"
        "🕙 10:00 — Современные танцы (7–18 лет)\n"
        "🕚 11:00 — ЛФК (4–6 лет)\n"
        "🕛 12:00 — Бэби (2–4 года)\n"
        "🕜 13:30 — Функц. трен. + Интимная гимнастика (14–70+ лет)\n"
        "🕔 17:00 — Народные танцы (7–11 лет)\n"
        "🕕 18:00 — High Heels (14–50 лет)\n"
        "🕖 19:00 — Танец живота (14–70 лет)\n"
        "🕗 20:00 — Эрофит (18–70 лет)"
    )
        bot.edit_message_text(chat_id = call.message.chat.id,
                              message_id = call.message.message_id,
                              text = text,
                              reply_markup=markup)
    elif call.data == 'sat_sun':    
        text = (
        "📅 Суббота / Воскресенье\n\n"
        "🕧 12:30 — Детская хореография"
    )
        bot.edit_message_text(chat_id = call.message.chat.id,
                              message_id = call.message.message_id,
                              text = text,
                              reply_markup=markup)
    
    
#------------------НАПРАВЛЕНИЯ---------------------
@bot.callback_query_handler(func=lambda call: call.data == 'directions_styles')
def handle_directions(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('👶 Дети (2–6 лет)', callback_data = 'baby'))
    markup.add(types.InlineKeyboardButton('🧒 Дети (7–12 лет)', callback_data = 'childs'))
    markup.add(types.InlineKeyboardButton('🧑‍🎓 Подростки (12–18)', callback_data = 'teens'))
    markup.add(types.InlineKeyboardButton('👩 Взрослые (18+)', callback_data = 'adults'))
    markup.add(types.InlineKeyboardButton('⬅️ Главное меню', callback_data='menu'))
    
    bot.edit_message_text(
        text = 'Выбирите категорию возраста:',
        chat_id = call.message.chat.id,
        message_id = call.message.message_id,
        reply_markup = markup)
    
@bot.callback_query_handler(func=lambda call:call.data in ['baby','childs','teens','adults'])
def handler_age(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посмотреть расписание', callback_data='schedule'))
    markup.add(types.InlineKeyboardButton('Записаться',callback_data='trial-lesson'))
    markup.row(
        types.InlineKeyboardButton('⬅️ Назад', callback_data='directions_styles'),
        types.InlineKeyboardButton('⬅️ Главное меню', callback_data='menu'),
        )

    if call.data == 'baby':
        text = (
            '👶 Дети (2–6 лет)\n\n'
            '— ЛФК\n'
            '— Детская хореография\n'
            '— Бейби\n'
        )
        bot.edit_message_text(chat_id = call.message.chat.id,
                              message_id = call.message.message_id,
                              text = text,
                              reply_markup=markup)
    elif call.data == 'childs':
        text = (
            '🧒 Дети (7–12 лет\n\n'
            '— Гимнастика\n'
            '— Народные танцы\n'
            '— Современные танцы'
        )
        bot.edit_message_text(chat_id = call.message.chat.id,
                              message_id = call.message.message_id,
                              text = text,
                              reply_markup=markup)
    elif call.data == 'teens':
        text = (
            '🧑‍🎓 Подростки (12–18)\n\n'
            '— Народные танцы\n'
            '— Современные танцы\n'
            '— High heels\n'
        )
        bot.edit_message_text(chat_id = call.message.chat.id,
                              message_id = call.message.message_id,
                              text = text,
                              reply_markup=markup)
    elif call.data == 'adults':
        text = (
            '👩 Взрослые (18+)\n\n'
            '— Танец живота\n'
            '— Зумба\n'
            '— Фитнес\n'
            '— Йога\n'
            '— High heels\n'
            '— Интимная гимнастика\n'
            '— Функциональные тренировки\n'
            '— Эрофит'
        )
        bot.edit_message_text(chat_id = call.message.chat.id,
                              message_id = call.message.message_id,
                              text = text,
                              reply_markup=markup)



# -------------------ЗАПИСЬ НА ПРОБНЫЙ УРОК---------------------

user_data = {}

@bot.callback_query_handler(func=lambda call: call.data == 'trial-lesson')
def start_trial_lesson(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton('Для себя', callback_data = 'for_me'),
        types.InlineKeyboardButton('Для ребенка', callback_data = 'for_child')
    )
    markup.add(types.InlineKeyboardButton('⬅️ Главное меню', callback_data = 'menu'))

    bot.edit_message_text(
        text = '❓ Для себя или для ребенка?',
        chat_id = call.message.chat.id,
        message_id = call.message.message_id,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data in ['for_me','for_child'])
def age_handler(call):
    markup = types.InlineKeyboardMarkup()

    if call.data == 'for_me':
        markup.add(types.InlineKeyboardButton('🧑‍🎓 Подростки (12–18)', callback_data = 'trial-lesson-teenS'))
        markup.add(types.InlineKeyboardButton('👩 Взрослые (18+)', callback_data = 'trial-lesson-adults'))
        markup.row(
            types.InlineKeyboardButton('⬅️ Назад', callback_data = 'trial-lesson'),
            types.InlineKeyboardButton('⬅️ Главное меню', callback_data = 'menu')
            )
        
        bot.edit_message_text(
            text = 'Укажите категорию вашего возраста:',
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = markup
        )
    elif call.data == 'for_child':
        markup.add(types.InlineKeyboardButton('👶 Дети (2–6 лет)', callback_data = 'trial-lesson-baby'))
        markup.add(types.InlineKeyboardButton('🧒 Дети (7–12 лет)', callback_data = 'trial-lesson-childs'))
        markup.add(types.InlineKeyboardButton('🧑‍🎓 Подростки (12–18)', callback_data = 'trial-lesson-teens'))
        markup.row(
            types.InlineKeyboardButton('⬅️ Назад', callback_data = 'trial-lesson'),
            types.InlineKeyboardButton('⬅️ Главное меню', callback_data = 'menu')
            )
        
        bot.edit_message_text(
            text = 'Укажите категорию возраста ребенка:',
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = markup
        )

@bot.callback_query_handler(func = lambda call: call.data.startswith('trial-lesson-'))
def directions_handler(call):
    markup = types.InlineKeyboardMarkup()

    if call.data == 'trial-lesson-baby':
        markup.add(types.InlineKeyboardButton('ЛФК', callback_data = 'sign_up-LFK'))
        markup.add(types.InlineKeyboardButton('Детская хореография', callback_data = 'sign_up-kids_chor'))
        markup.add(types.InlineKeyboardButton('Бейби', callback_data = 'sign_up-baby_chor'))
        markup.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'for_child'))

        bot.edit_message_text(
            text = 'Выберите направление, которое вас интересует:',
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = markup
        )

    elif call.data == 'trial-lesson-childs':
        markup.add(types.InlineKeyboardButton('Гимнастика', callback_data = 'sign_up-gimnastika'))
        markup.add(types.InlineKeyboardButton('Народыне танцы', callback_data = 'sign_up-folk'))
        markup.add(types.InlineKeyboardButton('Современные танцы', callback_data = 'sign_up-modern'))
        markup.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'for_child'))

        bot.edit_message_text(
            text = 'Выберите направление, которое вас интересует:',
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = markup
        )

    elif call.data == 'trial-lesson-teens':
        markup.add(types.InlineKeyboardButton('Народные танцы', callback_data = 'sign_up-folk'))
        markup.add(types.InlineKeyboardButton('Современные танцы', callback_data = 'sign_up-modern'))
        markup.add(types.InlineKeyboardButton('High heels', callback_data = 'sign_up-high-heels'))
        markup.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'for_me'))

        bot.edit_message_text(
            text = 'Выберите направление, которое вас интересует:',
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = markup
        )

    elif call.data == 'trial-lesson-teenS':
        markup.add(types.InlineKeyboardButton('Народные танцы', callback_data = 'sign_up-folk'))
        markup.add(types.InlineKeyboardButton('Современные танцы', callback_data = 'sign_up-modern'))
        markup.add(types.InlineKeyboardButton('High heels', callback_data = 'sign_up-high-heels'))
        markup.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'for_me'))

        bot.edit_message_text(
            text = 'Выберите направление, которое вас интересует:',
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = markup
        )

    elif call.data == 'trial-lesson-adults':
        markup.add(types.InlineKeyboardButton('Танец живота', callback_data = 'sign_up-belly_dance'))
        markup.add(types.InlineKeyboardButton('Зумба', callback_data = 'sign_up-zumba'))
        markup.add(types.InlineKeyboardButton('High heels', callback_data = 'sign_up-high-heels'))
        markup.add(types.InlineKeyboardButton('Фитнес', callback_data = 'sign_up-fitnes'))
        markup.add(types.InlineKeyboardButton('Йога', callback_data = 'sign_up-yoga'))
        markup.add(types.InlineKeyboardButton('Интимная гимнастика', callback_data = 'sign_up-intim-gimnastika'))
        markup.add(types.InlineKeyboardButton('Функциональные тренировки', callback_data = 'sign_up-func-train'))
        markup.add(types.InlineKeyboardButton('Эрофит', callback_data = 'sign_up-erofit'))
        markup.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'for_me'))

        bot.edit_message_text(
            text = 'Выберите направление, которое вас интересует:',
            chat_id = call.message.chat.id,
            message_id = call.message.message_id,
            reply_markup = markup
        )

@bot.callback_query_handler(func=lambda call: call.data.startswith('sign_up-'))
def ask_name(call):
    if call.message.chat.id in user_data:
        bot.answer_callback_query(call.id, text='Вы уже начали запись ⏳')
        return

    user_data[call.message.chat.id] = {
        'direction':call.data,
    }
    msg = bot.send_message(call.message.chat.id,
                     'Введите ваше имя:')
    bot.register_next_step_handler(msg, get_name)

def get_name(message):
    user_data[message.chat.id]['name'] = message.text
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn_phone = types.KeyboardButton(text='📞 Отправить номер', request_contact=True)
    markup.add(btn_phone)
    msg = bot.send_message(message.chat.id,
                     'Отправьте или введите номер телефона:',
                     reply_markup=markup)
    markup = types.ReplyKeyboardRemove()
    bot.register_next_step_handler(msg, get_phone)


def get_phone(message):
    if message.contact and message.contact.phone_number:
        phone = message.contact.phone_number
    else:
        phone = message.text.strip()

    user_data[message.chat.id]['phone'] = phone
    user_data[message.chat.id]['user_name'] = message.from_user.username or '—'
    user_data[message.chat.id]['timestamp'] = datetime.now().strftime('%H:%M %d-%m-Y')

    name = user_data[message.chat.id]['name']
    direction = user_data[message.chat.id]['direction']

    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton('Да, верно', callback_data='yes'),
        types.InlineKeyboardButton('Нет, не верно', callback_data='sign-up-')
    )
    bot.send_message(message.chat.id,
                     f'✅ Заявка получена!\n\n'
                     f'👤 Имя: {name}\n'
                    #  f'🔗 Имя пользователя: {user_name}\n'
                     f'📱 Телефон: {phone}\n'
                     f'🕺 Направление: {direction}\n',
                     reply_markup = markup
                     )
    

# Функция для отправки записи
@bot.callback_query_handler(func = lambda call: call.data == 'yes')
def notify_manager(call):
    data = user_data.get(call.message.chat.id)

    if not data:
        bot.answer_callback_query(call.id, text='❗️Что-то пошло не так, начните сначала.')
        return

    text = (
        f"📥 <b>Новая заявка на пробный урок!</b>\n\n"
        f"👤 Имя: {data['name']}\n"
        f"📱 Телефон: {data['phone']}\n"
        f"🕺 Направление: {data['direction']}\n"
        f"👤 Username: @{data['user_name']}\n"
        f"🕒 Время: {data['timestamp']}"
    )

    bot.send_message(-4755887401, text, parse_mode='HTML')  # Группа или админ
    bot.send_message(call.message.chat.id, "✅ Спасибо! Ваша заявка отправлена. Мы свяжемся с вами в ближайшее время.")
    user_data.pop(call.message.chat.id, None)
    
                     


# user_data = {}

# @bot.callback_query_handler(func=lambda call: call.data == 'trial-lesson')
# def start_trial_lesson(call):
#     chat_id = call.message.chat.id

#     if chat_id in user_data:
#         bot.answer_callback_query(call.id, text='Вы уже начали запись ⏳')
#         return

#     user_data[chat_id] = {}
#     bot.send_message(chat_id, "Как вас зовут?")
#     bot.register_next_step_handler(call.message, get_name)

# def get_name(message):
#     chat_id = message.chat.id
#     user_data[chat_id]['name'] = message.text.strip()
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
#     button_phone = types.KeyboardButton(text='📞 Отправить номер', request_contact=True)
#     markup.add(button_phone)
#     bot.send_message(chat_id, "Пожалуйста, отправьте или введите ваш номер телефона:", reply_markup=markup)
#     bot.register_next_step_handler(message, get_phone)

# def get_phone(message):
#     chat_id = message.chat.id
#     if message.contact and message.contact.phone_number:
#         phone = message.contact.phone_number
#     else:  
#         phone = message.text.strip()
    
#     if not phone.startswith('+996') or not phone[1:].isdigit() or len(phone) != 13:
#         bot.send_message(chat_id, "❗️Номер должен начинаться с +996 и содержать 13 символов. Попробуйте снова:")
#         bot.register_next_step_handler(message, get_phone)
#         return
#     user_data[chat_id]['phone'] = phone

#     markup = types.ReplyKeyboardRemove()
#     
#     bot.send_message(chat_id, "Какое направление вас интересует?",
#                      reply_markup=markup_age)
#     bot.register_next_step_handler(message, get_direction)

# def get_direction(message):
#     chat_id = message.chat.id
#     user_data[chat_id]['direction'] = message.text.strip()
#     user_data[chat_id]['timestamp'] = datetime.now().strftime('%H:%M %d-%m-%Y')
#     user_data[chat_id]['username'] = message.from_user.username or '—'
    
#     notify_manager(user_data[chat_id])
#     bot.send_message(chat_id, "✅ Спасибо! Ваша заявка отправлена. Мы свяжемся с вами в ближайшее время.")

#     # Очистка
#     user_data.pop(chat_id, None)





#---------------АДРЕС И КОНТАКТЫ------------------
@bot.callback_query_handler(func=lambda call:call.data == 'adress_contacts')
def adress_contacts(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('⬅️ Главное меню', callback_data='menu'))
    text = (
           "<b>📍 Адрес:</b>\n"
        "🏢 ул. Токтогула 259, г. Каракол\n"
        "🧭 Ориентир: 2 этаж, здание банка «Capital» (бывшее кафе «Караван»)\n\n"
        
        "<b>📞 Контакты:</b>\n"
        "☎️ +996 704 490 100\n"
        "☎️ +996 704 335 430\n"
        "📲 WhatsApp: +996 550 245 254\n"
        "📸 Instagram: <a href='https://www.instagram.com/kgdance_karakol/'>@kgdance_karakol</a>\n\n"
        
        "<b>🕒 График работы:</b>\n"
        "Пн–Сб: 08:00 – 20:00\n"
        "Вс: 12:00 – 14:00"
    )

    bot.edit_message_text(
        text = text,
        chat_id = call.message.chat.id,
        message_id = call.message.message_id,
        parse_mode='HTML',
        reply_markup=markup)
    
#-------------------ЧАСТЫЕ ВОПРОСЫ------------------
questions = {
    'Вопрос 1': 'Ответ 1',
    'Вопрос 2': 'Ответ 2',
    'Вопрос 3': 'Ответ 3',
    'Вопрос 4': 'Ответ 4',
    'Вопрос 5': 'Ответ 5',
}

@bot.callback_query_handler(func=lambda call: call.data == 'questions')
def show_questions(call):
    markup = types.InlineKeyboardMarkup()
    for i, q in enumerate(questions.keys()):
        markup.add(types.InlineKeyboardButton(f'❓ {q}', callback_data=f'que_{i}'))
    markup.add(types.InlineKeyboardButton('⬅️ Главное меню', callback_data='menu'))

    bot.edit_message_text(chat_id = call.message.chat.id,
                          message_id=call.message.message_id,
                          text = '🧠 <b>Часто задаваемые вопросы:</b>\n\nВыберите интересующий вас вопрос:',
                          parse_mode = 'HTML',
                          reply_markup = markup)
    
@bot.callback_query_handler(func=lambda call: call.data.startswith('que_'))
def answer_questions(call):
    q_index = int(call.data.split('_')[1])
    question = list(questions.keys())[q_index]
    answer = questions[question]

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Назад к вопросам', callback_data = 'questions'))
    markup.add(types.InlineKeyboardButton('Главнео меню', callback_data = 'menu'))
    
    bot.edit_message_text(
        chat_id = call.message.chat.id,
        message_id = call.message.message_id,
        text = f'<b>❓ {question}</b>\n\n— {answer}',
        parse_mode = 'HTML',
        reply_markup=markup
    )

bot.polling(non_stop=True)