import telebot

from odoo_msg_decorator.msg_decorator.constants import TELEGRAM_TOKEN, WELCOME_PHRASE


def create_bot(number_of_users_to_wait_for):
    bot = telebot.TeleBot(
        TELEGRAM_TOKEN)  # You can set parse_mode by default. HTML or MARKDOWN
    ids = []

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        ids.append(message.chat.id)
        bot.reply_to(message, WELCOME_PHRASE)
        if len(ids) >= number_of_users_to_wait_for:
            bot.stop_polling()

    return bot, ids
