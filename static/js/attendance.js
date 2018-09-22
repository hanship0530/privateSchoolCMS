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
                    msg: '정상적으로 등록되었습니다.'
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

// AttendanceTable Edting Part
// $('#lesson-table-list-div').on('click', '#update-table-btn', function() {
//     var btn = $(this);
//     var tr = btn.parent().parent();
//     var td = tr.children();
//     var input = td.children();
//     var number = input.eq(0).val();
//     var date = input.eq(1).val();
//     var content = input.eq(2).val();
//     var completed = input.eq(3).val();
//     var memo = input.eq(4).val();
//     var cells = input.eq(5).val();
//     var sheetName = input.eq(6).val();
//     var studentNumber = input.eq(7).val();      
//     $.ajax({
//         url: btn.attr("url"),
//         type: 'post',
//         datatype: 'json',
//         data: {
//             'number': studentNumber,
//             'date': date,
//             'content': content,
//             'completed': completed,
//             'memo': memo,
//             'cells': cells,
//             'sheetName': sheetName,
//             'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
//         },
//         success: function(data) {
//             if(data.isSuccess) {
//                 $('#lesson-table tbody').html(data.lessontable_html);
//                 $('.top-left').notify({message: { text: data.message }}).show(); 
//             } else{
//                 $('.top-left').notify({
//                     type: 'danger',
//                     message: { text: data.message }}).show(); 
//             }           
//         },
//         error: function(e) {
//             alert(e);
//         }
//     })
// })
