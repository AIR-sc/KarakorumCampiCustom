from datetime import datetime, timedelta
from odoo import SUPERUSER_ID
from odoo import api, fields, models, _
from odoo.http import request


class product_template(models.Model):
	_inherit = "product.template"

	# CARATTERISTICHE
	collezione = fields.Many2one('karakorum.collezione', string="Collezione", help="Associa il prodotto ad una collezione.")
	stagione = fields.Many2one('karakorum.stagione', string="Stagione", help="Associa il prodotto ad una stagione.")
	confezione_associata = fields.Char(string="Conf. associata", help="Specifica il numero delle confezioni omaggio associate.")

	pubblica_web_rivenditori = fields.Boolean(string="Pubblica sito riv.", help="Spuntare la casella per pubblicare l'articolo sul sito dei rivenditori (.tv)")
	pubblica_web_b2c = fields.Boolean(string="Pubblica sito B2C", help="Spuntare la casella per pubblicare l'articolo sul sito B2C (.it)")