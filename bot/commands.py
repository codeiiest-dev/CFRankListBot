from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils import cf, HANDLES_LIST, DATA
import logging

logger = logging.getLogger(__name__)


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    logger.info('Received message: %s', update.message.text)
    update.message.reply_text(update.message.text)


def getrank(update, context):
    """Fetch the latest CF rounds ranking list."""

    if len(context.args) == 0 or not context.args[0].isnumeric():
        update.message.reply_text(
            'Please enter a valid round number contest id. Eg: /getrank 1620')
        return

    contest_id = context.args[0]
    contest_data = cf.get_contest_data(contest_id, HANDLES_LIST)

    if contest_data['status'] == 'OK':
        update.message.reply_text('Done!')
        result = cf.filter_top_participants(contest_data, DATA)
        print(result)
    else:
        logger.error('Error: in fetching %s', contest_data['comment'])
        update.message.reply_text('Error! Codeforces API returned an error.')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def init(token):
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("getrank", getrank))
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
