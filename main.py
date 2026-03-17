import logging
import asyncio
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8608967851:AAE5heiMgTXWR7kqfgekaAfsOyZLNdDqjqo"

logging.basicConfig(level=logging.INFO)

# -------- TELEGRAM COMMAND --------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Sociology Bot is working 📚")

# -------- BOT FUNCTION --------
def run_bot():
    async def bot():
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        print("Bot started...")
        await app.run_polling()

    asyncio.run(bot())

# -------- WEB SERVER --------
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Sociology Bot is running!"

# -------- MAIN --------
if __name__ == "__main__":
    Thread(target=run_bot).start()
    web_app.run(host="0.0.0.0", port=10000)
