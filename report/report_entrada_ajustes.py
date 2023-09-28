# -*- coding: utf-8 -*-
from odoo import api, models, fields
from odoo.addons.num_to_words.models.numero_letras import numero_a_letras, numero_a_moneda
import logging, datetime

class ReportEntradaAjustes(models.AbstractModel):
    _name = 'report.intecsa.report_entrada_ajustes'

    def a_letras(self,monto):
        letras = numero_a_moneda(monto)
        return letras
        
    def convertir_fecha_hora(self, fecha_hora):
    	fecha = datetime.datetime.strptime(str(fecha_hora), '%Y-%m-%d %H:%M:%S').date().strftime('%Y-%m-%d')
    	hora = datetime.datetime.strftime(fields.Datetime.context_timestamp(self, datetime.datetime.now()), "%H:%M:%S")
    	logging.warning("funcion")
    	informacion = {
    		'fecha': fecha,
    		'hora': hora,
    	}
    	return informacion
    	
    def convertir_fecha_hora_ms(self, fecha_hora):
    	fecha = datetime.datetime.strptime(str(fecha_hora), '%Y-%m-%d %H:%M:%S.%f').date().strftime('%Y-%m-%d')
    	hora = datetime.datetime.strftime(fields.Datetime.context_timestamp(self, datetime.datetime.now()), "%H:%M:%S")
    	logging.warning("funcion2")
    	informacion = {
    		'fecha': fecha,
    		'hora': hora,
    	}
    	return informacion
    	
    def contiene_lote(self, move_line_ids_without_package):
    	lote = False
    	for linea in move_line_ids_without_package:
    		if linea.lot_id:
    			lote = True
    	return lote
    	

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['stock.picking'].browse(docids)
        logging.warning("hola")
        return {
            'convertir_fecha_hora': self.convertir_fecha_hora,
            'convertir_fecha_hora_ms': self.convertir_fecha_hora_ms,
            'contiene_lote': self.contiene_lote,
            'doc_ids': docids,
            'doc_model': 'stock.picking',
            'docs': docs,
            'a_letras': self.a_letras,

        }
        
