from datetime import datetime, timedelta
from odoo import SUPERUSER_ID
from odoo import api, fields, models, _
from odoo.http import request


class contact_template(models.Model):
	_inherit = "res.partner"

	agente = fields.Many2one('karakorum.agente', string="Agente")
	facebook =  fields.Char(string="Facebook")
	instagram =  fields.Char(string="Instagram")
	twitter =  fields.Char(string="Twitter")
	linkedin =  fields.Char(string="LinkedIn")

class agente(models.Model):
    _name = "karakorum.agente"

    name = fields.Char(string='Nome')
    contacts_ids = fields.One2many('res.partner', 'agente', string="Contatti")