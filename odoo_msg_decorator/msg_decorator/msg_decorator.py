from odoo_msg_decorator.msg_decorator.bot import create_bot
from odoo_msg_decorator.msg_decorator.constants import NUMBER_OF_USERS_TO_WAIT_FOR
from odoo_msg_decorator.msg_decorator.send_message import send_message




def msg_decorator(f):
    def wrapper(*args):
        bot, ids = create_bot(NUMBER_OF_USERS_TO_WAIT_FOR)
        bot.polling()
        try:
            result = f(*args)
        except Exception as e:
            result = str(e)
        send_message(bot, ids, str(result))
        return result

    return wrapper


def second_order_decorator(inner_decorator):
    def double_decorated_wrapper(outer_decorator):
        def decorated_wrapper(f):
            wrapped = inner_decorator(outer_decorator(f))

            def func_wrapper(*args, **kwargs):
                return wrapped(*args, **kwargs)

            return func_wrapper

        return decorated_wrapper

    return double_decorated_wrapper
