import telegram
import logging
from auth import *
from get import fetch_card
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

def card(bot, update, args):
	if len(args) > 0:
		#card input
		result = fetch_card(" ".join(args))
		if result['success'] == 0:
			#found one result
			bot.send_photo(chat_id=update.message.chat_id, photo=result['card']['img'], caption="[" + result['card']['name'] + "](" + result['card']['link'] + ")", parse_mode=telegram.ParseMode.MARKDOWN, disable_notification=True)
		elif result['success'] == 1:
			#found multiple results
			list = result['list']
			blist = []
			for b in result['list']:
				blist.append([telegram.InlineKeyboardButton(b, callback_data=b)])
			bot.send_message(chat_id=update.message.chat_id, text="Too many cards match the ambiguous name \"" + result['query'] + "\", which card did you mean to fetch?", disable_notification=True, reply_markup=telegram.InlineKeyboardMarkup(blist))
		else:
			bot.send_message(chat_id=update.message.chat_id, text=result['details'], disable_notification=True)
	else:
		#no args
		update.message.reply_text("A card's name is required for this command to work.", disable_notification=True)

def reply(bot, update):
	args = [update.callback_query.data]
	card(bot, update.callback_query, args)


updater = Updater(token)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
card_handler = CommandHandler('card', card, pass_args=True)
reply_handler = CallbackQueryHandler(reply)
dispatcher.add_handler(reply_handler)
dispatcher.add_handler(card_handler)
updater.start_polling()
print("start")