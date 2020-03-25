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
from odoo.exceptions import UserError

class WebsiteSale(WebsiteSale):

    def _get_mandatory_billing_fields(self):
        return ["name", "phone", "street", "city_sel", "zone", "country_id"]



    @http.route(['/shop/address'], type='http', methods=['GET', 'POST'], auth="public", website=True)
    def address(self, **kw):
        Partner = request.env['res.partner'].with_context(show_address=1).sudo()
        order = request.website.sale_get_order()

        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection

        mode = (False, False)
        can_edit_vat = False
        def_country_id = order.partner_id.country_id
        def_zone = order.partner_id.zone
        def_city_sel = order.partner_id.city_sel
        values, errors = {}, {}

        partner_id = int(kw.get('partner_id', -1))

        # IF PUBLIC ORDER
        if order.partner_id.id == request.website.user_id.sudo().partner_id.id:
            mode = ('new', 'billing')
            can_edit_vat = True
            country_code = request.session['geoip'].get('country_code')
            if country_code:
                def_country_id = request.env['res.country'].search([('code', '=', country_code)], limit=1)
            else:
                def_country_id = request.website.user_id.sudo().country_id
        # IF ORDER LINKED TO A PARTNER
        else:
            if partner_id > 0:
                if partner_id == order.partner_id.id:
                    mode = ('edit', 'billing')
                    can_edit_vat = order.partner_id.can_edit_vat()
                else:
                    shippings = Partner.search([('id', 'child_of', order.partner_id.commercial_partner_id.ids)])
                    if partner_id in shippings.mapped('id'):
                        mode = ('edit', 'shipping')
                    else:
                        return Forbidden()
                if mode:
                    values = Partner.browse(partner_id)
            elif partner_id == -1:
                mode = ('new', 'shipping')
            else: # no mode - refresh without post?
                return request.redirect('/shop/checkout')

        # IF POSTED
        if 'submitted' in kw:
            pre_values = self.values_preprocess(order, mode, kw)
            errors, error_msg = self.checkout_form_validate(mode, kw, pre_values)
            post, errors, error_msg = self.values_postprocess(order, mode, pre_values, errors, error_msg)

            if errors:
                errors['error_message'] = error_msg
                values = kw
            else:
                partner_id = self._checkout_form_save(mode, post, kw)
                if mode[1] == 'billing':
                    order.partner_id = partner_id
                    order.onchange_partner_id()
                    # This is the *only* thing that the front end user will see/edit anyway when choosing billing address
                    order.partner_invoice_id = partner_id
                    if not kw.get('use_same'):
                        kw['callback'] = kw.get('callback') or \
                            (not order.only_services and (mode[0] == 'edit' and '/shop/checkout' or '/shop/address'))
                elif mode[1] == 'shipping':
                    order.partner_shipping_id = partner_id

                order.message_partner_ids = [(4, partner_id), (3, request.website.partner_id.id)]
                if not errors:
                    return request.redirect(kw.get('callback') or '/shop/confirm_order')

        country = 'country_id' in values and values['country_id'] != '' and request.env['res.country'].browse(int(values['country_id']))
        country = country and country.exists() or def_country_id


        zone = 'zone' in values and values['zone'] != '' and request.env['res.partner.zone'].browse(int(values['zone']))
        zone = zone and zone.exists() or def_zone

        city_sel = 'city_sel' in values and values['city_sel'] != '' and request.env['res.partner.city'].browse(int(values['city_sel']))
        city_sel = city_sel and city_sel.exists() or def_city_sel

        render_values = {
            'website_sale_order': order,
            'partner_id': partner_id,
            'mode': mode,
            'checkout': values,
            'can_edit_vat': can_edit_vat,
            'country': country,
            'countries': country.get_website_sale_countries(mode=mode[1]),
            'zone': zone,
            'zones': zone.get_website_sale_countries(mode=mode[1]),
            'city_sel': city_sel,
            'city_sels': city_sel.get_website_sale_countries(mode=mode[1]),
            "states": country.get_website_sale_states(mode=mode[1]),
            'error': errors,
            'callback': kw.get('callback'),
            'only_services': order and order.only_services,
        }
        return request.render("website_sale.address", render_values)

	def _filter_attributes(self, **kw):
		return {k: v for k, v in kw.items() if "attribute" in k}

	def get_redirect_url(self, product_id):
		url = "/shop/cart"
		redirect_to_cart = request.website.redirect_to_cart

		if redirect_to_cart == 'same' and product_id:
			product = request.env['product.product'].browse(int(product_id))
			if product:
				url = '/shop/product/%s' % slug(product.product_tmpl_id)
		elif redirect_to_cart == "previous_page":
			url = request.httprequest.referrer

		return url

	@http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True, csrf=False)
	def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
		super(website_sale, self).cart_update(product_id, add_qty=add_qty, set_qty=set_qty, **kw)

		url = self.get_redirect_url(product_id)
		return request.redirect(url)

	@http.route("/new_get_redirect_val", type='json', auth="public",website=True)
	def new_get_redirect_val(self, product_id):
		url = self.get_redirect_url(product_id)
		return url

	@http.route(["/website/new_lang"], type='json', auth="public", methods=['POST'], website=True)
	def website_langauge(self, code, **kw):
		lang_id = request.env['res.lang'].search([('code','=',code.replace('-','_'))])
		return {
			'sep_format': lang_id.grouping,
			'decimal_point': lang_id.decimal_point,
			'thousands_sep': lang_id.thousands_sep
		}


	def checkout_redirection(self, order):
# 		minimum_order_value = 1 if not request.website.minimum_order_value else request.website.minimum_order_value
		minimum_order_value = request.website.minimum_order_value
		if order.amount_total < minimum_order_value:
			return request.redirect('/shop/cart')
		return super(website_sale, self).checkout_redirection(order)
