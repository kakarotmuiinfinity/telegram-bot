from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Bot token from Koyeb environment variable
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Telegram bot setup
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot. How can I assist you?")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))

    # Run polling in a separate thread
    import threading
    bot_thread = threading.Thread(target=application.run_polling)
    bot_thread.start()

# Flask route to keep it running on port 8000
@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=8000)
