
odoo.define('checkout_custom.website', function (require) {
"use strict";
    var base = require('web_editor.base');
    var ajax = require('web.ajax');    
       
    $('.oe_website_sale').each(function () {
        var oe_website_sale = this;
        $(oe_website_sale).on('click', '.btn.btn-primary.pull-right.mb32', function (ev)
        {
            var conf_value = $(this).find('.cart_values').attr('conf_value');
            var cart_value = $('#order_total>:last>span>span').text();
            var cart_value = cart_value.replace(",", "");
            var cart_value = parseFloat(cart_value);
            var currency_symbol = $(this).find('.cart_values').attr('currency_symbol');
            var $link = $(this);
            setTimeout(function() {$link.popover('destroy')},3000);
            if (cart_value < conf_value)
            {
                ev.preventDefault(); 
                $(this).popover({
                  content:"A minimum purchase total of "+ currency_symbol+" "+ conf_value+" is required to validate your order, current purchase total is "+ currency_symbol+" "+ cart_value,
                  title:"WARNING",
                  placement:"top",
                  trigger:'focus',
                });
                $(this).popover('show');
            }
        });


       
	});
});
