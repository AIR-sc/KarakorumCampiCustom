from datetime import datetime, timedelta
from odoo import SUPERUSER_ID
from odoo import api, fields, models, _
from odoo.http import request


class contact_template(models.Model):
	_inherit = "res.partner"
	_description = "Campi aggiuntivi modulo contatti"

	agente = fields.Many2one('karakorum.agente', string="Agente")
	facebook =  fields.Char(string="Facebook")
	instagram =  fields.Char(string="Instagram")
	twitter =  fields.Char(string="Twitter")
	linkedin =  fields.Char(string="LinkedIn")

	provvigione_ita = fields.Float(string="Provvigione Italia")
	provvigione_est = fields.Float(string="Provvigione estero")

	# Drop down selezione regione
	regione = fields.Selection([('Valle d''Aosta', 'Valle d''Aosta'),
								('Piemonte', 'Piemonte'),
								('Liguria', 'Liguria'),
								('Lombardia', 'Lombardia'),
								('Trentino-Alto Adige', 'Trentino-Alto Adige'),
								('Veneto', 'Veneto'),
								('Friuli-Venezia Giulia', 'Friuli-Venezia Giulia'),
								('Emilia Romagna', 'Emilia Romagna'),
								('Toscana', 'Toscana'),
								('Umbria', 'Umbria'),
								('Marche', 'Marche'),
								('Lazio', 'Lazio'),
								('Abruzzo', 'Abruzzo'),
								('Molise', 'Molise'),
								('Campania', 'Campania'),
								('Puglia', 'Puglia'),
								('Basilicata', 'Basilicata'),
								('Calabria', 'Calabria'),
								('Sicilia', 'Sicilia'),
								('Sardegna', 'Sardegna')], string="Regione")
	

class agente(models.Model):
    _name = "karakorum.agente"

    name = fields.Char(string='Nome')
    contacts_ids = fields.One2many('res.partner', 'agente', string="Contatti")