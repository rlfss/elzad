(function ($) {
	"use strict";
	$(document).ready(function () {
		$('.owl-quick-access').owlCarousel({
			loop: true,
			margin: 5,
			nav: true,
			dots: false,
			responsive: {
				0: {
					items: 1
				},
				300: {
					items: 2
				},
				576: {
					items: 3
				},
				768: {
					items: 4
				},
				992: {
					items: 5
				},
				1200: {
					items: 6
				}
			},
			navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
		})
		$('.owl-slider-home').owlCarousel({
			items: 1,
			nav: true,
			navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
		});
		$('.owl-product-home').owlCarousel({
			items: 4,
			margin: 5,
			nav: true,
			dots: false,
			navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            responsive: {
				0: {
					items: 1
				},
				576: {
					items: 2
				},
				992: {
					items: 4
				}
			},
		});
	});
})
(jQuery); // End of use strict