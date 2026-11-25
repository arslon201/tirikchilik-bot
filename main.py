from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from callbacks import add_callback, lang_callback, start, text_handler
from settings import BOT_TOKEN


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(lang_callback, pattern="^lang:"))
    app.add_handler(CallbackQueryHandler(add_callback, pattern="^add:"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    print("Bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()