# Import necessary libraries
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Enable logging for easier debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your bot. Type /help to see what I can do.")

# Define the /help command
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Here are the commands you can use:\n/start - Start the bot\n/help - Get help")

# Define an example command, like /info
def info_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("This is a simple Telegram bot created to help you learn Python.")

# Main function to start the bot
def main() -> None:
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
    updater = Updater("YOUR_BOT_TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers to handle each command
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("info", info_command))

    # Start the bot
    updater.start_polling()

    # Run the bot until you stop it with Ctrl+C
    updater.idle()

# Run the main function if this script is executed
if __name__ == '__main__':
    main()
  
