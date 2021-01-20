# -*- coding: utf-8 -*-
# Copyright 2017 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class EtichetteConfigurationSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    etichette_small_page_width = fields.Float(string='Small page width', size=4, digits=(4, 0), required=True, default=28)
    etichette_small_page_height = fields.Float(string='Small page height', size=4, digits=(4, 0), required=True, default=80)
    etichette_small_margin_top = fields.Float(string='Small page margin top', size=4, digits=(4, 0), required=True, default=2)
    etichette_small_margin_right = fields.Float(string='Small page margin right', size=4, digits=(4, 0), required=True, default=1)
    etichette_small_margin_bottom = fields.Float(string='Small page margin bottom', size=4, digits=(4, 0), required=True, default=2)
    etichette_small_margin_left = fields.Float(string='Small page margin left', size=4, digits=(4, 0), required=True, default=1)
    etichette_small_header_spacing = fields.Float(string='Small header spacing', size=4, digits=(4, 0), required=True, default=0)
    etichette_small_dpi = fields.Float(string='Small dpi', size=4, digits=(4, 0), required=True, default=90)
