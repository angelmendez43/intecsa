# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import time
import logging

from odoo import api, fields, models, _

class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'
    _description = 'add new fields'

    tipo_cuenta = fields.Char('Tipo de cuenta')
    
