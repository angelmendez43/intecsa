from odoo import api, fields, models, tools, _
import ast
import copy
import datetime
import io
import json
import logging
import markupsafe
from collections import defaultdict
from math import copysign, inf

from odoo.modules import get_module_resource
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo.addons.web.controllers.main import clean_action
from odoo.exceptions import RedirectWarning
from odoo.osv import expression
from odoo.tools import config, date_utils, get_lang
from odoo.tools.misc import formatLang, format_date
from odoo.tools.misc import xlsxwriter

import logging

class AccountReport(models.AbstractModel):
    _inherit = 'account.report'


    def _get_html_render_values(self, options, report_manager):
        res = super(AccountReport, self)._get_html_render_values(options, report_manager)

        res['report']['company'] = self.env.company
        return res
