/*
    2018-09-13
    reference source: https://simpleisbetterthancomplex.com
    modified by han

    django payment.view with Ajax 
*/

$(function () {
    //Search student by name
    var search = function () {
        var btn = $(this);
        $.ajax({
            // Ajax 정보입력
            url: btn.attr("url"), // request를 보낼 url urls.py에 등록된 주소로 하여야함 name 파라미터 값 사용 불가능
            type: 'post', // request 방식
            datatype: 'json', // 전달할 데이터 방식
            data: { // request 요청시 전달되는 데이터 json형식
                'name' : $('.input-student-name').val(), // 해당 요소의 값을 저장
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val() // 크로스오버 공격방지    
            },  
            success: function(data) { // 서버에 전송한 request가 수행되고 서버로 부터 결과를 받은 경우
                if(data.form_is_valid){
                    $('#table-student tbody').html(data.student_list); // 서버에서 html형식에 데이터를 넣어주면 그것을 html에 출력함
                    $("#table-payment tbody").html();
                } else {
                    $('#table-student tbody').html(data.student_list);
                    $("#table-payment tbody").html();
                    Lobibox.notify('warning', {
                        sound: false,
                        delay: 900,
                        msg: '오류 발생'
                    });
                }
            },
            error: function(error) { // 오류가 난 경우
                alert(error);
            }
        });
    };

    var inquire = function () {
        var btn = $(this);
        $.ajax({
            // Ajax 정보입력
            url: btn.attr("data-url"), 
            type: 'get', 
            datatype: 'json', 
            success: function(data) { 
                if(data.form_is_valid){
                    $('#table-student tbody').html(data.student_list); 
                    $("#table-payment tbody").html(data.payment_list);
                } else {
                    $('#table-student tbody').html(data.student_list);
                    $("#table-payment tbody").html(data.payment_list);
                    Lobibox.notify('warning', {
                        sound: false,
                        delay: 900,
                        msg: '오류 발생'
                    });
                }
            },
            error: function(error) { // 오류가 난 경우
                alert(error);
            }
        });
    };

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-payment").modal("show");
            },
            success: function (data) {
                $("#modal-payment .modal-content").html(data.html_form);
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
                    $("#table-student tbody").html(data.student_list);
                    $("#table-payment tbody").html(data.payment_list);
                    $("#modal-payment").modal("hide");  // <-- Close the modal
                    Lobibox.notify('success', {
                        sound: false,
                        delay: 900,
                        msg: '정상적으로 등록되었습니다.'
                    });
                }
                else {
                    $("#modal-payment .modal-content").html(data.html_form);
                    Lobibox.notify('warning', {
                        sound: false,
                        delay: 900,
                        msg: '오류 발생'
                    });
                }
            }
        });
        return false;
    };


  //Search student
  $('#div-student-search').on("click", ".js-student-search", search);

  //Inquire payment
  $("#table-student").on('click', ".js-inquire-payment", inquire);
  
  // Create payment
  $("#table-student").on('click', ".js-register-payment", loadForm);
  $("#modal-payment").on("submit", ".js-payment-register-form", saveForm);

  // Update payment
  $("#table-payment").on("click", ".js-update-payment", loadForm);
  $("#modal-payment").on("submit", ".js-payment-update-form", saveForm);

  // Delete payment
  $("#table-payment").on("click", ".js-delete-payment", loadForm);
  $("#modal-payment").on("submit", ".js-payment-delete-form", saveForm);
});
