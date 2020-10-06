import telebot


def create_bot(number_of_users_to_wait_for):
    bot = telebot.TeleBot(
        "1350534262:AAGmrQ5PpfMHQ66vb2mNA1txv2jzHbEzozc")  # You can set parse_mode by default. HTML or MARKDOWN
    ids = []

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        ids.append(message.chat.id)
        bot.reply_to(message, "Notifications from Odoo are set up for you.")
        if len(ids) >= number_of_users_to_wait_for:
            bot.stop_polling()

    return bot, ids
