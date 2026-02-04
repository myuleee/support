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
            [InlineKeyboardButton("Видеокарта", callback_data="video_card")],
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
        await query.edit_message_text('Настройки Radeon Software:\n'
                                        '1. Откройте Radeon Software\n'
                                        '2. Перейдите в раздел Настройки\n'
                                        '3. Производительность\n'
                                        '   • Radeon Anti-Lag - ВКЛ (для снижения задержки ввода)\n'
                                        '   • Radeon Boost - ВКЛ (динамическое разрешение для повышения FPS)\n'
                                        '   • Radeon Chill - ВЫКЛ (для максимальной производительности)\n'
                                        '   • Image Sharpening - 70-80% (улучшение четкости без потери FPS)'
                                      )
    elif query.data == "video_card":
        await query.edit_message_text("Настройки видеокарты:\n\n1. Разгон (если поддерживается)\n2. Настройки вентиляторов\n3. Настройки питания")
    elif query.data == "display_place":
        await query.edit_message_text("Настройки дисплея:\n\n1. Разрешение\n2. Частота обновления\n3. Цветовые профили")
    elif query.data == "main_menu":
        keyboard = [
            ["🔥 Оптимизация AMD", "📕 База знаний"],
            ["⚙️ Инструкция по установке", "🎮 Драйверы GPU"],
            ["💻 Драйверы CPU", "📞 Связь с разработчиком"],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await query.message.reply_text("Главное меню:", reply_markup=reply_markup)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    application.add_handler(CallbackQueryHandler(handle_inline_buttons))
    
    application.run_polling()

if __name__ == '__main__':
    main()
