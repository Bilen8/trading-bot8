import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Обработчики команд
async def start(update: Update, context):
    logger.info("Команда /start от пользователя %s", update.message.from_user.id)
    # Кнопки для выбора
    keyboard = [
        [InlineKeyboardButton("ACTIVE FIN", callback_data='ACTIVE_FIN')],
        [InlineKeyboardButton("ACTIVE OTC", callback_data='ACTIVE_OTC')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Я бот. Выберите действие:', reply_markup=reply_markup)

async def active_fin(update: Update, context):
    logger.info("Пользователь выбрал ACTIVE FIN: %s", update.message.from_user.id)
    await update.message.reply_text('Вы выбрали ACTIVE FIN.')

async def active_otc(update: Update, context):
    logger.info("Пользователь выбрал ACTIVE OTC: %s", update.message.from_user.id)
    await update.message.reply_text('Вы выбрали ACTIVE OTC.')

async def forecast(update: Update, context):
    logger.info("Пользователь выбрал валютную пару: %s", update.message.text)
    await update.message.reply_text('Вы выбрали валютную пару.')

async def reset(update: Update, context):
    logger.info("Пользователь выбрал Сброс: %s", update.message.from_user.id)
    await update.message.reply_text('Сброс. Возвращаемся в главное меню.')

# Обработчик кнопок
async def button(update: Update, context):
    query = update.callback_query
    await query.answer()  # Подтверждаем нажатие кнопки
    if query.data == 'ACTIVE_FIN':
        await query.edit_message_text(text="Вы выбрали ACTIVE FIN.")
    elif query.data == 'ACTIVE_OTC':
        await query.edit_message_text(text="Вы выбрали ACTIVE OTC.")

# Основная функция для запуска бота
def main():
    token = '7932281147:AAFSQnt6gYDEtfreLgNlaJIpRyfpDeK4r9A'  # Замените на свой токен
    application = Application.builder().token(token).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))  # Обрабатывает команду /start
    application.add_handler(MessageHandler(filters.Regex('^ACTIVE FIN$'), active_fin))  # Обрабатывает команду ACTIVE FIN
    application.add_handler(MessageHandler(filters.Regex('^ACTIVE OTC$'), active_otc))  # Обрабатывает команду ACTIVE OTC

    # Обработчик для выбора валютной пары
    application.add_handler(MessageHandler(filters.Regex(r'^(EUR/USD|GBP/USD|USD/JPY|AUD/USD|USD/CHF|Назад)$'), forecast))  # Прогноз для валютных пар

    # Обработчик для кнопки "Сброс"
    application.add_handler(MessageHandler(filters.Regex('^Сброс$'), reset))  # Возвращает в главное меню

    # Обработка callback запросов от кнопок (используем CallbackQueryHandler)
    application.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    logger.info("Запуск бота...")
    application.run_polling()
    logger.info("Бот работает.")

if __name__ == '__main__':
    main()

