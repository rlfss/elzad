from odoo import http
from odoo.http import request

class Regoins(http.Controller):
    @http.route(['''/shop/change_pricelist<model('website.branches'):br>'''], type='http', auth="public", website=True)
    def pricelist_change(self,br,**post):
        pl = br
        if (pl.selectable or pl == request.env.user.partner_id.property_product_pricelist) \
                and request.website.is_pricelist_available(pl.id):
            request.session['website_sale_current_pl'] = pl
            # request.session['website_sale_current_br'] = br.name
            request.website.sale_get_order(force_pricelist=pl)
        return request.redirect(request.httprequest.referrer or '/shop')