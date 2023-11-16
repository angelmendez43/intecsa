from odoo import api, fields, models, tools, _
from odoo.modules import get_module_resource


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    tipo_transaccion = fields.Selection([('cheque', 'Cheque'), ('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta')], string='Tipo transaccion')
