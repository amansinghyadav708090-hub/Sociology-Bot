from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Paste your NEW token here (from BotFather)
TOKEN = "8608967851:AAGLF3tIJ_ar8J9RKuCDoqv8E7SvzY8-hjg"

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working!")

def main():
    # Build application with concurrent updates for faster responses
    app = ApplicationBuilder().token(TOKEN).concurrent_updates(True).build()

    # Command handler
    app.add_handler(CommandHandler("start", start))

    print("Bot started successfully")

    # Start polling
    app.run_polling()

if __name__ == "__main__":
    main()
