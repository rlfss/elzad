# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Elzad Theme',
    'description': 'Elzad website theme',
    'category': 'Theme',
    'sequence': 1,
    'version': '12.0',
    'depends': ['website','website_theme_install','portal','website_sale'],
    'data': [
        'views/assets.xml',
        'views/templates.xml',
        'views/website_sale.xml',
    ],

    'application': False,
}
