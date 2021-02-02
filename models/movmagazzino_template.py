from datetime import datetime, timedelta
from odoo import SUPERUSER_ID
from odoo import api, fields, models, _
from odoo.http import request


class ordine_template(models.Model):
	_inherit = "stock.picking"
    
	_description = "Campi aggiuntivi modulo movimento magazzino"

	numero_colli = fields.Integer('Numero colli',default=1)
	contrassegno = fields.Float('Contrassegno', digits=(8,2))