/*
    Register Student Part
    error: notify is not working
*/
$(function () {
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("url"),
            type: 'post',
            dataType: 'json',
            data: {
                'number': btn.attr("data-id"),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            beforeSend: function () {
                $("#modal-student").modal("show");
            },
            success: function (data) {
                $("#modal-student .modal-content").html(data.html_form);
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
                    $("#student-table tbody").html(data.studentList);  
                    $("#modal-student").modal("hide");  
                    Lobibox.notify('success', {
                        sound: false,
                        delay: 900,
                        msg: '정상적으로 수정되었습니다.'
                    });                    
                }
                else {
                    $("#modal-student .modal-content").html(data.html_form);
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

  // Update Student
  $("#student-table").on("click", ".js-update-student", loadForm);
  $("#modal-student").on("submit", ".js-student-update-form", saveForm);

  // Delete book
  $("#student-table").on("click", ".js-delete-student", loadForm);
  $("#modal-student").on("submit", ".js-student-delete-form", saveForm);
});