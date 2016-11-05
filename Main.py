#!/usr/bin/env python3

from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
import telegram
import sys
from joke import give_blc, give_joke
import locale
from eat import newEat, eatCallback
from roomcommand import RoomCommand
from todolist import give_todo
from loghelper import log
from confighelper import ConfigHelper

locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

conf = ConfigHelper(sys.argv[1])
updater = Updater(token=conf.get_anastasia_key())
dispatcher = updater.dispatcher

room = RoomCommand(log, conf.path_ics())

start_handler = CommandHandler('room', room.give_room)
joke_handler = CommandHandler('joke', give_joke)
blc_handler = CommandHandler('blc', give_blc)
todo_handler = CommandHandler('todo', give_todo, pass_args=True)
keskonmange_handler = CommandHandler('keskonmange', newEat)
callback_handler = CallbackQueryHandler(eatCallback)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(blc_handler)
dispatcher.add_handler(todo_handler)
dispatcher.add_handler(keskonmange_handler)
dispatcher.add_handler(callback_handler)

updater.start_polling()
