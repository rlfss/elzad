# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import threading

from odoo.tools.misc import split_every

from odoo import _, api, fields, models, registry, SUPERUSER_ID
from odoo.osv import expression

_logger = logging.getLogger(__name__)

    
    
class CitySelect(models.Model):
    _name = 'res.partner.city'
    _description = 'City Select'
    
    name = fields.Char('Name')
    code = fields.Char('Code')
    def get_website_sale_countries(self, mode='billing'):
        return self.sudo().search([])


class ZoneSelect(models.Model):
    _name = 'res.partner.zone'
    _description = 'Zone Select'
    
    name =  fields.Char('Name')
    city_sel = fields.Many2one('res.partner.city', string='City')
    code = fields.Char('Code')
    def get_website_sale_countries(self, mode='billing'):
        return self.sudo().search([])


    
    
class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
    city_sel = fields.Many2one('res.partner.city', string='City')
    zone = fields.Many2one('res.partner.zone', string='Zone')
    
    @api.onchange('city_sel')
    def _onchange_city_sel(self):
        if self.city_sel:
            self.city = self.city_sel.name
