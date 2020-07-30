# -*- coding: utf-8 -*-
{
    'name': "Website Multi-Region",
    'summary': 'Multi-Region ',
    'category': 'Website',
    'version': '12.0.1.0.0',
    'license': "AGPL-3",
    'description': """
        With this module you can sell your products in different regions with different price list for every region.
    """,

    'author': "Yousuf",
    'depends': ['base','website','stock','website_sale','elzad_theme'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/templates.xml',
        # 'views/res_config_settings_views.xml',
        'views/regions_view.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False,
}
