(function ($) {
	"use strict";
	$(document).ready(function () {
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