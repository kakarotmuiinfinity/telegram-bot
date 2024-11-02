from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
import asyncio
import os

# Initialize Flask app
app = Flask(__name__)

# Bot token from Koyeb environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Telegram bot setup
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot. How can I assist you?")

async def run_bot():
    # Create application and add command handler
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))

    # Run the bot until manually stopped
    await application.run_polling()

# Flask route to keep it running on port 8080
@app.route("/")
def home():
    return "Bot is running"

# Main entry point
if __name__ == "__main__":
    # Run the bot in the background in the existing event loop
    loop = asyncio.get_event_loop()
    loop.create_task(run_bot())

    # Start the Flask app on port 8080
    app.run(host="0.0.0.0", port=8080)
