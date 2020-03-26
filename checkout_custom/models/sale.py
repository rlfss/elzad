# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.http import request
from odoo.addons import decimal_precision as dp
import logging
_log = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_phone = fields.Char(related='partner_id.phone', string='Phone', readonly=True)
    customer_street = fields.Char(related='partner_id.street', string='Street', readonly=True)
    customer_zone = fields.Many2one(related='partner_id.zone', string='Zone', readonly=True)
    sales_agent = fields.Many2one('sale.order.agent', string='Sales Agent')

    def get_minimun_cart(self):
        
        ir_default = self.env['website'].get_current_website().c_id._convert(
                    self.env['website'].get_current_website().minimum_order_value, request.env['website'].get_current_website().pricelist_id.currency_id, self.env.user.company_id,
                    fields.Date.today()
                    )
        return 1 if ir_default == None else round(ir_default, 2)
    @api.model
    def _get_errors(self, order):
        
        minimum_order_value =1 if self.env['website'].sudo().get_current_website().minimum_order_value == None else self.env['website'].sudo().get_current_website().c_id._convert(
                    self.env['website'].sudo().get_current_website().minimum_order_value, self.env['website'].sudo().get_current_pricelist().currency_id, self.env.user.company_id,
                    fields.Date.today()
                    )
        minimum_order_value = round(minimum_order_value,2)
        errors = []
        if order and order.amount_total < minimum_order_value:
            errors.append(['Invalid Cart Value',"A minimum purchase is %s%s , current purchase total is %s%s "%(order.currency_id.symbol ,minimum_order_value, order.currency_id.symbol ,order.amount_total)])
        return errors


class SaleOrderAgent(models.Model):
    _name = "sale.order.agent"
    _description = 'Sales Agent'

    name = fields.Char('Name', readonly=True , default=lambda x: str('New'))
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    zone = fields.Many2many('res.partner.zone', string='Zones')



    @api.onchange('partner_id')
    def oderupdate(self):
        if self.partner_id:
            self.name = self.partner_id.name



class website(models.Model):
    _inherit = 'website'

    minimum_order_value = fields.Float(string='Minimum Cart Value', digits=dp.get_precision('Product Price'))
    c_id = fields.Many2one('res.currency', 'Currency',default=lambda self: self.env.user.company_id.currency_id.id,required=True)
