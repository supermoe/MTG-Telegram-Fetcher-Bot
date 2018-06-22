from telegram.ext import Updater
import telegram
import logging
from auth import *
from get import fetch_card
from telegram.ext import CommandHandler

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Urza is now active in this chat. Use \"/card <card name>\" to fetch a card's information.")

def card(bot, update, args):
	if len(args) > 0:
		#card input
		result = fetch_card(" ".join(args))
		if result['success']:
			bot.send_photo(chat_id=update.message.chat_id, photo=result['card']['img'], caption="[" + result['card']['name'] + "](" + result['card']['link'] + ")", parse_mode=telegram.ParseMode.MARKDOWN, disable_notification=True)
		else:
			bot.send_message(chat_id=update.message.chat_id, text=result['details'], disable_notification=True)
	else:
		#no args
		update.message.reply_text("A card's name is required for this command to work.", disable_notification=True)

updater = Updater(token)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
start_handler = CommandHandler('start', start)
card_handler = CommandHandler('card', card, pass_args=True)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(card_handler)
updater.start_polling()
print("start")