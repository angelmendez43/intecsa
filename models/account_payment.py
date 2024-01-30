from odoo import models, fields

class AccountPaymentInherited(models.Model):
    _inherit = 'account.payment'

    descripcion = fields.Char(string='Descripción')
