# import telebot
# from io import BytesIO
#
# bot = telebot.TeleBot('5833361798:AAHlLO-qY3fybWRkq3Qop8tRWpZF51AuGqw', parse_mode=None)
#
# def start_image():
#     with open('image.jpeg', 'rb') as file:
#         obj = BytesIO(file.read())
#         obj.name = 'Picture.jpeg'
#         return obj
# @bot.message_handler(content_types=['text'])
# def get_message(message):
#     if message.text == 'Hello':
#         bot.send_message(message.from_user.id, "Hi")
#     elif message.text == 'What are you doing?':
#         bot.send_message(message.from_user.id, "Nothing")
#     elif message.text == 'photo':
#         photo = open('image.jpeg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.from_user.id, "I don't know")
#
# bot.polling(none_stop=True)







                          #Task

import telebot
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()


class MyBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def start_bot(self):

        def start_image():
            with open('image.jpeg', 'rb') as file:
                obj = BytesIO(file.read())
                obj.name = 'Picture.jpg'
                return obj
        @self.bot.message_handler(content_types=['text', 'document', 'number'])
        def get_message(message):
            if message.text.lower() == 'hello':
                self.bot.send_message(message.from_user.id,"Hi")
            elif message.text.lower() == 'hi':
                self.bot.send_message(message.from_user.id, "Hello")
            elif message.text.lower() == "photo":
                 photo = open('Python.png', 'rb')
                 self.bot.send_photo(message.chat.id, photo)
            elif message.text.lower() == "image":
                image = open('logo.png', 'rb')
                self.bot.send_photo(message.chat.id, image)
            else:
                self.bot.send_message(message.chat.id, "I don't know")
        self.bot.polling(none_stop=True)


myBot = MyBot(os.getenv('TOKEN'))
myBot.start_bot()