# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.addons import decimal_precision as dp


class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    categ_id = fields.Many2one('product.category',related='product_id.category_id', string='Product Category', readonly=True)

    @api.depends('order_id.order_line')
    def _compute_get_number(self):
        self.number = 0
        for order in self:
            number = 0
            for line in order.order_id.order_line:
                number += 1
                line.number = number
                
                
    number = fields.Integer('Seq', compute='_compute_get_number')