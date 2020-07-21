from datetime import datetime

from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.exceptions import UserError
from openerp.http import request


class AuthSignupHomeExt(AuthSignupHome):

    def do_signup(self, qcontext):
        """ Replaced the default do_signup base module to add extra fields. """
        if qcontext.get('company_type') == 'company':
            values = {key: qcontext.get(key) for key in ('login', 'password', 'phone', 'name','company_type')}
        if qcontext.get('company_type') == 'person':
            values = {key: qcontext.get(key) for key in ('login', 'password', 'phone', 'date_of_birth', 'sex','company_type','title')}
            values['name'] = qcontext.get('first_name') + ' ' + qcontext.get('last_name')
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        supported_langs = [lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
        if request.lang in supported_langs:
            values['lang'] = request.lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()
