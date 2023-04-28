# bot.py
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

# from notion_bot.handlers.start_handler import start
# from notion_bot.handlers.authorize_handler import authorize
# from notion_bot.handlers.process_input_handler import process_input
# from notion_bot.handlers.callback_query_handler import handle_callback

app = FastAPI()

# Initialize your bot and dispatcher
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = Bot(token=bot_token)
dp = Dispatcher(bot, None)

# Register handlers
dp.add_handler(CommandHandler("start", start))
# dp.add_handler(MessageHandler(Filters.text & ~Filters.command, authorize))
# dp.add_handler(MessageHandler(Filters.text & ~Filters.command, process_input))
# dp.add_handler(CallbackQueryHandler(handle_callback))

# Error handling (if needed)
# ...

# Webhook route
@app.post("/webhook")
async def webhook(request: Request):
    update = Update.de_json(await request.json(), bot)
    dp.process_update(update)
    return JSONResponse(content={})

def main():
    # Set the webhook
    bot.set_webhook(url=os.environ.get("WEBHOOK_URL"))

    # Run the server using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

if __name__ == "__main__":
    main()
