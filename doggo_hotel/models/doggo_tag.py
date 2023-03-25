from odoo import api, fields, models
class DoggoTag (models.Model):
    _name = "doggo.tag"
    _description = "Doggo Tag"

    name = fields.Char(string="Name" , required=True)
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Color")

    _sql_constraints = [
        ('unique_tag_name', 'unique (name, active)', 'The tag must be unique!')
    ]

