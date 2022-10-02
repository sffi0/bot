import telebot
import time

bot = telebot.TeleBot('5193435427:AAEZB6s2JsMFKBZ2CWuCrnvcM5BY-WWupZ4')
CHANNEL_NAME = '@neodigitalmarketing'
f = open('jokes.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()

for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    time.sleep(60)

bot.send_message(CHANNEL_NAME, "Чет я устал шутехи шутить, дальше сами")

bot.polling(none_stop=True, interval=0)