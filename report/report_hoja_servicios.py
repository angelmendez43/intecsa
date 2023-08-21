# -*- coding: utf-8 -*-
from odoo import api, models
from odoo.addons.num_to_words.models.numero_letras import numero_a_letras, numero_a_moneda
import logging

class ReportHojaServicios(models.AbstractModel):
    _name = 'report.intecsa.report_hoja_servicios'

    def a_letras(self,monto):
        letras = numero_a_moneda(monto)
        return letras

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['project.task'].browse(docids)
        tmpl_id = docs.worksheet_template_id.sudo().model_id.model
        worksheet = self.env[tmpl_id].search([('x_project_task_id', '=', docs.id)])
        logging.warning("hola")
        logging.warning(worksheet)
        return {
            'doc_ids': docids,
            'doc_model': 'project.task',
            'docs': docs,
            'worksheet': worksheet,
            'a_letras': self.a_letras,

        }
