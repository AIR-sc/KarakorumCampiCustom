from datetime import datetime, timedelta
from odoo import SUPERUSER_ID
from odoo import api, fields, models, _
from odoo.http import request


class product_template(models.Model):
	_inherit = "product.template"

	# CARATTERISTICHE
	collezione = fields.Many2one('karakorum.collezione', string="Collezione")
	stagione = fields.Many2one('karakorum.stagione', string="Stagione")
	confezione_associata = fields.Char(string="Conf. associata")