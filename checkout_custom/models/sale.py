# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_phone = fields.Char(related='partner_id.phone', string='Phone', readonly=True)
    customer_street = fields.Char(related='partner_id.street', string='Street', readonly=True)
    customer_zone = fields.Many2one(related='partner_id.zone', string='Zone', readonly=True)
    sales_agent = fields.Many2one('sale.order.agent', string='Sales Agent')


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
