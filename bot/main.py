import telebot 
import wikipedia

bot = telebot.TeleBot('8135757275:AAHx-sI8Q68kD8iH44_eAuE967DZg02nhdA')

wikipedia.set_lang('ru')

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1, button2)


@bot.message_handler(commands=['start', 'hello'])
def start_message(message):
    msg = bot.send_message(message.chat.id,'Привет, отправь мне слово и я найду информацию в википедии.')
    bot.register_next_step_handler(msg, answer)


def answer(message):
    try:
        text = wikipedia.page(message.text)
        info_text = text.content[:1000]
        result = info_text.split('. ')
        result.pop()
        result = '. '.join(result) + '.'
        bot.send_message(message.chat.id, result,reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Хотите продолжить?')
    except:
        bot.send_message(message.chat.id,'Ничего не найдено по данному запросу.')

@bot.message_handler(content_types=['text'])
def check(message):
    if message.text == 'Да':
        msg = bot.send_message(message.chat.id, 'Хорошо введи слово',
                               reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, answer)
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'До свидания!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        
    else:
        bot.send_message(message.chat.id, 'Нажите на кнопку!')

bot.polling(non_stop=True, interval=0)