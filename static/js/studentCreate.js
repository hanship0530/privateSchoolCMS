/*
    Register Student Part
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
                  Lobibox.notify('warning', {
                    sound: false,
                    delay: 900,
                    msg: '형식에 오류가 있습니다.'
                  });
                  // $('.top-right').Lobibox.notify({
                  //   type: 'danger',
                  //   message: "Registering is fail!" }).show();
                }
            }
        });
        return false;
    };
  $("#register-page-div").on("submit", ".js-student-register-form", saveForm);
});