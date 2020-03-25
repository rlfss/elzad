# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class website(models.Model):
    _inherit = 'website'

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    city_sel = fields.Many2one('res.partner.city', string='City')
    zone = fields.Many2one('res.partner.zone', string='Zone')
    
    @api.onchange('city_sel')
    def _onchange_city_sel(self):
        if self.city_sel:
            self.city = self.city_sel.name

    
class CitySelect(models.Model):
    _name = 'res.partner.city'
    _description = 'City Select'
    
    name =  fields.Char('Name')
    code = fields.Char('Code')
    
class ZoneSelect(models.Model):
    _name = 'res.partner.zone'
    _description = 'Zone Select'
    
    name =  fields.Char('Name')
    city_sel = fields.Many2one('res.partner.city', string='City')
    code = fields.Char('Code')
