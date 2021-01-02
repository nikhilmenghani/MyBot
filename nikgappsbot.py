#!/usr/bin/env python

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, run_async
from telegram.message import Message
from telegram.message import Document

# Enable logging
import Config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

all_user_data = dict()


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    # update.message.reply_text("Operation Complete on Server", reply_to_message_id=update.message.message_id)
    print(str(update.message.from_user.id) + " " + str(update.message.text))
    message = "Hi there,\n" \
              "As I am in growing phase, at the moment, I understand following commands\n\n" \
              "/fetch <package> \n\n" \
              "Try and send /fetch basic # this will fetch basic packages on server\n" \
              "Supported package names are core, basic, omni, macro, stock or full"
    sent_message = context.bot.send_message(chat_id=update.message.chat_id, text=message,
                                            reply_to_message_id=update.message.message_id)


def help(update, context):
    # print(type(update.message))
    result = authorize(update)
    if result:
        """Send a message when the command /help is issued."""
        update.message.reply_text(text=update.message, reply_to_message_id=update.message.message_id)


def echo(update, context):
    """Echo the user message."""
    # str_msg = update.message.reply_to_message.text
    result = authorize(update)
    if result:
        """Send a message when the command /help is issued."""
        update.message.reply_text(text=update.message.text, reply_to_message_id=update.message.message_id)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def authorize(update):
    authorized_id = ["390478637"]
    if str(update.message.from_user.id) in authorized_id :
        return True
    else:
        update.message.reply_text("You're not authorized!", reply_to_message_id=update.message.message_id)
        return False


def main():
    """Start the bot."""
    updater = Updater(Config.TOKEN, workers=8, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start, run_async=True))
    dp.add_handler(CommandHandler("help", help, run_async=True))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo, run_async=True))
    dp.add_handler(MessageHandler(Filters.document, echo, run_async=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
