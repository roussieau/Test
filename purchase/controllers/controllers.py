# -*- coding: utf-8 -*-
# from odoo import http


# class Account(http.Controller):
#     @http.route('/account/account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account/account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account.listing', {
#             'root': '/account/account',
#             'objects': http.request.env['account.account'].search([]),
#         })

#     @http.route('/account/account/objects/<model("account.account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account.object', {
#             'object': obj
#         })
