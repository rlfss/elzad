# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Elzad Theme',
    'description': 'Elzad website theme',
    'category': 'Theme/eCommerce',
    'sequence': 1000,
    'version': '1.0.5',
    'depends': ['website', 'website_theme_install', 'auth_signup', 'website_sale', 'portal', 'product',
                'website_sale_wishlist', 'auth_signup', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'templates/assets.xml',
        'templates/header.xml',
        'templates/footer.xml',
        'templates/home.xml',
        'templates/login.xml',
        'templates/signup.xml',
        'views/slider_home_view.xml',
        'views/product_template.xml',
        'views/res_partner_view.xml',
    ],
    'images': [
        'static/description/cover.png',
        'static/description/thumbnail.png',
    ],
    'application': False,
}
