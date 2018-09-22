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
                  Lobibox.notify('success', {
                    sound: false,
                    delay: 900,
                    msg: '정상적으로 등록되었습니다.'
                  });
                  $('#register-page-div').html(data.form_html);
                }
                else {
                  $('#register-page-div').html(data.form_html);
                  Lobibox.notify('warning', {
                    sound: false,
                    delay: 900,
                    msg: '형식에 오류가 있습니다.'
                  });
                }
            }
        });
        return false;
    };
  $("#register-page-div").on("submit", ".js-student-register-form", saveForm);
});