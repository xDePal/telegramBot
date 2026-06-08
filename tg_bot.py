import os
import re
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters
from vector_search import search
from llm import rewrite_chain, answer_chain

_ = load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Чем могу помочь?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    print(query)

    # Rewrite query
    rewritten = rewrite_chain.invoke({"query": query})
    rewritten_query = re.sub(r"<think>.*?</think>", "", rewritten.content, flags=re.DOTALL).strip()
    print(rewritten_query)

    # Vector search with rewritten query
    context_text = search(rewritten_query)

    # Answer with original query + context
    response = answer_chain.invoke({"query": query, "context": context_text})
    clean = re.sub(r"<think>.*?</think>", "", response.content, flags=re.DOTALL).strip()

    await update.message.reply_text(clean)

def run_bot():
    if not TOKEN:
        raise ValueError("Token is missing")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is locked and loaded!")
    app.run_polling()