# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import time
import logging

from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'add new fields'

    entrega_id = fields.Many2one('intecsa.entregas', 'Entrega')
    comentarios = fields.Char('Comentarios')
    oferta_venta = fields.Char('Ofertas de venta')
