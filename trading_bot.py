from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters
import yfinance as yf
from datetime import datetime

# Функция для получения прогноза с помощью yfinance
def get_prediction(currency_pair):
    # Формируем тикер для валютной пары (например, для EURUSD)
    pair = yf.Ticker(f"{currency_pair}=X")

    # Получаем последние 5 минутных данных
    data = pair.history(period="1d", interval="5m")

    if data.empty:
        return "Ошибка получения данных. Попробуйте позже."

    # Извлекаем последнюю цену
    latest_data = data.iloc[-1]
    latest_price = latest_data['Close']
    open_price = latest_data['Open']
    high_price = latest_data['High']
    low_price = latest_data['Low']

    # Сравниваем текущую цену с предыдущей для определения тренда
    prev_data = data.iloc[-2]
    prev_price = prev_data['Close']

    # Определяем тренд
    trend = "Вверх" if latest_price > prev_price else "Вниз"

    # Получаем текущее время
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Формируем подробный ответ
    result = f"""
    *Прогноз для {currency_pair}:*

    📅 *Дата и время прогноза:* {current_time}
    💵 *Текущая цена:* {latest_price} USD
    🔴 *Открытие:* {open_price} USD
    🔼 *Максимум:* {high_price} USD
    🔽 *Минимум:* {low_price} USD

    📊 *Тренд:* {trend}

    *Обновление данных:* Данные обновляются каждые 5 минут.
    """
    return result

# Функция для создания клавиатуры с валютными парами
def create_currency_keyboard():
    # Список валютных пар для отображения
    currency_pairs = ['EUR/USD', 'GBP/USD', 'USD/JPY', 'AUD/USD', 'USD/CHF']

    # Разбиваем валютные пары на компактные строки для удобства
    keyboard = [
        ['EUR/USD', 'GBP/USD'],
        ['USD/JPY', 'AUD/USD'],
        ['USD/CHF', 'USD/CAD'],
        ['Назад']  # Добавляем кнопку назад
    ]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

# Функция для создания клавиатуры с основными опциями
def create_main_keyboard():
    keyboard = [
        ['ACTIVE FIN', 'ACTIVE OTC'],
        ['Сброс']  # Добавляем кнопку сброс
    ]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

# Функция для создания клавиатуры с кнопкой "Назад" (для прогноза)
def create_back_keyboard():
    keyboard = [
        ['Назад']
    ]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

# Функция, которая будет запускаться при команде /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Привет! Выберите одну из опций:",
        reply_markup=create_main_keyboard()
    )

# Функция для выбора ACTIVE FIN
async def active_fin(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Выберите валютную пару:",
        reply_markup=create_currency_keyboard()
    )

# Функция для выбора ACTIVE OTC
async def active_otc(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "ACTIVE OTC пока не поддерживается.",
        reply_markup=create_main_keyboard()
    )

# Функция для прогноза
async def forecast(update: Update, context: CallbackContext):
    # Получаем выбранную валютную пару
    currency_pair = update.message.text.strip()

    # Если пользователь выбрал кнопку "Назад", возвращаем в меню валютных пар
    if currency_pair == "Назад":
        await active_fin(update, context)
        return

    # Получаем прогноз для валютной пары
    prediction = get_prediction(currency_pair.replace('/', ''))

    # Отправляем результат пользователю
    await update.message.reply_text(prediction, parse_mode='Markdown')

    # Отправляем кнопку "Назад"
    await update.message.reply_text(
        "Если хотите вернуться назад, нажмите 'Назад'.",
        reply_markup=create_back_keyboard()
    )

# Функция для сброса и возврата в главное меню
async def reset(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Вы вернулись в главное меню.",
        reply_markup=create_main_keyboard()
    )

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

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()











