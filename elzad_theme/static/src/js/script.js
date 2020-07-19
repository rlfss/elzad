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
			nav: true,
			dots: false,
			navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
		});

		$('a[href="#search-button"]').on("click", function (event) {
			$("#search-box").addClass("open");
			$('#search-box > form > input.search-input').focus();
		});
		$("#search-box, #search-box button.close").on("click keyup", function (event) {
			if (
				event.target == this ||
				event.target.className == "close" ||
				event.keyCode == 27
			) {
				$(this).removeClass("open");
			}
		});
		$("#search-box form").submit(function (event) {
			$("#search-box").removeClass("open");
		});

        $('[data-toggle="collapse"]').on('mouseenter', function() {
            var controls = $(this)[0].getAttribute("aria-controls")
            $(this).parents('.s_categs_home').find('#'+controls).collapse('show');
        });


	});
})
(jQuery); // End of use strict