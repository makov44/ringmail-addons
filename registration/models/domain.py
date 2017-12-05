from odoo import models, fields, api


class Domain(models.Model):
    _name = 'ringmail_reg.domain'

    name = fields.Char(string='Domain Name', required=True)
    state = fields.Selection([
        ('draft', 'Not Confirmed'),
        ('done', 'Confirmed'),
    ], string='Status', index=True, readonly=True, copy=False, default='draft')
