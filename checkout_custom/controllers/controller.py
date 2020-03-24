# -*- coding: utf-8 -*-
import logging
import re

import odoo
from odoo import http,SUPERUSER_ID ,_
from odoo.http import route,request
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.exceptions import UserError
from odoo.addons.website_sale.controllers.main import WebsiteSale
_logger = logging.getLogger(__name__)

class WebsiteSale(WebsiteSale):

    def _get_mandatory_billing_fields(self):
        return ["name", "phone", "street", "city", "country_id"]
