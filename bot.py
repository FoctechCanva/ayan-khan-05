import logging
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from os import getenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise Exception("❌ BOT_TOKEN not set. Please check your .env file.")

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Handler for /start command
async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Image path (make sure 'promo.jpg' is in the same folder)
    image_path = "promo.jpg"

    # Caption
    caption = (
        "🔥 Join the best Telegram channels and claim your reward now!\n\n"
        "👇 Click the buttons below 👇"
    )

    # Inline buttons
    buttons = [
        [InlineKeyboardButton("Join Now 1", url="https://t.me/channel1")],
        [InlineKeyboardButton("Join Now 2", url="https://t.me/channel2")],
        [InlineKeyboardButton("Join Now 3", url="https://t.me/channel3")],
        [InlineKeyboardButton("Join Now 4", url="https://t.me/channel4")],
        [InlineKeyboardButton("Join Now 5", url="https://t.me/channel5")],
        [InlineKeyboardButton("Join Now 6", url="https://t.me/channel6")],
        [InlineKeyboardButton("✅ Claim Now", url="https://t.me/claimbot")],
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    # Send image with buttons
    with open(image_path, "rb") as photo:
        await context.bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, reply_markup=reply_markup)

# Main function to start the bot
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot started successfully.")
    await app.run_polling()

# Safe asyncio launch (Render compatible)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "event loop is already running" in str(e):
            loop = asyncio.get_event_loop()
            loop.create_task(main())
            loop.run_forever()
        else:
            raise


