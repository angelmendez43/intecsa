from odoo import models, fields

class IntecsaEntregas(models.Model):
	_name = 'intecsa.entregas'
	_description = 'Entregas'

	name = fields.Char('Nombre')
