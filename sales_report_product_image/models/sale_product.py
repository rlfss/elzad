# See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    print_image = fields.Boolean('Print Image', default=True)

    image_sizes = fields.Selection(
        [('image', 'Big sized Image'), ('image_medium', 'Medium Sized Image'),
         ('image_small', 'Small Sized Image')],
        'Image Sizes', default="image_small",
        help="Image size to be displayed in report")


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    image_small = fields.Binary(
        'Product Image', related='product_id.image_small')
