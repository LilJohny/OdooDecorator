# -*- coding: utf-8 -*-

from odoo_msg_decorator.decorator.decorator import msg_decorator, second_order_decorator
from odoo.odoo.api import constrains

second_order_msg_decorator = second_order_decorator(msg_decorator)
constrains = second_order_msg_decorator(constrains)
