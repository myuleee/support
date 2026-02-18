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
        ["🔥 Настройки AMD", "📕 База знаний"],
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

    if text == "🔥 Настройки AMD":
        keyboard = [
            [InlineKeyboardButton("Видеокарта", callback_data="settings_rs")],
            [InlineKeyboardButton("Дисплей", callback_data="display_place")],
            [InlineKeyboardButton("🔙 Возврат в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Выберите нужный вам пункт:", reply_markup=reply_markup)

    elif text == "📕 База знаний":
        keyboard = [
            [InlineKeyboardButton("Раздел 1. Базовые знания", callback_data="baz_znanjia")],
            [InlineKeyboardButton("Раздел 2. Информация о настройке (Radeon Software)", callback_data="info_sett")],
            [InlineKeyboardButton("Раздел 3. Частые проблемы и решения", callback_data="problem_sett")],
            [InlineKeyboardButton("Раздел 4. Терминология AMD", callback_data="amd_info")],
            [InlineKeyboardButton("🔙 Возврат в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Выберите нужный вам пункт:", reply_markup=reply_markup)

    elif text == "⚙️ Инструкция по установке":
        keyboard = [
            [InlineKeyboardButton("Автоматическая установка", callback_data="auto_setup")],
            [InlineKeyboardButton("Ручная установка", callback_data="rych_setup")],
            [InlineKeyboardButton("Чистая установка", callback_data="clean_setup")],
            [InlineKeyboardButton("🔙 Возврат в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Выберите нужный вам пункт:", reply_markup=reply_markup)

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
        settings_text_1 = ('⚙️ *Настройки Radeon Software:*\n\n'
                           '1️⃣ Откройте Radeon Software\n'
                           '2️⃣ Перейдите в раздел Игры\n'
                           '3️⃣ Выберите "Видеокарта"\n\n'
                           '🔧 *Рекомендуемые настройки:*\n'
                           '• *Radeon Anti-Lag* - ВЫКЛ (снижает задержку ввода, но в некоторых соревновательных играх или на старых движках (например, в CS) она может вызывать микрозадержки)\n'
                           '• *Radeon Boost* - ВЫКЛ (динамическое разрешение для повышения FPS, в динамичных шутерах, стоит ее выключать, тк как от резких движений мышкой картинка становится размытой)\n'
                           '• *Radeon Chill* - ВЫКЛ (функция энергосбережения, которая ограничивает FPS, когда вы не двигаетесь, и повышает его при активности. Для максимальной производительности она вредна, так как создает нестабильную частоту кадров.)\n'
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
                           'Листаем вниз и нажимаем на дополнительные настройки\n'
                           'ставим все как на фото')

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
            [InlineKeyboardButton("Видеокарта", callback_data="settings_rs")],
            [InlineKeyboardButton("Дисплей", callback_data="display_place")],
            [InlineKeyboardButton("🔙 Возврат в главное меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите нужный вам пункт:", reply_markup=reply_markup)

    if query.data == "baz_znanjia":
        baz_text = ('Полезно для новых пользователей или при первой настройке.\n'
                    'Как определить свою модель AMD?\n'
                    'Нажми Ctrl + Shift + Esc(Диспетчер задач).\n'
                    'Перейди на вкладку "Производительность".\n'
                    'Слева выбери "ЦП" (процессор) или "ГП" (видеокарта). Название модели будет указано в правом верхнем углу.\n'
                    'Альтернатива: Программа CPU-Z (для процессора) или GPU-Z (для карты).\n\n'
                    'Как найти последний драйвер?\n'
                    'Способ 1 (Авто): Скачай и установи программу AMD Software: Adrenalin Edition. Она сама уведомит о новой версии.\n'
                    'Способ 2 (Ручной): Перейди на официальный сайт AMD в раздел "Драйверы и поддержка"\n' 
                    '(www.amd.com/ru/support).\n\n'
                    'Что такое чипсет и зачем его обновлять?\n'
                    'Это драйверы для материнской платы (управление USB, питанием, скоростью SSD).\n'
                    'Для процессоров Ryzen крайне рекомендуется ставить свежие драйверы чипсета с сайта AMD — они повышают производительность в играх.')

        await query.message.edit_text(baz_text)
        keyboard = [[InlineKeyboardButton("🔙 Назад к Разделам", callback_data="back_to_razdel")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    if query.data == "info_sett":
        info_text = ('Информация о настройке фирменного ПО для видеокарт\n'
                    'Где скачать Radeon Software?\n'
                    'Вместе с драйверами с официального сайта AMD.\n'
                    'Ключевые вкладки (краткий ликбез):\n'
                    '• 🎮 Игры:\n' 
                    'Здесь отображаются установленные игры. Можно тонко настроить графику для каждой игры отдельно (сглаживание, тени и т.д.).\n'
                    '• 📈 Производительность:\n'
                    'Вкладка для мониторинга (температура, FPS, частота) и разгона.\n'
                    'Есть автоматический разгон "одной кнопкой" (Auto Overclock) для новичков и ручной режим для профи.\n'
                    '⚙️ Настройки:\n'
                    'Общие параметры драйвера, уведомления, горячие клавиши.\n'
                    'Полезные функции Radeon Software:\n'
                    '• ✨ RSR (Radeon Super Resolution):\n'
                    'Технология, которая повышает FPS. Игра запускается в низком разрешении, а драйвер "дорисовывает" картинку до качества монитора.\n'
                    '• 🖱 Anti-Lag / Anti-Lag 2:\n'
                    'Уменьшает задержки ввода (клики мыши быстрее доходят до игры).\n'
                    '• 🎥 ReLive:\n'
                    'Встроенная функция записи геймплея и стриминга (аналог ShadowPlay от Nvidia). Настраивается в разделе "Запись и стриминг".')

        await query.message.edit_text(info_text)
        keyboard = [[InlineKeyboardButton("🔙 Назад к Разделам", callback_data="back_to_razdel")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)


    if query.data == "problem_sett":
        problem_text = ('Черный экран / Вылетает драйвер?\n'
                        '1. Скачай утилиту AMD Cleanup Utility(официальная программа для полного удаления старых драйверов).\n'
                        '2. Запусти её в безопасном режиме Windows (зажми Shift при перезагрузке).\n'
                        '3. После очистки перезагрузи ПК и установи свежий драйвер с сайта AMD.\n'
                        'Причина: Обычно возникает при установке нового драйвера поверх старого без очистки.\n'
                        'Низкая производительность в играх (ниже, чем в обзорах)?\n'
                        '1. Проверь, подключен ли монитор к видеокарте, а не к материнской плате.\n'
                        '2. Проверь температуры в простое и под нагрузкой (программой HWInfo/AIDA64).\n'
                        '3. Если выше 95°C у процессора или 100°C у видеокарты (Hot Spot) — проблемы с охлаждением.')

        await query.message.edit_text(problem_text)
        keyboard = [[InlineKeyboardButton("🔙 Назад к Разделам", callback_data="back_to_razdel")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    if query.data == "amd_info":
        amd_text = ('Словарик AMD\n'
                    '• AM4 / AM5: Сокеты (разъемы)\n'
                    'материнских плат для процессоров Ryzen.\n'
                    'AM4 — старая платформа (серии 1000-5000),\n'
                    'AM5 — новая (серии 7000, 9000, требует DDR5).\n'
                    '• X3D: Процессоры с дополнительной 3D-\n'
                    '(например, 5800X3D, 7800X3D). Лучшие игровые\n'
                    'процессоры AMD, так как память на кристалле снижает задержки.\n'
                    '• Infinity Cache: Большой кэш на видеокартах\n'
                    'Radeon RX 6000 и 7000, который позволяет им\n'
                    'отлично работать даже с "медленной" памятью и экономить энергию.\n'
                    '• SAM (Smart Access Memory):Технология для связки\n'
                    'Ryzen + Radeon, позволяющая процессору видеть\n'
                    'всю память видеокарты сразу, что дает прирост FPS (обычно 5-15%).Включается в BIOS как "Re-size BAR".\n'
                    '• FidelityFX Super Resolution (FSR):Технология повышения FPS от AMD (работает на любых видеокартах, даже Nvidia).\n'
                    'Игра рендерится в низком разрешении, а ИИ апскейлит картинку.\n')

        await query.message.edit_text(amd_text)
        keyboard = [[InlineKeyboardButton("🔙 Назад к Разделам", callback_data="back_to_razdel")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    elif query.data == "back_to_razdel":
        keyboard = [
            [InlineKeyboardButton("Раздел 1. Базовые знания", callback_data="baz_znanjia")],
            [InlineKeyboardButton("Раздел 2. Информация о настройке (Radeon Software)", callback_data="info_sett")],
            [InlineKeyboardButton("Раздел 3. Частые проблемы и решения", callback_data="problem_sett")],
            [InlineKeyboardButton("Раздел 4. Терминология AMD", callback_data="amd_info")],
            [InlineKeyboardButton("🔙 Возврат в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите нужный вам пункт:", reply_markup=reply_markup)

    if query.data == "auto_setup":
        auto_text = ('Способ 1: Автоматическая установка (рекомендуется для новичков)\n'
                    'Самый простой способ — использовать официальный инструмент автоопределения AMD.\n'
                    'Что нужно сделать:\n'
                    '1. Перейди на официальный сайт AMD:\n' 
                    'www.amd.com/ru/support\n'
                    '2. Нажми кнопку "Скачать сейчас" под инструментом Auto-Detect and Install.\n'
                    '3. Запусти скачанный файл и нажми Install.\n'
                    '4. Утилита сама проверит твою систему, определит модели твоих устройств и предложит скачать самые свежие драйверы.\n'
                    '5. Выбери драйвер:\n'
                    '• Recommended (Рекомендованный) — лучше стабильность, сертифицирован Microsoft.\n'
                    '• Optional (Опциональный) — свежие функции и исправления.\n'
                    '6. Следуй инструкциям установщика.')

        await query.message.edit_text(auto_text)
        keyboard = [[InlineKeyboardButton("🔙 Назад к инструкциям", callback_data="back_to_instruction")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    elif query.data == "back_to_instruction":
        keyboard = [
            [InlineKeyboardButton("Автоматическая установка", callback_data="auto_setup")],
            [InlineKeyboardButton("Ручная установка", callback_data="rych_setup")],
            [InlineKeyboardButton("Чистая установка", callback_data="clean_setup")],
            [InlineKeyboardButton("🔙 Возврат в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите нужный вам пункт:", reply_markup=reply_markup)


    elif query.data == "main_menu":
        keyboard = [
            ["🔥 Настройки AMD", "📕 База знаний"],
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
