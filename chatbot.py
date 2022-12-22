import telegram
bot = telegram.Bot(token='TOKEN')
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='TOKEN', use_context=True) 
dispatcher = updater.dispatcher
def hey(update, context):
    context.Bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')
hey_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hey_handler)
updater.start_polling()
