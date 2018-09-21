// Made by Han
$('#date-search-div').on('click', '#schedule-search', function(){
    var sp = $(this);
    $.ajax({
        url: sp.attr("url"),
        type: 'post',
        datatype: 'json',
        data: {
            'daymonthyear': $('#search-date').val(),
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
            $('.schedule-table tbody').html(data.scheduleTable);
        },
        error: function(e) {
            alert(e);
        }
    })
});
$('.schedule-table').on('click', '.update-schedule-btn', function(){
    var btn = $(this);
    var tr = btn.parent().parent();
    var td = tr.children();
    var input = td.children();
    var number = input.eq(0).val();
    var name = input.eq(1).val();
    var grade = input.eq(2).val();
    var memo = input.eq(3).val();
    var cellInfo = input.eq(4).val();
    var sheet = input.eq(5).val();
    var day = input.eq(6).val();

    $.ajax({
        url: btn.attr("url"),
        type: 'post',
        datatype: 'json',
        data: {
            'number': number,
            'name': name,
            'grade': grade,
            'memo': memo,
            'cellInfo': cellInfo,
            'sheet': sheet,
            'day': day,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
            if(data.is_valid == true){
                $('.schedule-table tbody').html(data.scheduleTable);
                $('.top-right').notify({message: { text: "Success!" }}).show();
            }
            else {
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
$('.schedule-table').on('click', '.attend-lesson-btn', function(){
    var btn = $(this);
    var tr = btn.parent().parent();
    var td = tr.children();
    var input = td.children();
    var number = input.eq(0).val();
    $.ajax({
        url: btn.attr("url"),
        type: 'post',
        datatype: 'json',
        data: {
            'number': number,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
            if(data.is_valid == true){
                $('.top-right').notify({message: { text: "Success!" }}).show();
            }
            else {
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
