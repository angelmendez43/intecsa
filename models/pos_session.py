from odoo import models

class POSSession(models.Model):
    _inherit = 'pos.session'

    # def action_pos_session_close(self, balancing_account=False, amount_to_balance=0, bank_payment_method_diffs=None):
    #     # Llama al método original
    #     super(POSSession, self).action_pos_session_close(balancing_account, amount_to_balance, bank_payment_method_diffs)

    #     # Obtén la referencia del reporte y luego llama a report_action
    #     report_ref = self.env.ref('intecsa.report_pos_session_template')
    #     if report_ref:
    #         return report_ref.report_action(self)
    #     return True
