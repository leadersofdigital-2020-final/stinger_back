import config
import telebot
from telebot import types # кнопки
from string import Template
from serializers import CVSerializer

bot = telebot.TeleBot(config.token)

user_dict = {}

_keys = ['profession', 'full_name', 'schedule', 'employment', 
            'education', 'salary', 'experience', 'skills', 
            'achievements', 'expectations', 'add_info', 'feedback']
_dict = dict.fromkeys(_keys)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    itembtn1 = types.KeyboardButton('/about')
    itembtn2 = types.KeyboardButton('/reg')

    markup.add(itembtn1, itembtn2)
    
    bot.send_message(message.chat.id, "Здравствуйте "
    + message.from_user.first_name
    + ", я бот, чтобы вы хотели узнать?", reply_markup=markup)

@bot.message_handler(commands=['about'])
def send_about(message):
	bot.send_message(message.chat.id, "Мы надежная компания" 
    + " company. 10 лет на рынке.")


@bot.message_handler(commands=["reg"])
def user_reg(message):
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    
    itembtn1 = types.KeyboardButton('Python-разработчик')
    itembtn2 = types.KeyboardButton('Go-разработчик')
    itembtn3 = types.KeyboardButton('Java-разработчик')

    markup.add(itembtn1, itembtn2, itembtn3)
       

    msg = bot.send_message(message.chat.id, 'Вакансия', reply_markup=markup)
    bot.register_next_step_handler(msg, process_city_step)


def process_city_step(message):
    try:
        chat_id = message.chat.id
        # user_dict[chat_id] = User(message.text)
        _dict['proffession'] = message.text

        print(_dict)
        
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'ФИО', reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)

        print(_dict)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        _dict['full_name'] = message.text

        msg = bot.send_message(chat_id, 'Ваш номер телефона')
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_phone_step(message):
    # int(message.text)

    chat_id = message.chat.id
    _dict['phone'] = message.text

    msg = bot.send_message(chat_id, 'Введите номер телефона для связи')
    bot.register_next_step_handler(msg, process_employment_step)

    # except Exception as e:
    #     msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
    #     bot.register_next_step_handler(msg, process_phone_step)

def process_employment_step(message):
    try:
        chat_id = message.chat.id
        _dict['employment'] = message.text

        msg = bot.send_message(chat_id, 'Частичная или полная занятость')
        bot.register_next_step_handler(msg, process_salary_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_salary_step(message):
    try:
        chat_id = message.chat.id
        _dict['salary'] = message.text
       
        msg = bot.send_message(chat_id, 'Зарплата')
        bot.register_next_step_handler(msg, process_experience_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_experience_step(message):
    try:
        chat_id = message.chat.id
        _dict['experience'] = message.text

        msg = bot.send_message(chat_id, 'Опыт работы в формате 1г 2м')
        bot.register_next_step_handler(msg, process_skills_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_skills_step(message):
    try:
        chat_id = message.chat.id
        _dict['skills'] = message.text

        msg = bot.send_message(chat_id, 'Навыки')
        bot.register_next_step_handler(msg, process_achievements_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_achievements_step(message):
    try:
        
        chat_id = message.chat.id
        _dict['achievements'] = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        fivetwo = types.KeyboardButton('5/2')
        twotwo = types.KeyboardButton('2/2')
        flexfourthy = types.KeyboardButton('гибкий 40 часов')
        flextwenty = types.KeyboardButton('гибкий 20 часов')
        markup.add(fivetwo, twotwo, flexfourthy, flextwenty)


        msg = bot.send_message(chat_id, 'График работы', reply_markup=markup)
        bot.register_next_step_handler(msg, process_expectations_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_expectations_step(message):
    try:
        chat_id = message.chat.id
        _dict['expectations'] = message.text

        msg = bot.send_message(chat_id, 'Ожидания от работы')
        bot.register_next_step_handler(msg, process_add_info_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_add_info_step(message):
    try:
        chat_id = message.chat.id
        _dict['add_info'] = message.text

        msg = bot.send_message(chat_id, 'Дополнительная информация')
        bot.register_next_step_handler(msg, process_feedback_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_feedback_step(message):
    try:
        chat_id = message.chat.id
        _dict['feedback'] = message.text

        print(_dict)

        serializers = TodoSerializer(data=_dict)
        if (serializers.is_valid()):
            serializers.save()
        
    except Exception as e:
        bot.reply_to(message, 'ooops!!')

# def getRegData(user, title, name):
#     print(_dict)

# произвольный текст
@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'О нас - /about\nРегистрация - /reg\nПомощь - /help')

# произвольное фото
@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, 'Напишите текст')

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)