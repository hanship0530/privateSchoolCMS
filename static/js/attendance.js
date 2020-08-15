/*

*/
$('#student-search-div').on("click", "#student-search-btn", function(){
    var btn = $(this);
    $.ajax({
        // Ajax 정보입력
        url: btn.attr("url"), 
        type: 'post', 
        datatype: 'json', 
        data: { 
            'name' : $('#student-name-input').val(), 
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val() // 크로스오버 공격방지    
        }, 	
        success: function(data) { 
            if(data.is_valid){
                $('#student-table tbody').html(data.studentList); 
            } else {
                  Lobibox.notify('warning', {
                    sound: false,
                    delay: 900,
                    msg: data.errorMsg
                  }); 
            }
        },
        error: function(error) { 
            alert(error);
        }
    })
});

//display student chart naming compltedt
$('#student-div').on('click', '#display-table-btn', function(){
    var btn = $(this);
    $.ajax({
        // Ajax 정보입력
        url: btn.attr("url"), 
        type: 'post', 
        datatype: 'json', 
        data: { 
            'number' : btn.attr("data-id"),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val() // 크로스오버 공격방지    
        },  
        success: function(data) { 
            if(data.is_valid) {
                $('#student-table tbody').html(data.studentList); 
                $('#attendance-table tbody').html(data.attendLists);
                  Lobibox.notify('success', {
                    sound: false,
                    delay: 900,
                    msg: 'Successfully completed.'
                  });    
            }
            else {
                  Lobibox.notify('warning', {
                    sound: false,
                    delay: 900,
                    msg: data.errorMsg
                  }); 
            }            
        },
        error: function(error) { 
            alert(error);
        }
    })
});

//register student attendance card
$('#student-div').on('click', '#register-attendCard-btn', function(){
    var btn = $(this);
    $.ajax({
        url: btn.attr("url"), 
        type: 'post', 
        datatype: 'json', 
        data: { 
            'number' : btn.attr("data-id"),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()   
        },
        beforeSend: function () {
            $('body').loadingModal({
                text: 'Please tag Card! Detecting Card',
                color: '#fff',
                backgroundColor: 'rgb(0,0,0)',
                animation: 'doubleBounce'
            });
        },          
        success: function(data) { 
            $('body').loadingModal('hide');
            Lobibox.notify('success', {
                sound: false,
                delay: 900,
                msg: data.successMessageAjax
            });            
        },
        error: function(error) { 
            alert(error);
        }
    })
});

$('#attendance-div').on('click', '#update-attendance-btn', function() {
    var btn = $(this);
    $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
            $("#modal-attendance").modal("show");
        },
        success: function (data) {
            $("#modal-attendance .modal-content").html(data.html_form);
        },
        error: function(error) {
            alert(error);
        }        
    });
})

// $('#modal-attendance').on('submit', '#js-attendance-update-form', function() {
//     var form = $(this);
//     console.log(form.serialize());
//     $.ajax({
//         url: form.attr("action"),
//         data: form.serialize(),
//         type: form.attr("method"),
//         dataType: 'json', 
//         success: function (data) {
//             if (data.form_is_valid) {
//                 $("#student-table tbody").html(data.studentList);  
//                 $("#attendance-table tbody").html(data.attendLists);  
//                 $("#modal-attendance").modal("hide");  
//                 Lobibox.notify('success', {
//                     sound: false,
//                     delay: 900,
//                     msg: 'Successfully completed.'
//                 });                    
//             }
//             else {
//                 $("#modal-attendance .modal-content").html(data.html_form);
//                 Lobibox.notify('warning', {
//                     sound: false,
//                     delay: 900,
//                     msg: data.errorMsg
//                 });                    
//             }
//         },
//         error: function(error) {
//             alert(error);
//         }
//     });
// })