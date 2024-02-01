from odoo import models, fields
import logging

class AccountPaymentRegisterInherit(models.TransientModel):
    _inherit = 'account.payment.register'
    
    descripcion = fields.Char(string='Descripción')

    def _create_payments(self):
        self.ensure_one()
        res = super(AccountPaymentRegisterInherit, self)._create_payments()
        res.write({'descripcion': self.descripcion if self.descripcion else ''})
        return res
       
       