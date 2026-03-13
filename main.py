from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
from flask import Flask
from threading import Thread
import os

logging.basicConfig(level=logging.INFO)

TOKEN = "7542764200:AAEf2138dCdQ4zYJo9okgPP-WV86EjiomTs"

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running"


def run():
    port = int(os.environ.get("PORT", 8080))
    flask_app.run(host="0.0.0.0", port=port)


def keep_alive():
    t = Thread(target=run)
    t.start()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working!")


if __name__ == "__main__":
    keep_alive()

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot started")

    app.run_polling()
