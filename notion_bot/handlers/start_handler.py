# handlers/start_handler.py
from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    welcome_message = "Welcome! Please authorize by sending your Notion API token."
    update.message.reply_text(welcome_message)