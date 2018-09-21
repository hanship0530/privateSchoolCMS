/*
    Lesson table javascript
*/


// chart searching base on student's name
$('#student-search-div').on("click", "#student-search-btn", function(){
    var btn = $(this);
    $.ajax({
        url: btn.attr("url"), 
        type: 'post', 
        datatype: 'json', 
        data: { // view에 전송할 데이터
            'name' : $('#student-name-input').val(), 
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val() // 크로스오버 공격방지    
        }, 	
        success: function(data) { 
            if(data.is_valid){
                $('#student-table tbody').html(data.studentList); 
                $('#lesson-table tbody').html(data.lessonList);
                $('.top-right').notify({ message: { text: "Success!" } }).show();
            } else {
                $('#student-table tbody').html('');
                $('#lesson-table tbody').html('');;
                $('.top-right').notify({
                    type: 'danger',
                    message: { text: data.errorMsg }}).show();
            }
        },
        error: function(error) {
            alert(error);
        }
    })
});

//create student's new lesson-excel-sheet: copy main sheet to new sheet
//wating effect must be added
$('#student-div').on('click', '#create-table-btn', function(){
    var btn = $(this);
    $.ajax({
        // Ajax 정보입력
        url: btn.attr("url"), 
        type: 'post', 
        datatype: 'json', 
        data: { // view에 전송할 데이터
            'number' : btn.attr("data-id"), 
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val() // 크로스오버 공격방지
        },  
        success: function(data) { 
            if(data.isSuccess) {
                $('#student-table tbody').html(data.studentList); 
                $('#lesson-table tbody').html(' ');                
                $('.top-right').notify({ message: { text: "Success!" }}).show();
            }
            else {
                $('.top-right').notify({
                    type: 'danger',
                    message: { text: data.errorMsg }}).show();                
            }
        },
        error: function(error) { 
            alert(error);
        }
    })
});

// display student's lesson table
$('#student-div').on('click', '#display-table-btn', function(){
    var btn = $(this);
    $.ajax({
        // Ajax 정보입력
        url: btn.attr("url"), 
        type: 'post', 
        datatype: 'json', 
        data: { // view에 전송할 데이터
            'number' : btn.attr("data-id"),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val() // 크로스오버 공격방지    
        },  
        success: function(data) { 
            if(data.is_valid) {
                $('.top-right').notify({message: { text: "Success!" }}).show();
                $('#sheet-select').html(data.worksheets);
                $('#lesson-table tbody').html(data.lessonTable);
                $('#lesson-table-header').html(data.student.name+'('+data.student.number+')의 레슨테이블');
            }
            else {
                $('#student-table').html(' ');
                $('#lesson-table tbody').html(' ');
                $('#lesson-table-header').val('레슨테이블');
                $('.top-right').notify({
                    type: 'danger',
                    message: { text: data.errorMsg }}).show();
            }            
        },
        error: function(error) { 
            alert(error);
        }
    })
});

// remove student from attendance list when completing table writing
$('#student-div').on('click', '#fillout-table-btn', function(){
    var btn = $(this);
    $.ajax({
        // Ajax 정보입력
        url: btn.attr("url"), 
        type: 'post', 
        datatype: 'json', 
        data: { // view에 전송할 데이터
            'number' : btn.attr("data-id"),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val() // 크로스오버 공격방지    
        },  
        success: function(data) { 
            if(data.is_valid) {
                $('#student-table tbody').html(data.studentList); 
                $('#lesson-table tbody').html(' ');                 
                $('.top-right').notify({message: { text: "Success!" }}).show();
            }
            else {
                $('.top-right').notify({
                    type: 'danger',
                    message: { text: data.errorMsg }}).show();
            }            
        },
        error: function(error) { 
            alert(error);
        }
    })
});

// update lesson table
$('#lesson-table-div').on('click', '#update-table-btn', function() {
    var btn = $(this);
    var tr = btn.parent().parent();
    var td = tr.children();
    var input = td.children();
    var number = input.eq(0).val();
    var date = input.eq(1).val();
    var content = input.eq(2).val();
    var completed = input.eq(3).val();
    var memo = input.eq(4).val();
    var cells = input.eq(5).val();
    var sheetName = input.eq(6).val();
    var studentNumber = input.eq(7).val();
    // Ajax 정보입력      
    $.ajax({
        url: btn.attr("url"),
        type: 'post',
        datatype: 'json',
        data: { // view에 전송할 데이터
            'number': studentNumber,
            'date': date,
            'content': content,
            'completed': completed,
            'memo': memo,
            'cells': cells,
            'sheetName': sheetName,
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
            if(data.is_valid) {
                $('#student-table tbody').html(data.studentTable);
                $('#lesson-table tbody').html(data.lessonTable);
                $('.top-right').notify({message: { text: "Success" }}).show(); 
            } else{
                $('.top-right').notify({
                    type: 'danger',
                    message: { text: data.errorMsg }}).show(); 
            }           
        },
        error: function(error) {
            alert(error);
        }
    })
});
$('#lesson-table-div').on('click', '#sheet-select-btn', function() {
    var btn = $(this);
    $.ajax({
        url: btn.attr("url"),
        type: 'post',
        datatype: 'json',
        data: {
            'sheet': $('#sheet-select').val(),
            'number': $('#lesson-table-header').text(),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
            if(data.is_valid){
                $('#lesson-table tbody').html(data.lessonTables);
                $('#sheet-select').html(data.worksheets);
                $('#lesson-table-header h1').html(data.studentNumber);
                $('#student-table tbody').html(data.students);                
            } else {
                $('.top-right').notify({
                    type: 'danger',
                    message: { text: data.errorMsg }}).show();             
            } 
        },
        error: function(e) {
            alert(e);
        }
    })
});