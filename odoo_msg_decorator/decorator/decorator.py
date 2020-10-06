from msg_decorator.decorator.bot import create_bot
from msg_decorator.decorator.send_message import send_message


def msg_decorator(f, *args):
    def wrapper(*args, **kwargs):
        bot, ids = create_bot(1)
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
