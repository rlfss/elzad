from odoo import http
from odoo.http import request

class Regoins(http.Controller):
    @http.route(['''/shop/change_branch/<model('website.branches'):br>'''], type='http', auth="public", website=True)
    def pricelist_change(self,br,**post):
        brr  = request.env['website.branches'].sudo().search([('id', '=', br.id)], limit=1)
        pl = brr.pricelist.id
        request.session['website_sale_current_pl'] = pl
        request.session['website_sale_current_br'] = brr.name
        request.website.sale_get_order(force_pricelist=pl)
        return request.redirect(request.httprequest.referrer or '/shop')