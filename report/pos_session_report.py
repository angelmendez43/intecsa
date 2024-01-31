from odoo import models, api

class ReportPOSSession(models.AbstractModel):
    _name = 'report.intecsa.report_pos_session_template'

    def pagos_agrupados(self, o):
        pagos = {}
        if o.order_ids:
            for pedido in o.order_ids:
                if pedido.payment_ids:
                    for linea in pedido.payment_ids:
                        if linea.payment_method_id.id not in pagos:
                            pagos[linea.payment_method_id.id] = {'metodo_pago': linea.payment_method_id.name, 'total': 0, 'cantidad': 0}
                        pagos[linea.payment_method_id.id]['total'] += linea.amount
                        pagos[linea.payment_method_id.id]['cantidad'] += 1
                        
        return pagos
    
    @api.model
    def _get_report_values(self, docids, data=None):
        sessions = self.env['pos.session'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'pos.session',
            'docs': sessions,
            'pagos_agrupados': self.pagos_agrupados,
        }
