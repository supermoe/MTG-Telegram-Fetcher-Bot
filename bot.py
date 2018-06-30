import telegram
import logging
import random
from auth import *
from get import fetch_card, fetch_inline
from telegram.ext import CommandHandler, CallbackQueryHandler, InlineQueryHandler, Updater
def card(bot, update, args):
	if len(args) > 0:
		#card input
		result = fetch_card(" ".join(args))
		if result['success'] == 0:
			#found
			bot.send_photo(chat_id=update.message.chat_id, photo=result['card']['img'], caption="[" + result['card']['name'] + "](" + result['card']['link'] + ")", parse_mode=telegram.ParseMode.MARKDOWN, disable_notification=True)
		else:
			bot.send_message(chat_id=update.message.chat_id, text=result['details'], disable_notification=True)
	else:
		#no args
		update.message.reply_text("A card's name is required for this command to work.", disable_notification=True)

def inline(bot, update):
	print('received inline query for "' + update.inline_query.query + '"')
	cards = fetch_inline(update.inline_query.query)
	results = [telegram.InlineQueryResultPhoto(
	id=hex(random.getrandbits(64))[2:],
	photo_url=c['full'],
	thumb_url=c['thumb'],
	title='test',
	description='test',
	photo_width=488,
	photo_height=680,
	caption="[" + c['name'] + "](" + c['url'] + ")",
	parse_mode=telegram.ParseMode.MARKDOWN)
	for c in cards]
	bot.answerInlineQuery(update.inline_query.id, results=results)

def reply(bot, update):
	args = [update.callback_query.data]
	card(bot, update.callback_query, args)


updater = Updater(token)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
card_handler = CommandHandler('card', card, pass_args=True)
reply_handler = CallbackQueryHandler(reply)
inline_handler = InlineQueryHandler(inline)
dispatcher.add_handler(reply_handler)
dispatcher.add_handler(card_handler)
dispatcher.add_handler(inline_handler)
updater.start_polling()
print("start")