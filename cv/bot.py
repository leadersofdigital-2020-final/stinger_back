from .config import token
import telebot
from telebot import types # кнопки
from string import Template
from .serializers import CVSerializer

bot = telebot.TeleBot(token)

_keys = ['profession', 'full_name', 'schedule', 'employment', 
            'education', 'salary', 'experience', 'skills', 
            'achievements', 'expectations', 'add_info', 'feedback']
_dict = dict.fromkeys(_keys)


_from_bot = ''

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    itembtn1 = types.KeyboardButton('Давай знакомиться')
    itembtn2 = types.KeyboardButton('Пройти собеседование')

    markup.add(itembtn1, itembtn2)
    
    bot.send_message(message.chat.id, "Привет "
    + message.from_user.first_name
    + ":) Мы рады, что такой талантливый человек заинтересовался работой у нас. Давай познакомимся и поймем, насколько подходим друг другу?", reply_markup=markup)

def user_reg(message):
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    
    itembtn1 = types.KeyboardButton('Python-разработчик')
    itembtn2 = types.KeyboardButton('Go-разработчик')
    itembtn3 = types.KeyboardButton('Java-разработчик')

    markup.add(itembtn1, itembtn2, itembtn3)
       

    msg = bot.send_message(message.chat.id, 'Вас заинтересовала позиция', reply_markup=markup)
    bot.register_next_step_handler(msg, process_achievements_step)


def process_achievements_step(message):
        
    chat_id = message.chat.id
    dict['profession'] = message.text


    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    fivetwo = types.KeyboardButton('5/2')
    twotwo = types.KeyboardButton('2/2')
    flexfourthy = types.KeyboardButton('гибкий 40 часов')
    flextwenty = types.KeyboardButton('гибкий 20 часов')
    markup.add(fivetwo, twotwo, flexfourthy, flextwenty)


    msg = bot.send_message(chat_id, 'Какой график для вас самый комфортный?', reply_markup=markup)
    bot.register_next_step_handler(msg, process_phone_step)


def process_phone_step(message):
    # int(message.text)

    chat_id = message.chat.id
    _dict['schedule'] = message.text

    msg = bot.send_message(chat_id, 'Напишите, какое у вас образование: учебное заведение и специализация?')
    bot.register_next_step_handler(msg, process_salary_step)



def process_salary_step(message):
    
    chat_id = message.chat.id
    _dict['education'] = message.text
       
    msg = bot.send_message(chat_id, 'Укажите желаемый размер заработной платы')
    bot.register_next_step_handler(msg, process_experience_step)


def process_experience_step(message):
    
    chat_id = message.chat.id
    _dict['salary'] = message.text

    msg = bot.send_message(chat_id, 'Расскажите о своем опыте работы: где работали, кем, сколько времени?')
    bot.register_next_step_handler(msg, process_skills_step)


def process_skills_step(message):
    
    chat_id = message.chat.id
    _dict['experience'] = message.text

    msg = bot.send_message(chat_id, 'Выделите свои ключевые навыки, компетенции, которыми вы обладаете?')
    bot.register_next_step_handler(msg, process_add_info_step)


def process_add_info_step(message):
    
    chat_id = message.chat.id
    _dict['skills'] = message.text

    msg = bot.send_message(chat_id, 'Воу, воу, воу, да вы крутой специалист!;)  Напиши свои главные достижения/результаты на прошлых местах работы/учебы?')
    bot.register_next_step_handler(msg, process_expectations_step)



def process_expectations_step(message):
    
    chat_id = message.chat.id
    _dict['achievements'] = message.text

    msg = bot.send_message(chat_id, 'Отлично, мы почти на финише;) Опишите идеальные условия работы для вас? Что вам важно в работе/работодателе?')
    bot.register_next_step_handler(msg, process_feedback_step)


def process_feedback_step(message):
    
    chat_id = message.chat.id
    # _dict['feedback'] = message.text

    bot.send_message(chat_id, 'Спасибо за оставленную заявку, наш HR-специалист свяжется с вами')

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True) 

    one = types.KeyboardButton('1.12')
    three = types.KeyboardButton('3.12')
    four = types.KeyboardButton('4.12')

    markup.add(one, three, four)
    msg = bot.send_message(chat_id, 'Мы готовы провести с вами финальное собеседование. В какую дату вам удобно?', reply_markup=markup)
    bot.register_next_step_handler(msg, process_time_step)
        # print(_dict)


def process_time_step(message):
    
    chat_id = message.chat.id
        # _dict['interview_date'] = message.text

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True) 

    one = types.KeyboardButton('9:00-12:00')
    three = types.KeyboardButton('13:00-16:00')
    four = types.KeyboardButton('18:00-20:00')

    markup.add(one, three, four)
    msg = bot.send_message(chat_id, 'А в какой промежуток времени?', reply_markup=markup)
    bot.register_next_step_handler(msg, process_end_step)

    serializers = CVSerializer(data=_dict)
    if (serializers.is_valid()):
        serializers.save()


def process_end_step(message):

    chat_id = message.chat.id
    _dict['feedback'] = message.text

    bot.send_message(chat_id, 'Очень скоро вам позвонит ваш будущий коллега;)')

# def getRegData(user, title, name):
#     print(_dict)


def send_about(message):
	bot.send_message(message.chat.id, 
    """
    Мы разрабатываем и поддерживаем собственные мобильные приложения для B2B и B2C, которыми пользуемся мы сами, а также большое число наших клиентов и обычных пользователей.
    Мы ищем Python разработчиков, способных реализовывать от идеи до “продакшна” крупные проекты по:
    Разработке и поддержке существующего функционала по выдаче ЭП. Результатом вашей работы будут пользоваться более 1,5 миллиона людей – на компьютерах, планшетах и смартфонах.
    Мы не работаем под заказ, мы создаем тиражные продукты. Используемый стек технологий: C++, Python, PostgreSQL, Javascript, NodeJS, Redis, ElasticSearch, Clickhouse. Вам не нужно знать буквально все наши технологии. Нужна светлая голова и страстное желание работать. Делать лучший продукт в России.

    Мы предлагаем:
    интересную работу в крупной и стабильной IT-компании;
    заработную плату в зависимости от квалификации и уровня ответственности;
    оформление по ТК РФ;
    премии от 5 до 20% по итогам работы за месяц
    социальные гарантии;
    корпоративное обучение;
    возможности профессионального и карьерного роста, курсы иностранных языков;
    корпоративные праздники и различные совместные мероприятия.)
    """)

@bot.message_handler(content_types=["text"])
def send_video(message):
    bot.send_message(message.chat_id, 'Ваши ответы увидит руководитель и даст обратную связь')

@bot.message_handler(content_types=["text"])
def send_help(message):
    if message.text == "Давай знакомиться":
        send_about(message)
    elif message.text == 'Пройти собеседование':
        user_reg(message)
    else:
        _from_bot = message.text
        print(_from_bot)
        # bot.send_message(message.chat.id, 'О нас - /about\nРегистрация - /reg\nПомощь - /help')

# @bot.message_handler(content_types=["video"])


@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, 'Напишите текст')

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

def get_interview():
    bot.polling() 

if __name__ == '__main__':
    bot.polling(none_stop=True)