import telebot
import config
from telebot import types


bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Просмотреть календарь')
    item2 = types.KeyboardButton('Просмотреть задачи')
    item3 = types.KeyboardButton('Личный ToDо лист')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Добро пожаловать в телерам бота WZ Studio, мы рады приветствовать тебя {0.first_name}!\nЯ - Генадий, с любыми вопросами приходи ко мне или пиши кожанным ублюдкам которые создали меня @TumaH7 @Alive_0utside'.format(message.from_user, bot.get_me()), parse_mode="html", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def calendar(message):
    if message.chat.type == 'private':
        if message.text == 'Просмотреть календарь':
            bot.send_message(message.chat.id, "{0.first_name}.\nТвой календарь".format(message.from_user, bot.get_me()),
                             parse_mode="html")
            pho = open('static/Frame 1.png', 'rb')
            bot.send_photo(message.chat.id, pho)
        if message.text == 'Просмотреть задачи':
            bot.send_message(message.chat.id, "{0.first_name}.\nCлушай пока для тебя задач нет".format(message.from_user, bot.get_me()), parse_mode="html")
        if message.text == 'Личный ToDо лист':
            bot.send_message(message.chat.id, '{0.first_name}!\tТвой ToDo лист готов!\nlocalhost:3000'.format(message.from_user, bot.get_me()), parse_mode="html")

bot.polling(none_stop=True)
