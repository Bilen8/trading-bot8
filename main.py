from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 1. Отправляем заголовок или Ref
    await update.message.reply_text("Main Menu\nRef шага: 1750617010726cf13c4b69")

    # 2. Отправляем картинку по URL (замени на свою ссылку)
    photo_url = "https://example.com/your_image.jpg"  # вставь сюда свою картинку
    await update.message.reply_photo(photo=photo_url, caption="image")

    # 3. Отправляем приветственный текст с кнопками
    keyboard = [
        [InlineKeyboardButton("📡 Daily Quotes", callback_data='daily_quotes')],
        [InlineKeyboardButton("📊 Results", callback_data='results')],
        [InlineKeyboardButton("💎 Join VIP", callback_data='join_vip')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        "Welcome to SSFX Bot — your access point to daily signals, results, and elite trading motivation.\n\n"
        "Here you’ll find:\n"
        "🔹 Daily trading quotes\n"
        "🔹 Live trading session results\n"
        "🔹 Top platforms to start trading\n"
        "🔹 Access to the VIP group\n\n"
        "Let’s take your trading to the next level. 🏁"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

if __name__ == '__main__':
    app = ApplicationBuilder().token("8175464094:AAGrcsWYvy-ORV6ZBDMngB1zbaL9AAEpCWg").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

