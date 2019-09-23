# -*- coding: utf-8 -*-
from odoo import http

# class Extra-addons/snippets(http.Controller):
#     @http.route('/extra-addons/snippets/extra-addons/snippets/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-addons/snippets/extra-addons/snippets/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/snippets.listing', {
#             'root': '/extra-addons/snippets/extra-addons/snippets',
#             'objects': http.request.env['extra-addons/snippets.extra-addons/snippets'].search([]),
#         })

#     @http.route('/extra-addons/snippets/extra-addons/snippets/objects/<model("extra-addons/snippets.extra-addons/snippets"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/snippets.object', {
#             'object': obj
#         })