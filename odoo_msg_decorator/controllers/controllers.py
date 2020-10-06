# -*- coding: utf-8 -*-
# from odoo import http


# class OdooMsgDecorator(http.Controller):
#     @http.route('/odoo_msg_decorator/odoo_msg_decorator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_msg_decorator/odoo_msg_decorator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_msg_decorator.listing', {
#             'root': '/odoo_msg_decorator/odoo_msg_decorator',
#             'objects': http.request.env['odoo_msg_decorator.odoo_msg_decorator'].search([]),
#         })

#     @http.route('/odoo_msg_decorator/odoo_msg_decorator/objects/<model("odoo_msg_decorator.odoo_msg_decorator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_msg_decorator.object', {
#             'object': obj
#         })
