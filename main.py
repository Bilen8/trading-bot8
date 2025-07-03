from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random

TOKEN = "8175464094:AAGrcsWYvy-ORV6ZBDMngB1zbaL9AAEpCWg"

QUOTES = [
    "💬 “Risk comes from not knowing what you’re doing.”\n— Warren Buffett",
    "💬 “Even the most cautious man must sometimes take risks—unless he wants to remain a small-time speculator forever.”\n— Edwin Lefèvre",
    "💬 “The goal of a successful trader is to make the best trades. Money is secondary.”\n— Alexander Elder",
    "💬 “If you can't control your emotions, you can't control your money.”\n— Warren Buffett",
    "💬 “Remember, your goal is to trade well, not to trade often.”\n— Alexander Elder",
    "💬 “It's not whether you're right or wrong that matters, but how much you make when you're right and how much you lose when you're wrong.”\n— George Soros",
    "💬 “I never argue with the market. You can get mad at it, but it won’t do you any good.”\n— Jesse Livermore",
    "💬 “The purpose of trading is not to guess up or down, but to win.”\n— Jesse Livermore",
    "💬 “The most important quality for an investor is temperament, not intellect.”\n— Warren Buffett",
    "💬 “When people say they want to be a millionaire, what they usually mean is, 'I want to spend a million,' which is the opposite.”\n— Morgan Housel",
    "💬 “Risk only what you can afford to lose—but enough to make a win meaningful.”\n— Edward Seykota",
    "💬 “The market is like the ocean—its waves rise and fall regardless of your wishes.”\n— Alexander Elder",
    "💬 “One key lesson: true understanding of the market comes gradually, as you begin to rely more on yourself.”\n— Mark Douglas",
    "💬 “Michael Marcus taught me: Make decisions, make mistakes, make another decision. That’s how you grow your capital.”\n— Bruce Kovner",
    "💬 “When I lose in the market, I walk away. Staying leads to bad decisions driven by emotions.”\n— Randy McKay",
    "💬 “I always define my risk, so I don’t have to worry about it.”\n— Tony Saliba",
    "💬 “If a position moves against me, I get out. If it works, I hold. Risk management is everything.”\n— Paul Tudor Jones",
    "💬 “Over the years, I’ve learned that stepping away from the market often brings more clarity and better results.”\n— Martin Schwartz",
    "💬 “If a stock doesn’t act right, don’t touch it. No diagnosis—no forecast. No forecast—no profit.”\n— Jesse Livermore",
    "💬 “Start small. If it works, build the position.”\n— George Soros",
    "💬 “To make money, you need to act. To make big money, you need to act at the right time.”\n— Edwin Lefèvre",
    "💬 “Don’t be greedy. If you miss the right price, skip the trade and move on.”\n— Linda Raschke",
    "💬 “I’ve seen little correlation between intelligence and trading success. Emotional control matters far more.”\n— William Eckhardt",
    "💬 “Don’t try to be a hero. The moment you think you’ve figured it all out—you’re in danger.”\n— Paul Tudor Jones",
    "💬 “When you’re losing, reduce size and rebuild confidence step by step.”\n— Bill Lipschutz",
    "💬 “If you want good money—you must learn to wait.”\n— Larry Williams",
    "💬 “The key secret: listen to the market. Don’t impose your will on it.”\n— Linda Raschke",
    "💬 “Accept losses. Keep them small. Don’t increase position sizes until your capital has grown 2–3x.”\n— Martin Schwartz",
    "💬 “The most important thing I learned from Soros: It’s not about being right, it’s about how much you make when you are.”\n— Stanley Druckenmiller",
    "💬 “Once you understand that each trade has equal odds of winning or losing, you stop giving them emotional weight.”\n— Nial Fuller",
    "💬 “Wealthy people don’t bet big every day. They bet smart.”\n— Larry Williams",
    "💬 “Small losses are part of the game. Big losses take you out of it.”\n— Doug Kass",
    "💬 “Keep your positions small enough that fear doesn’t cloud your judgment.”\n— Joe Vidich",
    "💬 “There is no single right way to trade. No strategy works all the time.”\n— Jack Schwager",
    "💬 “Don’t worry about the market. Focus on how you’ll respond to it.”\n— Michael Carr",
    "💬 “It’s safer to be a speculator than an investor—speculators risk what they understand, investors often don’t.”\n— John Maynard Keynes (paraphrased)",
    "💬 “Trading is a psychological game. You’re not fighting the market. You’re fighting yourself.”\n— Martin Schwartz",
    "💬 “Most beginners trade 3–5x more than they should. Risk 1–2%, not 10%.”\n— Bruce Kovner",
    "💬 “Many stocks may seem cheap, but the economy changes everything. Often, the hardest move is to do nothing.”\n— David Tepper",
    "💬 “I’ve made counter-trend trades before, but generally it’s a bad idea.”\n— Richard Dennis",
    "💬 “Never risk more than 1% of your capital per trade. That way, you stay detached and objective.”\n— Larry Hite",
    "💬 “No book, no guru, no strategy will make you profitable. Only time and effort can do that.”\n— Brett Steenbarger",
    "💬 “Patience is the currency of trading. Hold it, and profit will follow.”\n— Trading Wisdom",
    "💬 “Emotions are expensive. Stay calm, stay funded.”\n— Trading Wisdom",
    "💬 “You don’t need to trade every day. You need to trade the right day.”\n— Trading Wisdom",
    "💬 “Discipline beats strategy when emotions take control.”\n— Trading Wisdom",
    "💬 “A missed trade is better than a forced loss.”\n— Trading Wisdom",
    "💬 “Your goal isn’t to win today. Your goal is to survive forever.”\n— Trading Wisdom",
    "💬 “Trade with logic, exit with discipline.”\n— Trading Wisdom",
    "💬 “Every bad trade teaches. Every good trade repeats.”\n— Trading Wisdom",
    "💬 “Chasing the market is like chasing wind. Let it come to you.”\n— Trading Wisdom",
]

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📡 Daily Quotes", callback_data='daily_quotes')],
        [InlineKeyboardButton("📊 Results", callback_data='results')],
        [InlineKeyboardButton("💎 Join VIP", callback_data='join_vip')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    caption_text = (
        "Welcome to SSFX Bot — your access point to daily signals, results, and elite trading motivation.\n\n"
        "Here you’ll find:\n\n"
        "🔹 Daily trading quotes\n"
        "🔹 Live trading session results\n"
        "🔹 Top platforms to start trading\n"
        "🔹 Access to the VIP group\n\n"
        "Let’s take your trading to the next level. 🏁"
    )

    # Отправка стартового фото и текста
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="https://i.ibb.co/Jjv62Vsy/Chat-GPT-Image-23-2025-23-54-01.png",
        caption=caption_text,
        reply_markup=reply_markup
    )

# Обработка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data in ['daily_quotes', 'next_quote']:
        quote = random.choice(QUOTES)
        keyboard = [[InlineKeyboardButton("🔁 Next Quote", callback_data='next_quote')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Отправляем новое сообщение (не редактируем старое)
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text=quote,
            reply_markup=reply_markup
        )

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
