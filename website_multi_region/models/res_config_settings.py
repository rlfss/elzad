from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    has_multi_region = fields.Boolean("Multi-region")
    # regions = fields.Many2one('website.regions',"Regions")