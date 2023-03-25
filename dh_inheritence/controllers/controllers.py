# -*- coding: utf-8 -*-
# from odoo import http


# class DhInheritence(http.Controller):
#     @http.route('/dh_inheritence/dh_inheritence', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dh_inheritence/dh_inheritence/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dh_inheritence.listing', {
#             'root': '/dh_inheritence/dh_inheritence',
#             'objects': http.request.env['dh_inheritence.dh_inheritence'].search([]),
#         })

#     @http.route('/dh_inheritence/dh_inheritence/objects/<model("dh_inheritence.dh_inheritence"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dh_inheritence.object', {
#             'object': obj
#         })
