from datetime import datetime, timedelta
from odoo import SUPERUSER_ID
from odoo import api, fields, models, _
from odoo.http import request

class collezione(models.Model):
    _name = "karakorum.collezione"

    name = fields.Char(string='Valore')
    description = fields.Char(string='Descrizione')
    products_ids = fields.One2many('product.template', 'collezione', string="Prodotti")

class stagione(models.Model):
    _name = "karakorum.stagione"

    name = fields.Char(string='Valore')
    description = fields.Char(string='Descrizione')
    products_ids = fields.One2many('product.template', 'stagione', string="Prodotti")
