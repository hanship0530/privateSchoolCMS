/*
    Register Lesson
    2018-09-08 
    resource from simpleisbetterthancomplex.com
*/
$(function () {
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-lesson").modal("show");
            },
            success: function (data) {
                $("#modal-lesson .modal-content").html(data.html_form);
            }
        });
    };
  
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#lesson-table tbody").html(data.lesson_list);  // <-- Replace the table body
                    $("#modal-lesson").modal("hide");  // <-- Close the modal
                    Lobibox.notify('success', {
                        sound: false,
                        delay: 900,
                        msg: '정상적으로 등록되었습니다.'
                    });
                }
                else {
                    $("#modal-lesson .modal-content").html(data.html_form);
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


  /* Binding */

  // update lesson 
  $("#lesson-table").on("click", ".js-update-lesson", loadForm);
  $("#modal-lesson").on("submit", ".js-lesson-update-form", saveForm);

  // delete lesson
  $("#lesson-table").on("click", ".js-delete-lesson", loadForm);
  $("#modal-lesson").on("submit", ".js-lesson-delete-form", saveForm);
});