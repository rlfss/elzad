# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sex = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Sex")
    date_of_birth = fields.Date(string='Date of Birth')
