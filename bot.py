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

# Flask route to keep it running on port 8000
@app.route("/")
def home():
    return "Bot is running"

# Main entry point
if __name__ == "__main__":
    # Create and set a new event loop if one does not exist
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # Schedule the bot to run in the created event loop
    loop.create_task(run_bot())

    # Run the Flask app on port 8000
    app.run(host="0.0.0.0", port=8000)
    
