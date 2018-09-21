/*
    Register Lesson Part
*/
$(function () {
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                  $('.top-right').notify({message: { text: "Registered Successfully!" }}).show();
                  $('#register-page-div').html(data.form_html);
                }
                else {
                  $('#register-page-div').html(data.form_html);
                  $('.top-right').notify({
                    type: 'danger',
                    message: "Registering is fail!" }).show();
                }
            }
        });
        return false;
    };
  $("#register-page-div").on("submit", ".js-lesson-register-form", saveForm);
});