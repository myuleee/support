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
        keyboard = [
            [InlineKeyboardButton("🤖 Последние версии", callback_data="last_version")],
            [InlineKeyboardButton("🛠 Ссылки для скачивания", callback_data="link_save")],
            [InlineKeyboardButton("✅ Рекомендации", callback_data="rec_data")],
            [InlineKeyboardButton("📋 Что нового в последних драйверах", callback_data="last_driver")],
            [InlineKeyboardButton("🔙 Возврат в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Выберите нужный вам пункт:", reply_markup=reply_markup)

    elif text == "💻 Драйверы CPU":
        # Новое меню для CPU драйверов
        keyboard = [
            [InlineKeyboardButton("🖥️ Что такое чипсетные драйверы?", callback_data="chipset_info")],
            [InlineKeyboardButton("⚡ Важность обновления чипсета", callback_data="chipset_importance")],
            [InlineKeyboardButton("📥 Скачать драйверы чипсета", callback_data="chipset_download")],
            [InlineKeyboardButton("🛠 Инструкция по установке", callback_data="chipset_install")],
            [InlineKeyboardButton("🔙 Возврат в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Выберите нужный вам пункт:", reply_markup=reply_markup)

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

    elif query.data == "chipset_info":
        info_text = (
            '🖥️ *Что такое чипсетные драйверы?*\n\n'
            'Чипсетные драйверы — это программное обеспечение, которое обеспечивает связь между процессором (CPU) и остальными компонентами материнской платы.\n\n'
            'Они отвечают за:\n'
            '• 🚀 *Управление питанием* — правильное распределение напряжения и энергосбережение\n'
            '• 🔌 *Работу USB портов* — стабильность подключения устройств\n'
            '• 💾 *SSD и накопители* — оптимизация работы NVMe и SATA дисков\n'
            '• 🎮 *PCI Express* — корректная работа видеокарты и других устройств\n'
            '• 🌡 *Мониторинг* — правильное отображение температур и скоростей вентиляторов\n'
            '• 🔄 *AMD Ryzen Power Plans* — специальные схемы питания для максимальной производительности\n\n'
            '❗ Важно: Чипсетные драйверы устанавливаются отдельно от драйверов видеокарты!'
        )
        await query.message.edit_text(info_text, parse_mode='Markdown')
        keyboard = [[InlineKeyboardButton("🔙 Назад к драйверам CPU", callback_data="back_to_cpu_drivers")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    elif query.data == "chipset_importance":
        importance_text = (
            '⚡ *Важность обновления чипсетных драйверов*\n\n'
            'Многие пользователи недооценивают важность чипсетных драйверов, но они критически важны для стабильной работы системы!\n\n'
            '✅ *Зачем обновлять:*\n'
            '• 📈 *Прирост производительности* — новые драйверы оптимизируют работу процессора, особенно для Ryzen\n'
            '• 🐛 *Исправление багов* — устранение проблем с USB, вылетами игр, синими экранами смерти\n'
            '• 🔋 *Улучшенное энергопотребление* — процессор работает эффективнее, снижается температура\n'
            '• 🎮 *Лучшая совместимость с играми* — многие современные игры требуют актуальные драйверы чипсета\n'
            '• 🚀 *Поддержка новых технологий* — например, PCIe 4.0/5.0, USB 3.2 Gen2x2\n'
            '• 🛡 *Безопасность* — исправление уязвимостей на аппаратном уровне\n\n'
            '⚠️ *Что может случиться без обновления:*\n'
            '• Периодические зависания системы\n'
            '• Проблемы с подключением периферии (клавиатура, мышь)\n'
            '• Некорректная работа USB-C и быстрой зарядки\n'
            '• Снижение FPS в играх\n'
            '• Невозможность использовать функцию SAM (Smart Access Memory)'
        )
        await query.message.edit_text(importance_text, parse_mode='Markdown')
        keyboard = [[InlineKeyboardButton("🔙 Назад к драйверам CPU", callback_data="back_to_cpu_drivers")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    elif query.data == "chipset_download":
        download_text = (
            '📥 *Скачать чипсетные драйверы AMD*\n\n'
            '🔗 *Официальная страница загрузки:*\n'
            'https://www.amd.com/ru/support/chipsets\n\n'
            '📌 *Как выбрать правильный драйвер:*\n\n'
            '1️⃣ Зайдите на официальный сайт AMD по ссылке выше\n'
            '2️⃣ Выберите свою платформу:\n'
            '   • *Для AM5* (Ryzen 7000/8000/9000): AMD Socket AM5\n'
            '   • *Для AM4* (Ryzen 1000-5000): AMD Socket AM4\n'
            '   • *Для TRX40/sTRX4* (Threadripper): соответствующий раздел\n'
            '   • *Для мобильных процессоров*: Laptops and Pre-built PCs\n\n'
            '3️⃣ Нажмите "Отправить"\n'
            '4️⃣ Скачайте версию для вашей ОС (Windows 10/11)\n\n'
            '💡 *Совет:* Всегда скачивайте последнюю WHQL версию для максимальной стабильности.\n\n'
            '🔍 *Как определить свой чипсет:*\n'
            '• Нажми Win + R → введите "msinfo32" → строка "Модель материнской платы"\n'
            '• Или используйте программу CPU-Z → вкладка "Mainboard"\n'
            '• Модель обычно имеет вид: B550, X570, B650, X670, A620 и т.д.'
        )
        await query.message.edit_text(download_text, parse_mode='Markdown')
        keyboard = [[InlineKeyboardButton("🔙 Назад к драйверам CPU", callback_data="back_to_cpu_drivers")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    elif query.data == "chipset_install":
        install_text = (
            '🛠 *Инструкция по установке чипсетных драйверов*\n\n'
            '📋 *Способ 1: Автоматическая установка*\n\n'
            '1. Скачайте последнюю версию драйверов с официального сайта AMD\n'
            '2. Закройте все работающие программы\n'
            '3. Запустите скачанный .exe файл\n'
            '4. Следуйте инструкциям установщика\n'
            '5. Перезагрузите компьютер после завершения установки\n\n'
            '🧹 *Способ 2: Чистая установка (при возникновении проблем)*\n\n'
            '1. Сначала удалите старые драйверы через Панель управления\n'
            '2. Перезагрузите компьютер\n'
            '3. Скачайте свежие драйверы\n'
            '4. Установите и снова перезагрузитесь\n\n'
            '⚙️ *Способ 3: Через Windows Update*\n\n'
            'Windows может автоматически устанавливать базовые драйверы, но рекомендуется скачивать их вручную с сайта AMD для получения всех оптимизаций.\n\n'
            '💡 *Важные моменты:*\n'
            '• После установки чипсетных драйверов в Windows появятся специальные планы питания "AMD Ryzen Balanced" или "AMD Ryzen High Performance"\n'
            '• Для процессоров Ryzen 5000/7000/9000 рекомендуется выбирать план "AMD Ryzen Balanced"\n'
            '• Если вы используете режим "Ultimate Performance" от Windows, он также совместим с процессорами AMD\n\n'
            '⚠️ *После установки обязательно перезагрузите компьютер!*'
        )
        await query.message.edit_text(install_text, parse_mode='Markdown')
        keyboard = [[InlineKeyboardButton("🔙 Назад к драйверам CPU", callback_data="back_to_cpu_drivers")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    elif query.data == "back_to_cpu_drivers":
        keyboard = [
            [InlineKeyboardButton("🖥️ Что такое чипсетные драйверы?", callback_data="chipset_info")],
            [InlineKeyboardButton("⚡ Важность обновления чипсета", callback_data="chipset_importance")],
            [InlineKeyboardButton("📥 Скачать драйверы чипсета", callback_data="chipset_download")],
            [InlineKeyboardButton("🛠 Инструкция по установке", callback_data="chipset_install")],
            [InlineKeyboardButton("🔙 Возврат в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Выберите нужный вам пункт:", reply_markup=reply_markup)

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
                    'Игра рендерится в низком разрешении, а ИИ апскейлит картинку.')

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
        auto_text = ('Способ 1: Автоматическая установка (рекомендуется для новичков)\n\n'
                     'Самый простой способ — использовать официальный инструмент автоопределения AMD.\n\n'
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

    if query.data == "rych_setup":
        rych_text = ('Способ 2: Ручная установка (если автоопределение не сработало)\n\n'
                     'Этот способ пригодится, если у тебя старое железо, специфичная ОС или не работают автоопределители.\n\n'
                     'Шаг 1. Скачивание драйвера\n'
                     '1. Перейди на страницу: www.amd.com/ru/support\n'
                     '2. Воспользуйся ручным поиском:\n'
                     '• Выбери категорию продукта (например, "Графика" или "Чипсеты").\n'
                     '• Выбери серию и модель своего устройства.\n'
                     '3. Нажми Отправить и выбери версию драйвера для своей операционной системы.\n'
                     'Если ты обновляешь драйвер со старой версии — перейди к разделу "Чистая установка" ниже.\n\n'
                     'Шаг 2. Процесс установки\n'
                     '1. Запусти скачанный .exe файл.\n'
                     '2. Если появится запрос контроля учетных записей (UAC), нажми Да.\n'
                     '3. Установщик распакует файлы (по умолчанию в C:\AMD) и запустится автоматически.\n'
                     '4. Прими лицензионное соглашение.\n'
                     '5. Выбери тип установки:\n'
                     '• Default (По умолчанию) — полная версия Radeon Software со всеми функциями (запись, стриминг, настройка).\n'
                     '• Minimal (Минимальная) — только основные драйверы, без расширенных функций.\n'
                     '• Driver Only (Только драйвер) — только драйвер без панели управления.\n'
                     '6. Для чистой установки отметь галочку Factory Reset (Сброс к заводским)\n'
                     'это удалит старые версии и перезагрузит ПК.\n'
                     '7. Нажми Установить и дождись завершения. Экран может пару раз мигнуть — это нормально.\n'
                     '8. По окончании перезагрузи компьютер, если потребуется.')

        await query.message.edit_text(rych_text)
        keyboard = [[InlineKeyboardButton("🔙 Назад к инструкциям", callback_data="back_to_instruction")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    if query.data == "clean_setup":
        clean_text = ('🧹 Способ 3: Чистая установка (если возникают ошибки или глюки)\n\n'
                      'Если старый драйвер "сломался", вылетают ошибки или черный экран, лучше удалить всё полностью и начать с нуля.\n\n'
                      'Инструкция по полной зачистке:\n\n'
                      '1. Скачай официальную утилиту AMD Cleanup Utility.\n'
                      'https://www.amd.com/en/resources/support-articles/faqs/GPU-601.html\n'
                      '(Она часто идет в комплекте с драйверами в папке Bin64, либо её можно найти на форумах поддержки AMD.)\n'
                      '2. Отключи интернет (выдерни кабель или отключи Wi-Fi).\n'
                      '3. Запусти amdcleanuputility.exe.\n'
                      '4. Утилита предложит перезагрузиться в безопасном режиме — согласись (Да).\n'
                      '5. В безопасном режиме она удалит все следы старых драйверов AMD.\n'
                      '6. После завершения компьютер снова перезагрузится.\n'
                      'Теперь можно устанавливать свежий драйвер способом 1 или 2.')

        await query.message.edit_text(clean_text)
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

    if query.data == "last_version":
        last_text = ('⚡ Последние Актуальные версии:\n'
                     'Adrenalin 26.3.1 Preview (март 2026, бета)\n'
                     'Adrenalin 26.2.2 WHQL (18 февраля 2026)\n'
                     'Adrenalin 26.2.1 WHQL (11 февраля 2026)\n'
                     'Adrenalin 26.1.1 WHQL (21 января 2026)\n\n'
                     '📋 Предыдущие стабильные:\n'
                     'Adrenalin 25.12.1 WHQL (декабрь 2025)\n'
                     'Adrenalin 25.10.2 WHQL (октябрь 2025)\n'
                     'Adrenalin 25.9.2 WHQL (сентябрь 2025)\n'
                     'Adrenalin 25.9.1 WHQL (сентябрь 2025)\n'
                     'Adrenalin 25.8.1 WHQL (август 2025)')

        await query.message.edit_text(last_text)
        keyboard = [[InlineKeyboardButton("🔙 Назад к разделу", callback_data="back_to_driversGPU")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    if query.data == "link_save":
        link_text = ('📌 Официальный сайт AMD:\n'
                     '🔗 Центр загрузки AMD (https://www.amd.com/ru/support)\n\n'
                     '✅ *Последний драйвер для 9000 серии:*\n'
                     'https://www.amd.com/en/support/downloads/drivers.html/graphics/radeon-rx/radeon-rx-9000-series.html\n'
                     '✅ *Последний драйвер для 7000 серии:*\n'
                     'https://www.amd.com/en/support/downloads/drivers.html/graphics/radeon-rx/radeon-rx-7000-series.html\n'
                     '✅ *Последний драйвер для 6000 серии:*\n'
                     'https://www.amd.com/en/support/downloads/drivers.html/graphics/radeon-rx/radeon-rx-6000-series.html\n'
                     '✅ *Последний драйвер для 5000 серии:*\n'
                     'https://www.amd.com/en/support/downloads/drivers.html/graphics/radeon-rx/radeon-rx-5000-series.html\n\n'
                     '⚠️ Важно: Всегда скачивайте драйверы только с официального сайта AMD!')

        await query.message.edit_text(link_text)
        keyboard = [[InlineKeyboardButton("🔙 Назад к разделу", callback_data="back_to_driversGPU")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    if query.data == "rec_data":
        rec_text = ('Рекомендации по драйверам AMD\n\n'
                    '⭐ Лучший выбор:\n'
                    'Adrenalin 26.2.2 (WHQL)\n'
                    '  • Самая стабильная версия на данный момент\n'
                    '  • Полная поддержка всех новых игр\n'
                    '  • Работает на RX 9000/8000/7000 сериях\n\n'
                    '🎮 Для игр:\n'
                    'Adrenalin 26.2.2 + HYPR-RX 2.0\n'
                    '   • Включайте HYPR-RX в играх одной кнопкой\n'
                    '   • AFMF 3 дает +30-50% FPS\n'
                    '   • FSR 4.0 в поддерживаемых играх\n\n'
                    '💻 Для работы:\n'
                    'Adrenalin 25.12.1\n'
                    '   • Максимальная стабильность\n'
                    '   • Минимум ошибок в профессиональном ПО\n'
                    '   • Проверено временем\n\n'
                    'Лучше поставить постарее драйвер, чем новый\n'
                    'Старый драйвер (3+ месяца) уже протестирован тысячами пользователей, все критические баги найдены и исправлены, работают без сбоев.\n\n'
                    '💡 Главные советы:\n'
                    '✅ Всегда ставьте WHQL версии для стабильности\n'
                    '🧹 Используйте DDU или AMD Cleanup Utility для чистой установки\n'
                    '💾 Делайте точку восстановления перед обновлением\n'
                    '🔄 Не гонитесь за "свежестью", если всё работает\n'
                    '📌 Preview версии только для тестирования')

        await query.message.edit_text(rec_text)
        keyboard = [[InlineKeyboardButton("🔙 Назад к разделу", callback_data="back_to_driversGPU")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    if query.data == "last_driver":
        lstdrive_text = ('🚀 Adrenalin 26.3.1 (Март 2026, бета)\n'
                         'Новые функции:\n'
                         '   • AMD FSR 4 — новая ИИ-масштабизация для RX 9070 серии\n'
                         '   • AFMF 2.1 — улучшенная генерация кадров с меньшим гостингом\n'
                         '   • AMD Chat — локальный ИИ-чат с генерацией текста и изображений\n'
                         '   • AMD Install Manager — автообновление драйверов\n'
                         '   • ROCm на WSL 2 — официальная поддержка для RX 7000\n\n'
                         '⚡ Adrenalin 26.2.2 (Февраль 2026, WHQL)\n'
                         'Поддержка новых игр:\n'
                         '   • Resident Evil Requiem\n'
                         '   • Marathon\n'
                         'Исправлено:\n'
                         '   • Вылеты в Roblox Player на RX 7000 при переключении задач\n'
                         '   • Мерцание текстур при Instant Replay на RX 7000\n\n'
                         '⚡ Adrenalin 26.2.1 (Февраль 2026, WHQL)\n'
                         'Поддержка новых игр:\n'
                         '   • Yakuza Kiwami 3 & Dark Ties\n'
                         '   • Nioh 3\n'
                         'Исправлено:\n'
                         '   • Искаженные облака в Arc Raiders на RX 9000\n'
                         '   • Вылеты в The Finals с RT на RX 7000\n\n'
                         '⚡ Adrenalin 26.1.1 (Январь 2026, WHQL)\n'
                         'Новые функции:\n'
                         '   • Опциональный AI Bundle (набор ИИ-инструментов)\n'
                         'Поддержка новых игр:\n'
                         '   • Starsand Island\n'
                         '   • Avatar: Frontiers of Pandora - From the Ashes Edition\n'
                         'Исправлено:\n'
                         '   • Тени в Call of Duty: Black Ops 7 на RX 5000/6000\n'
                         '   • Текстуры в Enshrouded на RX 7000/9000\n'
                         '   • Вылеты в Diablo 4 с нелатинскими символами\n'
                         '   • Ночные сцены в MSFS 2024 на RX 9000\n'
                         '   • Сбои Unreal Engine 5.6 с Lumen HWRT\n'
                         '   • Артефакты в Chromium/Electron приложениях\n'
                         '   • Артефакты TAA в Baldurs Gate 3')

        await query.message.edit_text(lstdrive_text)
        keyboard = [[InlineKeyboardButton("🔙 Назад к разделу", callback_data="back_to_driversGPU")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)


    elif query.data == "back_to_driversGPU":
        keyboard = [
            [InlineKeyboardButton("🤖 Последние версии", callback_data="last_version")],
            [InlineKeyboardButton("🛠 Ссылки для скачивания", callback_data="link_save")],
            [InlineKeyboardButton("✅ Рекомендации", callback_data="rec_data")],
            [InlineKeyboardButton("📋 Что нового в последних драйверах", callback_data="last_driver")],
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
