# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Karakorum custom fields',
    'version': "1.2.0.0",
    'author': "AIR-sc",
    'summary': 'Consente di specificare alcuni campi personalizzati per Karakorum',
    'description' : 'Consente di specificare alcuni campi custom come stagione, collezione,... nei prodotti. Ma anche nei contatti e negli ordini',
    'license':'OPL-1',
    'category': "Extra Tools",
    'data':[
             'views/product_form_custom_fields.xml',
             'views/contact_form_custom_fields.xml',
             'views/movmagazzino_form_custom_fields.xml',
             'views/custom_css.xml',
             'views/menu.xml',
             'security/ir.model.access.csv',
             'reports/etichette_report.xml',
             'reports/etichette_report_template.xml'
             ],
    'css': ['static/src/css/karakorum_custom.css'],
    'website': 'https://www.air-srl.com',
    'depends': ['stock', 'sale'],
    'installable': True,
    'auto_install': False,
	"images":['static/description/karakorumLogo.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
