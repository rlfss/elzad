from odoo.addons.portal.controllers.web import Home
from odoo import http
from odoo.http import request


class WebsiteSort(Home):
    @http.route('/')
    def index(self, **kw):
        super(WebsiteSort, self).index()
        Product = request.env['product.template'].with_context(bin_size=True)
        Category = request.env['product.public.category']

        new_products = Product.search([('is_published', '=', True)], order="create_date DESC", limit=8)
        offers_products = Product.search([('is_published', '=', True), ('is_offers', '=', True)])
        popular_products = Product.search([('is_published', '=', True), ('is_popular', '=', True)])
        categories = Category.search([('parent_id', '=', False)] + request.website.website_domain())
        slider_home = request.env['slider.home'].search([])

        return request.render('website.homepage', {
            'new_products': new_products,
            'offers_products': offers_products,
            'popular_products': popular_products,
            'categories': categories,
            'slider_home': slider_home,
        })
