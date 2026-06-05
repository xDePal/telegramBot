import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

_ = load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Just echo func
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(text)


# Func to run the bot
def run_bot():
    if not TOKEN:
        raise ValueError("Token is missing")

    app = Application.builder().token(TOKEN).build()

    # This catches EVERYTHING except commands like /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is locked and loaded!")
    app.run_polling()