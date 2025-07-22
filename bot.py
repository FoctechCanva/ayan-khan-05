import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise Exception("❌ BOT_TOKEN not set. Please check your .env file.")

# Define buttons and links
channel_links = [
    "https://t.me/channel1",
    "https://t.me/channel2",
    "https://t.me/channel3",
    "https://t.me/channel4",
    "https://t.me/channel5",
    "https://t.me/channel6",
]
claim_link = "https://t.me/claim_now"

# Create the inline keyboard layout
keyboard = [
    [InlineKeyboardButton("Join Now", url=link)] for link in channel_links
]
keyboard.append([InlineKeyboardButton("🎁 Claim Now", url=claim_link)])
reply_markup = InlineKeyboardMarkup(keyboard)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("promo.jpg", "rb") as image_file:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=image_file,
            caption="🚀 Join All Channels Below & Claim Your Reward 🎁",
            reply_markup=reply_markup
        )

# Run the bot
async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
