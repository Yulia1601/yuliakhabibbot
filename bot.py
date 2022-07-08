import telebot

bot = telebot.TeleBot('5327041930:AAF8rh0LXWv7jmifm7WyGglyby1XGslLNDE')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()