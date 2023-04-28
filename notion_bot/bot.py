# bot.py
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

# from notion_bot.handlers.start_handler import start
# from notion_bot.handlers.authorize_handler import authorize
# from notion_bot.handlers.process_input_handler import process_input
# from notion_bot.handlers.callback_query_handler import handle_callback

def main():
    # Replace with your own telegram-bot token
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")

    updater = Updater(bot_token)
    dp = updater.dispatcher

    # Register handlers
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, authorize))
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, process_input))
    # dp.add_handler(CallbackQueryHandler(handle_callback))

    # Error handling (if needed)
    # ...

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
