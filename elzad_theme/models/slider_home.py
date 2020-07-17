# -*- coding: utf-8 -*-
from odoo import fields, models


class SliderHome(models.Model):
    _name = "slider.home"
    _description = "Slider home"

    name = fields.Char(string='Name', required=True, translate=True)
    image = fields.Binary(string="Icon")
    link = fields.Char(string="Link")
