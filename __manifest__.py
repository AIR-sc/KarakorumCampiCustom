# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': "Karakorum custom fields",
    'version': "1.0.0.0",
    'author': "AIR-sc",
    'summary': 'Consente di specificare alcuni campi personalizzati nell''elenco dei proditti',
    'description' : 'Consente di specificare alcuni campi custom come stagione, collezione,... nei prodotti',
    'license':'OPL-1',
    'category': "Extra Tools",
    'data':[
             'views/product_form_custom_fields.xml',
             'views/contact_form_custom_fields.xml',
             'views/menu.xml',
             'security/ir.model.access.csv',
             ],
    'website': 'https://www.air-srl.com',
    'depends': ['stock'],
    'installable': True,
    'auto_install': False,
	"images":['static/description/karakorumLogo.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
