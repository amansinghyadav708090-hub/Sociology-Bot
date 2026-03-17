import os
import logging
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ---------------- LOGGING ----------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ---------------- TOKEN ----------------
TOKEN = "8608967851:AAE5heiMgTXWR7kqfgekaAfsOyZLNdDqjqo"

# ---------------- TELEGRAM COMMANDS ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Hello!\n\n"
        "This is *The Sociology Bot* 📚\n\n"
        "Use /help to see commands.",
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Available Commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show commands\n"
        "/about - About this bot"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 The Sociology Bot\n\n"
        "Designed for NET & CUET PG Sociology preparation."
    )

# ---------------- TELEGRAM BOT ----------------
def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))

    print("🚀 Telegram bot started")

    app.run_polling()

# ---------------- FLASK SERVER ----------------
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot is running successfully!"

# ---------------- MAIN ----------------
if __name__ == "__main__":
    bot_thread = Thread(target=run_bot)
    bot_thread.start()

    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port)
