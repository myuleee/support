import sqlite3
import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '8409649553:AAEnIxWXA4rFg027Kw4oNtfEkKZpBz6JbQs'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🔥 Оптимизация AMD", "📕 База знаний"],
        ["⚙️ Инструкция по установке", "🎮 Драйверы GPU"],
        ["💻 Драйверы CPU", "📞 Связь с разработчиком"],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    welcome_text = (
        'Добро пожаловать в AMD Support Bot!\n\n'
        'Я — бот поддержки для пользователей AMD.\n'
        'Помогу с драйверами, настройками и решением проблем.\n\n'
        'Что я умею:\n'
        '• Показывать последние драйверы\n'
        '• Давать инструкции по установке\n'
        '• Помогать с оптимизацией\n'
        '• Решать частые проблемы\n\n'
        'Выберите действие ниже 👇'
    )

    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup
    )


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🔥 Оптимизация AMD":
        keyboard = [
            [InlineKeyboardButton("Настройки Radeon Software", callback_data="settings_rs")],
            [InlineKeyboardButton("Дисплей", callback_data="display_place")],
            [InlineKeyboardButton("🔙 Возврат в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Выберите нужный вам пункт:", reply_markup=reply_markup)

    elif text == "📕 База знаний":
        await update.message.reply_text("Раздел 'База знаний' в разработке...")

    elif text == "⚙️ Инструкция по установке":
        await update.message.reply_text("Инструкции по установке в разработке...")

    elif text == "🎮 Драйверы GPU":
        await update.message.reply_text("Раздел 'Драйверы GPU' в разработке...")

    elif text == "💻 Драйверы CPU":
        await update.message.reply_text("Раздел 'Драйверы CPU' в разработке...")

    elif text == "📞 Связь с разработчиком":
        keyboard = [[InlineKeyboardButton("Написать разработчику", url="https://t.me/bapehook")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Свяжитесь с разработчиком:", reply_markup=reply_markup)


async def handle_inline_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "settings_rs":
        # Первое изображение с основными настройками
        settings_text_1 = ('⚙️ *Настройки Radeon Software:*\n\n'
                           '1️⃣ Откройте Radeon Software\n'
                           '2️⃣ Перейдите в раздел Игры\n'
                           '3️⃣ Выберите "Видеокарта"\n\n'
                           '🔧 *Рекомендуемые настройки:*\n'
                           '• *Radeon Anti-Lag* - ВЫКЛ (для снижения задержки ввода)\n'
                           '• *Radeon Boost* - ВЫКЛ (динамическое разрешение для повышения FPS)\n'
                           '• *Radeon Chill* - ВЫКЛ (для максимальной производительности)\n'
                           '• *Image Sharpening* - 70-80% (улучшение четкости без потери FPS)')

        try:
            with open('radeon_settings.jpg', 'rb') as photo:
                await query.message.reply_photo(
                    photo=photo,
                    caption=settings_text_1,
                    parse_mode='Markdown'
                )
        except FileNotFoundError:
            await query.message.reply_text("Первое изображение не найдено")
            await query.message.reply_text(settings_text_1, parse_mode='Markdown')
        except Exception as e:
            await query.message.reply_text(f"Ошибка при отправке изображения: {e}")

        settings_text_2 = ('📌 *Дополнительные настройки:*\n\n'
                           'Листаем вниз и нажимаем на дополнительные настройки')

        try:
            with open('radeon_settings_2.jpg', 'rb') as photo:
                await query.message.reply_photo(
                    photo=photo,
                    caption=settings_text_2,
                    parse_mode='Markdown'
                )
        except FileNotFoundError:
            await query.message.reply_text("Второе изображение не найдено")
            await query.message.reply_text(settings_text_2, parse_mode='Markdown')
        except Exception as e:
            await query.message.reply_text(f"Ошибка при отправке изображения: {e}")

        keyboard = [[InlineKeyboardButton("🔙 Назад к оптимизации", callback_data="back_to_optimization")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    elif query.data == "display_place":
        display_text = ('🖥️ *Настройки дисплея:*\n\n'
                        '1️⃣ *Параметры дисплея*\n'
                        '2️⃣ *Пользовательский цвет*\n'
                        '3️⃣ *Пользовательские разрешения*\n\n'
                        '*Пункт «Параметры дисплея»*\n'
                        '• «Масштабирование ГП» включить\n'
                        '• «Режим масштабирования» на Полная панель\n\n'
                        '*Пункт «Пользовательский цвет»*\n'
                        '• Индивидуальная настройка (можете поставить как на фото)\n\n'
                        '*Пункт «Пользовательские разрешения»*\n'
                        '• Нажимаете "Создать новый"\n'
                        '• Меняете только Разрешение, Частота обновления ГЦ, Отображение (параметр синхронизации)')

        keyboard = [[InlineKeyboardButton("🔙 Назад к оптимизации", callback_data="back_to_optimization")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

        try:
            with open('display_settings.jpg', 'rb') as photo:
                await query.message.reply_photo(
                    photo=photo,
                    caption=display_text,
                    parse_mode='Markdown'
                )
        except FileNotFoundError:
            await query.message.reply_text(display_text, parse_mode='Markdown')
        except Exception as e:
            await query.message.reply_text(f"Ошибка при отправке изображения: {e}")

    elif query.data == "back_to_optimization":
        keyboard = [
            [InlineKeyboardButton("Настройки Radeon Software", callback_data="settings_rs")],
            [InlineKeyboardButton("Дисплей", callback_data="display_place")],
            [InlineKeyboardButton("🔙 Возврат в главное меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите нужный вам пункт:", reply_markup=reply_markup)

    elif query.data == "main_menu":
        keyboard = [
            ["🔥 Оптимизация AMD", "📕 База знаний"],
            ["⚙️ Инструкция по установке", "🎮 Драйверы GPU"],
            ["💻 Драйверы CPU", "📞 Связь с разработчиком"],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await query.message.delete()
        await query.message.reply_text("Главное меню:", reply_markup=reply_markup)


def main():
    try:
        application = Application.builder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
        application.add_handler(CallbackQueryHandler(handle_inline_buttons))

        print("Бот успешно запущен...")
        application.run_polling()
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")


if __name__ == '__main__':
    main()
