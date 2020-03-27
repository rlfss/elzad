# -*- coding: utf-8 -*-
{
    'name': 'Checkout Custom',
    'category': 'Sales',
    'version': '12.2.1.0.0',
    'license': 'OPL-1',
    'depends': ['base','website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/checkout_template_view.xml',
        'views/sale.xml',
        'data/data.xml',
    ],
    'installable': True,
}
