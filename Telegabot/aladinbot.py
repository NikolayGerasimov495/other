#pip3 install pyTelegramBotAPI

# Подключаем библиотеку
import telebot

# Здесь нужно вставить токен, который дал BotFather при регистрации
# Пример: token = '2007628239:AAEF4ZVqLiRKG7j49EC4vaRwXjJ6DN6xng8'
token = '6459780143:AAFliKWuovDnb03P6hegHLkjXj4SKQ8Z7LU'  # <<< Ваш токен

# В этой строчке мы заводим бота и даем ему запомнить токен
bot = telebot.TeleBot(token)

# Пишем первую функцию, которая отвечает "Привет" на команду /start
# Все функции общения приложения с ТГ спрятаны в функции под @
@bot.message_handler(commands=['start'])
def say_hi(message):
    bot.send_message(message.chat.id, 'Привет')

# Запускаем бота. Он будет работать до тех пор, пока работает ячейка
# (крутится значок слева).
# Остановим ячейку - остановится бот
bot.polling()