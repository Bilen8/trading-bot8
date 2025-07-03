from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = "8175464094:AAGrcsWYvy-ORV6ZBDMngB1zbaL9AAEpCWg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📡 Daily Quotes", callback_data='daily_quotes')],
        [InlineKeyboardButton("📊 Results", callback_data='results')],
        [InlineKeyboardButton("💎 Join VIP", callback_data='join_vip')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    chat_id = update.effective_chat.id

    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://i.ibb.co/Jjv62Vsy/Chat-GPT-Image-23-2025-23-54-01.png",
        caption=(
            "Main Menu\n\n"
            "Welcome to SSFX Bot — your access point to daily signals, results, and elite trading motivation.\n\n"
            "Here you’ll find:\n\n"
            "🔹 Daily trading quotes\n"
            "🔹 Live trading session results\n"
            "🔹 Top platforms to start trading\n"
            "🔹 Access to the VIP group\n\n"
            "Let’s take your trading to the next level. 🏁"
        ),
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'daily_quotes':
        await query.edit_message_text(text="📡 Here are your daily trading quotes!")
    elif data == 'results':
        await query.edit_message_text(text="📊 Here are the live trading session results!")
    elif data == 'join_vip':
        await query.edit_message_text(
            text="💎 Join our VIP group here: [VIP Link](https://t.me/joinchat/example)",
            parse_mode='Markdown'
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot started...")
    app.run_polling()
