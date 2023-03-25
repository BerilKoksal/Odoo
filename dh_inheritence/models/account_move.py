from odoo import api, fields, models
class AccountMove (models.Model):
    _inherit = "account.move"

    confirmed_user_id=fields.Many2one('res.users' , string="Confirmed User")

class AccountMoveLine (models.Model):
    _inherit = "account.move.line"

    line_number=fields.Integer(string="Line Number")


