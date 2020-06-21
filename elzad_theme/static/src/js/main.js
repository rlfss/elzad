// slider

$('.slider-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.slider-nav'
});
$('.slider-nav').slick({
    slidesToScroll: 4,
    asNavFor: '.slider-for',
    dots: false,
    slidesToShow: 5,
    centerMode: false,
    focusOnSelect: true,
    prevArrow: $('.prev'),
    nextArrow: $('.next'),
    responsive: [
        {
            breakpoint: 1024,
            settings: {
                slidesToShow: 5,
                slidesToScroll: 4,
            }
        },
        {
            breakpoint: 600,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 2
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        }

    ]
});

$('.slider-for2').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.slider-nav2'
});
$('.slider-nav2').slick({
    slidesToScroll: 2,
    asNavFor: '.slider-for2',
    dots: false,
    slidesToShow: 3,
    centerMode: false,
    focusOnSelect: true,
    prevArrow: $('.prev'),
    nextArrow: $('.next'),
    responsive: [
        {
            breakpoint: 1024,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 600,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 2
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }

    ]
});
//input width auto
$(document).ready(function () {
    var resizeInput = $('input.resizeInput');
    if($('input').hasClass('resizeInput')){
        resizeInput.width(resizeInput.val().length + "ch");
        resizeInput.on('input', function () {
            $(this).width($(this).val().length + "ch");
        });
    }
     // get the input element

});

//plus-btnValue minus-btnValue
$(document).ready(function () {
    $(document).on('click', '.minus-btn, .plus-btn', function (e) {
        var $this = $(e.target),
            input = $this.parent().find('.number-cunt'),
            v = $this.hasClass('minus-btn') ? input.val() - 1 : input.val() * 1 + 1,
            min = input.attr('data-min') ? input.attr('data-min') : 1,
            max = input.attr('data-max') ? input.attr('data-max') : false;
        if (v >= min) {
            if (!max == false && v > max) {
                return false
            } else input.val(v);
        }
        e.preventDefault();
    });
    $(document).on('change', '.number-cunt', function (e) {
        var input = $(e.target),
            min = input.attr('data-min') ? input.attr('data-min') : 1,
            max = input.attr('data-max'),
            v = input.val();
        if (v > max) input.val(max);
        else if (v < min) input.val(min);
    });
});

$(window).load(function() {
    $(".loading-overly").fadeOut(1500,
        function () {
            $(this).remove();
            $('body').removeClass('overflow-hidden')
        });
});
//validation
$("#i_form").validate({
    rules: {
        customCheck1: 'required',
        customCheck2: 'required',
        customCheck3: 'required',
        i_password: "required",
        i_c_password: {
            equalTo: "#password"
        }
    },
    messages: {
        customCheck1: 'You must agree to the terms',
        customCheck2: 'You must agree to the terms',
        customCheck3: 'You must agree to the terms',
        i_c_password: {
            equalTo: "Password does not match."
        }
    }
});
$("#p_form").validate({
    rules: {
        customCheck4: 'required',
        customCheck5: 'required',
        customCheck6: 'required',
        p_password: "required",
        p_c_password: {
            equalTo: "#password"
        }
    },
    messages: {
        customCheck4: 'You must agree to the terms',
        customCheck5: 'You must agree to the terms',
        customCheck6: 'You must agree to the terms',
        p_c_password: {
            equalTo: "Password does not match."
        }
    }
});
$('#login_form').validate({});
$('#contact_form').validate({});
$('#card_form').validate({});

//datepicker
$('[data-toggle="datepicker"]').datepicker();
