# -*- coding: UTF-8 -*-

from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import api

#import Freezer as fr
#import youtubeplayer as yp -> needs to change the search button
import Freebies as fre #calleble
import article as ar #calleble
import Mcdonalds as mc #calleble
#import check as ch


def MC(bot, update):
    arg = update.message.text.split(" ")[1:]
    text = mc.select(arg)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=text)
    
def AR(bot, update):
    arg = update.message.text.split(" ")[1:]
    text=ar.select(arg)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=text)
    
def YP(bot, update):
    arg = update.message.text.split(" ")[1:]
    arg = " ".join(arg)
    print(arg)
    yp.Player(arg)
    
    
    
def FRE(bot, update):
    arg = update.message.text.split(" ")[1:]
    text=fre.select(arg)
    
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=text)

def Help(bot, update):
    text="This is my bot to control other bots \n Use /mc to use Mcdonalds (use arg fries or drink) \n Use /fre for Freebies \n /yp to play music (add video by arg) \n /ar for articles (select news by arg) \n"
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=text)

def Credits(bot, update):
    text=" Created finally in 2020 by Ridlees"
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=text)



def main():

    updater = Updater(api.api)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('credits',Credits))
    dp.add_handler(CommandHandler('help',Help))
    dp.add_handler(CommandHandler('mc',MC))
    dp.add_handler(CommandHandler('ar',AR)) 
    dp.add_handler(CommandHandler('yp',YP))
    dp.add_handler(CommandHandler('fre',FRE)) 
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
