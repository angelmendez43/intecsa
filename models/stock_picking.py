# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import time
import logging

from odoo import api, fields, models, _

class Warehouse(models.Model):
    _inherit = 'stock.warehouse'
    _description = 'add new fields'

    no_almacen = fields.Char('Número almacén')
    
