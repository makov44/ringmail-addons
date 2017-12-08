from odoo import models, fields, api
from odoo.exceptions import UserError


class Alias(models.Model):
    _name = 'ringmail_reg.alias'

    name = fields.Char(string='Email Name', required=True)
    state = fields.Selection([
        ('draft', 'Not Confirmed'),
        ('done', 'Confirmed'),
    ], string='Status', index=True, readonly=True, copy=False, default='draft')

    @api.multi
    def send_confirmation_email(self):
        pass