from odoo import models, fields

class PesantrenRoom(models.Model):
    _name = 'pesantren.room'
    _description = 'Pesantren Room'

    name = fields.Char(string='Room Name', required=True)
    capacity = fields.Integer(string='Capacity', required=True)
    santri_ids = fields.Many2many('res.partner', string='Santri', domain=[('is_company', '=', False)])

