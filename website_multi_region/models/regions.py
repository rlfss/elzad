from odoo import api, fields, models
from odoo.http import request


class Regions(models.Model):
    _name = 'website.branches'

    name = fields.Char("Name")
    code = fields.Char("Code")
    stock_location = fields.Many2one('stock.location',String = "Stock Location")
    sales_team = fields.Many2one('crm.team',String = "Sales Team")
    pricelist = fields.Many2one('product.pricelist',String = "Price")

    def get_branches_available(self):
        return self.search([])

    def get_current_branch(self):
        if request and request.session.get('website_sale_current_br'):
            br = self.env['website.branches'].browse(request.session['website_sale_current_br'])
            return br.id

