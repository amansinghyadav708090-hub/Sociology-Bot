import logging
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8608967851:AAE5heiMgTXWR7kqfgekaAfsOyZLNdDqjqo"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ---------------- BOT ---------------- #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! The Sociology Bot is working.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /start to test the bot.")

def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

# ---------------- WEB SERVER (Render needs this) ---------------- #

web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Sociology Bot is running!"

def run_web():
    web_app.run(host="0.0.0.0", port=10000)

# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    Thread(target=run_bot).start()
    run_web()
