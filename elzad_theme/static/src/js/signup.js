(function ($) {
	"use strict";

    $(document).ready(function () {
        var tmp_company = '<div class="col-md-8">'+
                                '<div class="form-group field-name">'+
                                    '<label for="name">The Company\'s name</label>'+
                                    '<input type="text" name="name" t-att-value="name" id="name"'+
                                           'class="form-control form-control-md"'+
                                           'required="required" t-att-readonly="readonly if only_passwords else None"'+
                                           't-att-autofocus="autofocus if login and not only_passwords else None"/>'+
                                '</div>'+
                            '</div>'+
                            '<div class="col-md-4">'+
                                '<div class="form-group field-login">'+
                                    '<label for="login">Email</label>'+
                                    '<input type="text" name="login" t-att-value="login" id="login"'+
                                           'class="form-control form-control-md" autofocus="autofocus"'+
                                           'autocapitalize="off" required="required"'+
                                           't-att-readonly="readonly if only_passwords else None"/>'+
                                '</div>'+
                            '</div>'+
                            '<div class="col-md-4">'+
                                '<div class="form-group field-vat">'+
                                    '<label for="vat">Tax ID</label>'+
                                    '<input type="text" name="vat" t-att-value="vat" id="vat"'+
                                           'class="form-control form-control-md" autofocus="autofocus"'+
                                           'autocapitalize="off" required="required"'+
                                           't-att-readonly="readonly if only_passwords else None"/>'+
                                '</div>'+
                            '</div>'+
                            '<div class="col-md-4">'+
                                '<div class="form-group field-title">'+
                                    '<label for="title">Title</label>'+
                                    '<input type="text" name="title" t-att-value="title" id="title"'+
                                           'class="form-control form-control-md" autofocus="autofocus"'+
                                           'autocapitalize="off" required="required"'+
                                           't-att-readonly="readonly if only_passwords else None"/>'+
                                '</div>'+
                            '</div>'+
                            '<div class="col-md-4">'+
                                '<div class="form-group field-password">'+
                                    '<label for="password">Password</label>'+
                                    '<input type="password" name="password" id="password" class="form-control form-control-md"'+
                                           'required="required" t-att-autofocus="autofocus if only_passwords else None"/>'+
                                '</div>'+
                            '</div>'+
                            '<div class="col-md-4">'+
                                '<div class="form-group field-confirm_password">'+
                                    '<label for="confirm_password">Confirm Password</label>'+
                                    '<input type="password" name="confirm_password" id="confirm_password"'+
                                           'class="form-control form-control-md" required="required"/>'+
                                '</div>'+
                            '</div>'+
                            '<div class="col-md-4">'+
                                '<div class="form-group field-phone">'+
                                    '<label for="phone">Phone</label>'+
                                    '<input type="text" name="phone" t-att-value="phone" id="phone" required="required"'+
                                           'class="form-control form-control-md" autofocus="autofocus"'+
                                           'autocapitalize="off"'+
                                           't-att-readonly="readonly if only_passwords else None"/>'+
                                '</div>'+
                            '</div>'
        var tmp_person =    '<div class="col-md-4">'+
                            '<div class="form-group field-first_name">'+
                            '<label for="first_name">FirstName</label>'+
                            '<input type="text" name="first_name" t-att-value="first_name" id="first_name"'+
                            'class="form-control form-control-md"'+
                            'required="required" t-att-readonly="readonly if only_passwords else None"'+
                            't-att-autofocus="autofocus if login and not only_passwords else None"/>'+
                            '</div></div>'+
                            '<div class="col-md-4">'+
                            '<div class="form-group field-last_name">'+
                            '<label for="last_name">LastName</label>'+
                            '<input type="text" name="last_name" t-att-value="last_name" id="last_name"'+
                            'class="form-control form-control-md"'+
                            'required="required" t-att-readonly="readonly if only_passwords else None"'+
                            't-att-autofocus="autofocus if login and not only_passwords else None"/>'+
                            '</div></div>'+
                            '<div class="col-md-4">'+
                            '<div class="form-group field-login">'+
                            '<label for="login">Email</label>'+
                            '<input type="text" name="login" t-att-value="login" id="login"'+
                            'class="form-control form-control-md" autofocus="autofocus"'+
                            'autocapitalize="off" required="required"'+
                            't-att-readonly="readonly if only_passwords else None"/>'+
                            '</div></div>'+
                            '<div class="col-md-4">'+
                            '<div class="form-group field-password">'+
                            '<label for="password">Password</label>'+
                            '<input type="password" name="password" id="password" class="form-control form-control-md"'+
                            'required="required" t-att-autofocus="autofocus if only_passwords else None"/>'+
                            '</div></div>'+
                            '<div class="col-md-4">'+
                            '<div class="form-group field-confirm_password">'+
                            '<label for="confirm_password">Confirm Password</label>'+
                            '<input type="password" name="confirm_password" id="confirm_password"'+
                            'class="form-control form-control-md" required="required"/>'+
                            '</div></div>'+
                            '<div class="col-md-4">'+
                            '<div class="form-group field-phone">'+
                            '<label for="phone">Phone</label>'+
                            '<input type="text" name="phone" t-att-value="phone" id="phone" required="required"'+
                            'class="form-control form-control-md" autofocus="autofocus"'+
                            'autocapitalize="off"'+
                            't-att-readonly="readonly if only_passwords else None"/>'+
                            '</div></div>'+
                            '<div class="col-md-4">'+
                            '<div class="form-group field-sex field-radio">'+
                            '<label for="sex"></label>'+
                            '<div class="d-flex">'+
                            '<div class="mr-10">'+
                            '<input type="radio" id="male" name="sex" value="male" checked="checked"'+
                            'required="required"'+
                            't-att-readonly="readonly if only_passwords else None"/>'+
                            '<label for="male" class="form-control form-control-md">Male</label>'+
                            '</div><div>'+
                            '<input type="radio" id="female" name="sex" value="female" required="required"'+
                            't-att-readonly="readonly if only_passwords else None"/>'+
                            '<label for="female" class="form-control form-control-md">Female</label>'+
                            '</div></div></div></div>'+
                            '<div class="col-md-4">'+
                            '<div class="form-group field-date_of_birth">'+
                            '<label for="phone">Date of birth</label>'+
                            '<input type="date" name="date_of_birth" id="date_of_birth"'+
                            'class="form-control form-control-md" autofocus="autofocus"'+
                            'autocapitalize="off" required="required"'+
                            't-att-readonly="readonly if only_passwords else None"/>'+
                            '</div></div>'

        var cfs = document.getElementById("content_form_signup");
        cfs.innerHTML = tmp_company
        $('#company').on("click", function (event) {
            cfs.innerHTML = tmp_company
		});
        $('#person').on("click", function (event) {
            cfs.innerHTML=  tmp_person
		});

		$('#acceptterms').on("click", function (event) {
            var btnsignup = document.getElementById("btnsignup");
            console.log('$(this) = ',$(this))
            if ($(this)[0].checked == true)
            {
                btnsignup.disabled = false;
            }
            else
            {
                btnsignup.disabled = true;
            }
        });

    });

})
(jQuery); // End of use strict