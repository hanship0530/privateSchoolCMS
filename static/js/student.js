/*
    Register Student Part
*/
$(function () {
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
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
                }
                else {
                    $("#modal-student .modal-content").html(data.html_form);
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