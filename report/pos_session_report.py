from odoo import models, api

class ReportPOSSession(models.AbstractModel):
    _name = 'report.intecsa.report_pos_session_template'

    @api.model
    def _get_report_values(self, docids, data=None):
        sessions = self.env['pos.session'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'pos.session',
            'docs': sessions,
        }
