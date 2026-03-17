import logging
import asyncio
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8608967851:AAE5heiMgTXWR7kqfgekaAfsOyZLNdDqjqo"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! The Sociology Bot is running 📚")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/start\n/help")

async def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot started...")
    await app.run_polling()

web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Sociology Bot running"

def run_web():
    web_app.run(host="0.0.0.0", port=10000)

async def main():
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, run_web)
    await run_bot()

if __name__ == "__main__":
    asyncio.run(main())
