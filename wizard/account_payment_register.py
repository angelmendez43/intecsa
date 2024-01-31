from odoo import models, fields

class AccountPaymentRegisterInherit(models.TransientModel):
    _inherit = 'account.payment.register'
    
    descripcion = fields.Char(string='Descripción')

    def _create_payments(self):
        self.ensure_one()
        batches = self._get_batches()
        edit_mode = self.can_edit_wizard and len(batches[0]['lines']) == 1
        to_reconcile = []
        if edit_mode:
            payment_vals = self._create_payment_vals_from_wizard()
            payment_vals['descripcion'] = self.descripcion  
            payment = self.env['account.payment'].create(payment_vals)
            payments = payment
            to_reconcile.append(payment)
        else:
            payments = self.env['account.payment']
            for batch in batches:
                payment_vals_list = self._create_payment_vals_from_batch(batch)
                for payment_vals in payment_vals_list:
                    payment_vals['descripcion'] = self.descripcion 
                    payments |= self.env['account.payment'].create(payment_vals)
                    to_reconcile.append(payments[-1])
       
       