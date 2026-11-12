
import os
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if update.message is None:
        return

    await update.message.reply_text(
        "🎬 <b>Welcome to Staxler Movie Library!</b> 🍿\n\n"
        "Hi there! We're happy to have you here.\n\n"
        "Explore and search your favourite movies "
        "and series in <b>Malayalam</b> and <b>English</b>.\n\n"
        "✨ Use <code>/help</code> to view all "
        "available commands.",
        parse_mode=ParseMode.HTML,
    )

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "🎬 Welcome to Staxler Movie Library!\n\n"
        "/start - Start the bot\n"
        "/help - Show help"
    )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is missing!")

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    print("Staxler Movie Library Bot is running!")
    application.run_polling()

if __name__ == "__main__":
    main()
