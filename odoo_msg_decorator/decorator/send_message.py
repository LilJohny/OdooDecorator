
def send_message(bot, ids, msg_text):
    for i in ids:
        bot.send_message(i, msg_text)
