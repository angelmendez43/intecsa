# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import time
import logging

from psycopg2 import sql, DatabaseError

from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import ValidationError, UserError
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'add new fields'


    codigo = fields.Char(string='Código')
