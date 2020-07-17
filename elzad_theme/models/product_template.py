# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_offers = fields.Boolean('Offers')
    is_popular = fields.Boolean('Popular')