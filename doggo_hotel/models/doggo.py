from odoo import api, fields, models,_
from odoo.exceptions import ValidationError
from datetime import date
class DoggoHotelGuest (models.Model):
    _name = "doggo.hotel.guest"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "Doggo Hotel Guest"

    name = fields.Char(string='Name', tracking=True)
    age = fields.Integer(string='Age', compute="_compute_age", inverse="_inverse_compute_age")
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')
    breed = fields.Char(string='Breed')
    active = fields.Boolean(string="Active" , default=True)
    date_of_birth = fields.Date(string='Date of Birth')
    parent = fields.Char(string="Parent Name")
    guest_no = fields.Char(string="Guest No")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('doggo.tag' , string="Tags")
    reservation_count = fields.Integer(string="Reservation Count", compute="_compute_reservation_count", store=True)
    reservation_ids=fields.One2many('doggo.hotel.reservation', 'doggo_id', string="Reservations")

    @api.depends('reservation_ids')
    def _compute_reservation_count(self):
        for rec in self:
            rec.reservation_count= self.env['doggo.hotel.reservation'].search_count([('doggo_id','=',rec.id)])

    @api.ondelete(at_uninstall=False)
    def _check_reservation(self):
        for rec in self:
            if self.reservation_ids:
                raise ValidationError(_("You can not delete a guest with reservation."))



    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("Time travel doesn't exist."))

    @api.model
    def create(self, vals):
        print("works")
        vals['guest_no']=self.env['ir.sequence'].next_by_code('doggo.hotel.guest')
        return super(DoggoHotelGuest,self).create(vals)


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    @api.depends('age')
    def _inverse_compute_age(self):
        return

    def action_view_reservation(self):
        return {
            'name': _('Reservations'),
            'view_mode': 'list,form',
            'res_model': 'doggo.hotel.reservation',
            'domain':[('doggo_id','=',self.id)],
            'type': 'ir.actions.act_window',
            'context': {'default_doggo_id': self.id},
            'target': 'current'
        }
