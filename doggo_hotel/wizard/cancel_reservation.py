from odoo import api, fields, models, _
import datetime
from odoo.exceptions import ValidationError
from datetime import date
from dateutil import relativedelta
class CancelReservationWizard (models.TransientModel):
    _name = "cancel.reservation.wizard"
    _description = "Cancel Reservation Wizard"

    @api.model
    def default_get(self, fields):
        a = super(CancelReservationWizard,self).default_get(fields)
        a['date_cancel']= datetime.date.today()
        return a

    reservation_id=fields.Many2one('doggo.hotel.reservation', string="Doggo" , domain=[('state', '=','draft')])
    reason=fields.Text(string="Reason")
    date_cancel = fields.Date(string="Cancellation Date")


    def action_cancel(self):
        cancel_days=self.env['ir.config_parameter'].get_param('doggo_hotel.cancel_days')
        allowed_date= self.reservation_id.reservation_date - relativedelta.relativedelta(days=int(cancel_days))
        if allowed_date.date() < date.today():
            raise ValidationError(_("Cancellation is not allowed within {} day of booking. You can cancel it on {}.").format(cancel_days, allowed_date.date()))
        self.reservation_id.state='cancel'
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }



