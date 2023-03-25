from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class DoggoHotelReservation (models.Model):
    _name = "doggo.hotel.reservation"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "Doggo Hotel Reservation"
    _rec_name = 'doggo_id'
    #_order = 'id decs'

    doggo_id=fields.Many2one('doggo.hotel.guest', string='Doggo', ondelete="restrict")
    reservation_date=fields.Datetime(string="Reservation Date", default=fields.Datetime.now)
    reservation_time=fields.Date(string='Reservation Time')
    gender = fields.Selection(related='doggo_id.gender')
    parent = fields.Char(string="Parent Name" , help="Parent name from doggo record")
    content = fields.Html(string="Content")
    priority = fields.Selection([('0', 'Very Low'),
                                 ('1', 'Low'),
                                 ('2', 'Normal'),
                                 ('3', 'High')],
                                string='Priority')
    state = fields.Selection([('draft', 'Draft'),
                                 ('in_progress', 'In Progress'),
                                 ('done', 'Done'),
                                 ('cancel', 'Canceled')], default='draft', required=True,
                                string='Status')
    sitter_id=fields.Many2one('res.users', string="Dog Sitter")
    food_ids = fields.One2many('reservation.food.lines', 'reservation_id', string="Food Preference")
    hide_price=fields.Boolean(string="Hide Price")
    reference_record=fields.Reference(selection=[('doggo.hotel.guest','Doggo'),('doggo.hotel.reservation','Reservation')],
                                      string="Record")
    duration = fields.Float(string="Duration")



    def unlink(self):
        for rec in self:
            if self.state != 'draft':
                raise ValidationError(_("You can not delete this reservation."))
            return super(DoggoHotelReservation,self).unlink()

    @api.onchange('doggo_id')
    def onchange_doggo_id(self):
        self.parent = self.doggo_id.parent
    def test_button(self):
        print("Works like that")
        return {
                'type': 'ir.actions.act_url',
                'target' : 'new',
                'url': 'https://www.youtube.com/watch?v=v2AC41dglnM'
            }


    def action_in_progress(self):
        for rec in self:
            if rec.state=='draft':
              rec.state='in_progress'

    # def action_cancel(self):
    #     action = self.env.ref('doggo_hotel.action_cancel_reservation').read()[0]
    #     return action

    def action_done(self):
        for rec in self:
            rec.state='done'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Here you are',
                    'type': 'rainbow_man',
                }
            }
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_share_whatsapp(self):
        whatsapp_api_url='https://api.whatsapp.com/send?'
        return

class ReservationFoodLines(models.Model):
    _name = "reservation.food.lines"
    _description = "Reservation Food Lines"

    product_id = fields.Many2one('product.product' , required=True)
    price = fields.Float(related='product_id.list_price')
    quantity = fields.Integer(string="Quantity", default=1)
    reservation_id = fields.Many2one('doggo.hotel.reservation', string='Doggo')



