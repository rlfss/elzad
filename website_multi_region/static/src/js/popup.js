//Pop up Modal JS

jQuery(function($) {

        var object_iframe =
            $("#popup-modal").find("iframe");
        var object_iframe_src =
            object_iframe.attr("src");
        var cookieName = 'yourcookiename';
        $(document).ready( function(e) {
               checkCookie();
            });

			function checkCookie() {
			    if (document.cookie.length > 0 && document.cookie.indexOf(cookieName + '=') != -1) {
			            // do nothing, cookie already sent
			    } else {
			            // handle jQuery animation

			    $("#popup-modal").not(".chch_shown").show("fast");
                jQuery(document).trigger("popup-modal-opened");
                $("#popup-modal").addClass("chch_shown");

			            // set the cookie to show user has already visited
			            document.cookie = cookieName + "=1";
			    }
			}
        jQuery(document).on("popup-modal-opened", function() {
            var winheight = $(window).height();
            var modalheight = $("#popup-modal").outerHeight();
            var modaltop = (winheight - modalheight) / 2;
            if (winheight > modalheight) {
                $("#popup-modal").css("top", modaltop);
            } else {
                $("#popup-modal").css("top", "");
            }
        });
        jQuery(window).resize(function() {
            jQuery(document).trigger("popup-modal-opened");
        });
        $('#popup-modal').find('img').on('load error', function() {
            $(this).trigger('popup-modal-opened');
        });
        $("#popup-modal .cc-pop-up__close").click(function() {
        	//window.close();
        	$('.cc-pop-up__bg').css("display", "none");
        	$('.cc-pop-up__article').css("display", "none");
        });
});

/* Contact (right) Popup */

$(document).ready(function() {
	$("#closeWidget").click(function() {
		$("#widgetContent").fadeOut("slow");
		// jQuery( "#widgetContent" ).toggle( "slide" );
	});
});
$(document).ready(function() {
	$("#pullWidget").click(function() {
		$("#widgetContent").fadeIn("slow");
		// jQuery( "#widgetContent" ).toggle( "slide" );
	});
});

$(document).ready(function() {
	$("#toggleSearch").click(function() {
		$(".searchBox").slideToggle("slow");
		$(this).toggleClass("active");
		// jQuery( "#widgetContent" ).toggle( "slide" );
	});
});

