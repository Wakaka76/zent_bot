import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import time
import random

TOKEN = "8547410707:AAEPYbkYy04Panp22DvNZRovxKfi-ABeeAU"
ADMIN_IDS = [5849423818, 987654321]  # Вадим и Арсений

bot = telebot.TeleBot(TOKEN)

# ========== КРУТЫЕ КНОПКИ ==========
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("🎬 ХОЧУ ЭДИТ 🔥")
menu.row("📖 КТО ТАКИЕ ZENT?", "💰 СКОЛЬКО ДЕНЕГ?")
menu.row("⭐ ПОКАЖИ ПРИМЕРЫ", "📞 ГДЕ ВЫ?")
menu.row("💬 НАПИСАТЬ ПО-ЧЕЛОВЕЧЕСКИ")

# ========== ЖИВЫЕ ТЕКСТЫ ==========

about_text = """
🤘 ПРИВЕТ, ДРУГ! 🤘

Мы — ZENT | Эдиты. Вадим и Арсений, два пацана, которые делают эдиты.

⬇️⬇️⬇️ КАК ЭТО РАБОТАЕТ ⬇️⬇️⬇️

1️⃣ Ты кидаешь мне свои фото (5-10 штук) или видос
2️⃣ Я колдую с эффектами и переходами
3️⃣ Через 30-60 мин ты получаешь ГОТОВЫЙ ЭДИТ
4️⃣ Смотришь и решаешь: нравится → платишь 50₽, нет → не платишь

⬇️⬇️⬇️ ЧЕСТНО, БЕЗ ОБМАНА ⬇️⬇️⬇️

• Никакой предоплаты — даже копейки не просим
• Твои фото? Да мы их через час удаляем
• Не нравится результат? Иди гуляй, платить не надо
• Мы не пропадаем — всегда отвечаем

⬇️⬇️⬇️ ДЛЯ КОГО ЭТО ⬇️⬇️⬇️

• Для ТикТока
• Для Instagram Reels
• Для просто для души
• Для показать друзьям

🔥 КОРОЧЕ, ПРОСТО ПОПРОБУЙ. ТЕБЕ ЖЕ НЕ СЛОЖНО, А МНЕ ПРИЯТНО 🔥
"""

price_text = """
💰 ДЕНЬГИ — ЩЕКОТЛИВАЯ ТЕМА 💰

НО У НАС ПРОСТО:

50 РУБЛЕЙ. ПЯТЬДЕСЯТ. 50 ₽.

⬇️ ПОЧЕМУ СТОЛЬКО? ⬇️

Потому что мы не олигархи. Мы школьники/студенты, которые умеют делать крутые вещи.

⬇️ КАК ПЛАТИТЬ? ⬇️

Ты сначала ПОЛУЧАЕШЬ эдит. Смотришь, проверяешь, ржёшь или плачешь (от счастья). 
Если зашло — кидаешь 50₽ на карту. Если нет — НИЧЕГО НЕ ДОЛЖЕН.

⬇️ СЕРЬЁЗНО? ⬇️

Серьёзно. Нам нужны довольные клиенты, а не разовые 50 рублей. 
Хочешь проверить нашу честность? Закажи эдит, получи его, а потом реши.

😎 ПС: первый заказ можешь вообще не оплачивать, просто так, для знакомства 😎
"""

examples_text = """
⭐ ПРИМЕРЫ? ЛЕГКО! ⭐

Что мы умеем:

🔥 БЫСТРЫЙ МОНТАЖ — тык-тык-тык, и видео под трек
🔥 ПЛАВНЫЕ ПЕРЕХОДЫ — красиво, эстетично, под музыку
🔥 ЭФФЕКТЫ — замедления, ускорения, неон, киберпанк
🔥 ТЕКСТ НА ВИДЕО — добавлю что скажешь

⬇️ ГДЕ ПОСМОТРЕТЬ? ⬇️

Пока примеры не выложили (лень/времени нет), но ты можешь:

• Заказать пробный эдит — первые фото просто так сделаем
• Спросить у тех, кто заказывал — они живы и довольны

⬇️ КОРОЧЕ ⬇️

Хочешь увидеть — закажи. Ты ничего не теряешь, кроме 10 минут времени.
"""

contacts_text = """
📞 НАШИ КОНТАКТЫ (НЕ ПОТЕРЯЙ) 📞

⬇️ ГДЕ НАС ИСКАТЬ ⬇️

• В этом боте — я всегда онлайн
• Вадим: @vadim_zent (если бот тупит — пиши сюда)
• Арсений: @arseny_zent (по сотрудничеству)

⬇️ КОГДА ОТВЕЧАЕМ ⬇️

Обычно в течение 15-30 минут. Иногда быстрее.
Если долго нет ответа — значит спим/в школе/едим. Дёрни ещё раз.

⬇️ ЧТО ПИСАТЬ ⬇️

Можешь просто «Привет», можешь сразу фото кидать. Мы не кусаемся.

🤝 БУДЕМ ЗНАКОМЫ 🤝
"""

order_text = """
🎬 ОК, ТЫ РЕШИЛ ЗАКАЗАТЬ ЭДИТ 🎬

⬇️ ЧТО ОТ ТЕБЯ НУЖНО ⬇️

Вариант 1: 5-10 фотографий
Вариант 2: одно видео (до 30 секунд)

⬇️ ЧТО ПОТОМ ⬇️

1. Я получаю твои файлы
2. Делаю эдит (30-60 минут, иногда быстрее)
3. Присылаю тебе готовое видео
4. Ты смотришь и решаешь: платить 50₽ или нет

⬇️ КАКУЮ МУЗЫКУ СТАВИТЬ? ⬇️

Напиши название трека и исполнителя. Если не напишешь — поставлю что-то крутое на свой вкус.

⬇️ ПОЕХАЛИ? ⬇️

КИДАЙ ФОТКИ ИЛИ ВИДОС 👇👇👇
"""

answer_text = """
📩 ОТВЕТИЛИ, ПОДОЖДИ 📩

Я переслал твоё сообщение ребятам. Они скоро напишут (15-30 мин).

⬇️ ЧТО ДЕЛАТЬ? ⬇️

Просто жди. Не спамь. Мы тебя не забыли.

А пока можешь:
• Посмотреть примеры (кнопка «ПОКАЖИ ПРИМЕРЫ»)
• Почитать про цены
• Или просто ждать, пока тебе ответит человек, а не бот

🤘 Скоро увидимся 🤘
"""


# ========== ПРИВЕТСТВИЕ ==========
@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔥 ДА, ПОГНАЛИ 🔥", callback_data="agree"))
    kb.add(InlineKeyboardButton("😴 МОЖЕТ, ПОТОМ", callback_data="disagree"))

    bot.send_message(
        message.chat.id,
        f"🧨🧨🧨 ВНИМАНИЕ 🧨🧨🧨\n\n"
        f"Ты попал в ZENT | Эдиты.\n\n"
        f"Мы делаем эдиты из твоих фото и видео. Без предоплаты. Без обмана.\n\n"
        f"{about_text}\n\n"
        f"⬇️⬇️⬇️ ТЫ С НАМИ? ⬇️⬇️⬇️",
        reply_markup=kb
    )

    @bot.callback_query_handler(func=lambda call: call.data == "agree")
    def agree(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            call.message.chat.id,
            f"🤘 ДОБРО ПОЖАЛОВАТЬ В КОМАНДУ ZENT 🤘\n\n"
            f"{about_text}\n\n"
            f"👇 ВЫБИРАЙ, ЧЕГО ХОЧЕШЬ 👇",
            reply_markup=menu
        )

    @bot.callback_query_handler(func=lambda call: call.data == "disagree")
    def disagree(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            call.message.chat.id,
            f"😔 Ладно, без обид. Если надумаешь — жми /start\n\n"
            f"Мы будем тут, с эдитами и позитивом 🤘"
        )

    # ========== КНОПКИ ==========
    @bot.message_handler(func=lambda m: m.text == "📖 КТО ТАКИЕ ZENT?")
    def about(m):
        bot.send_message(m.chat.id, about_text)

    @bot.message_handler(func=lambda m: m.text == "💰 СКОЛЬКО ДЕНЕГ?")
    def price(m):
        bot.send_message(m.chat.id, price_text)

    @bot.message_handler(func=lambda m: m.text == "⭐ ПОКАЖИ ПРИМЕРЫ")
    def examples(m):
        bot.send_message(m.chat.id, examples_text)

    @bot.message_handler(func=lambda m: m.text == "📞 ГДЕ ВЫ?")
    def contacts(m):
        bot.send_message(m.chat.id, contacts_text)

    @bot.message_handler(func=lambda m: m.text == "🎬 ХОЧУ ЭДИТ 🔥")
    def order(m):
        bot.send_message(m.chat.id, order_text)

    @bot.message_handler(func=lambda m: m.text == "💬 НАПИСАТЬ ПО-ЧЕЛОВЕЧЕСКИ")
    def human(m):
        bot.send_message(m.chat.id,
                         "✏️ Пиши сюда что хочешь. Я прочитаю и отвечу (не сразу, но отвечу). Живой человек тебе ответит!")

    # ========== ФОТО И ВИДЕО ==========
    @bot.message_handler(content_types=['photo', 'video'])
    def handle_files(message):
        responses = [
            "✅ ФОТКИ ПРИНЯЛ! ЩА БУДЕТ КРАСОТА 🔥",
            "🎬 О, видос! Сейчас поколдую над ним",
            "📸 ПРИНЯЛ! Через 30-60 мин пришлю готовый эдит",
            "😎 Хорошие фото, сейчас сделаю шедевр",
            "🤘 ЗАПИЛИВАЮ... Жди результат!"
        ]

        bot.send_message(message.chat.id, random.choice(responses))
        bot.send_message(message.chat.id,
                         "⏱ Обычно уходит 30-60 минут. Ты получишь готовое видео СЮДА. Оплата ПОСЛЕ того, как посмотришь и одобришь.")

        for admin_id in ADMIN_IDS:
            try:
                user = message.from_user
                name = f"@{user.username}" if user.username else user.first_name

                bot.send_message(admin_id, f"🔔🔔🔔 НОВЫЙ ЗАКАЗ! 🔔🔔🔔\n\nОт: {name}\nID: {user.id}\n\n⬇️ ФАЙЛЫ ⬇️")

                if message.photo:
                    bot.send_photo(admin_id, message.photo[-1].file_id)
                if message.video:
                    bot.send_video(admin_id, message.video.file_id)
                if message.caption:
                    bot.send_message(admin_id, f"📝 Трек/комментарий: {message.caption}")

                bot.send_message(admin_id, f"👉 Чтобы ответить клиенту: /answer {user.id} [текст]")
            except Exception as e:
                print(f"Ошибка: {e}")

    # ========== ТЕКСТОВЫЕ СООБЩЕНИЯ ==========
    @bot.message_handler(func=lambda m: True)
    def forward_to_admin(message):
        # Пропускаем кнопки
        buttons = ["📖 КТО ТАКИЕ ZENT?", "💰 СКОЛЬКО ДЕНЕГ?", "⭐ ПОКАЖИ ПРИМЕРЫ",
                   "📞 ГДЕ ВЫ?", "🎬 ХОЧУ ЭДИТ 🔥", "💬 НАПИСАТЬ ПО-ЧЕЛОВЕЧЕСКИ"]

        if message.text in buttons:
            return
        if message.text and message.text.startswith('/'):
            return

        for admin_id in ADMIN_IDS:
            try:
                user = message.from_user
                name = f"@{user.username}" if user.username else user.first_name

                bot.send_message(admin_id, f"💬💬💬 СООБЩЕНИЕ ОТ {name} 💬💬💬\n\n{message.text}")
                bot.send_message(message.chat.id, answer_text)
            except Exception as e:
                print(f"Ошибка: {e}")

    # ========== ОТВЕТ АДМИНОВ ==========
    @bot.message_handler(commands=['answer'])
    def admin_reply(message):
        if message.from_user.id in ADMIN_IDS:
            pass
        else:
            bot.send_message(message.chat.id, "❌ Не лезь в настройки бота, плиз")
        return

    try:
        parts = message.text.split(' ', 2)
        if len(parts) < 3:
            bot.send_message(message.chat.id, "❌ Формат: /answer ID_пользователя Текст ответа")
            return

        user_id = int(parts[1])
        reply_text = parts[2]

        bot.send_message(user_id, f"📩 ОТВЕТ ОТ ZENT:\n\n{reply_text}\n\n🤘 Если что-то ещё — пиши!")
        bot.send_message(message.chat.id, f"✅ Ответ отправлен пользователю {user_id}")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка: {e}")

# ========== ЗАПУСК ==========
print("="*50)
print("🤘 ZENT | ЭДИТЫ - БОТ ВЗЛЕТЕЛ! 🤘")
print("="*50)
print("Вадим и Арсений, бот готов к работе!")
print("Клиенты могут заказывать эдиты")
print("="*50)

bot.infinity_polling()