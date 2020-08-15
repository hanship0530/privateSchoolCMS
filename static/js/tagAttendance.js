//$('#tagCard-div').on("click", "#attend-now-btn", function(){
$( document ).ready(function() {
    var btn = $('#tagCard-url-input');
    console.log(btn.attr('url'));
    $.ajax({
        url: btn.attr("url"),
        type: 'post', 
        datatype: 'json', 
        timeout: 10000,
        data: { 
            'number' : "nothing",
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()   
        },
        beforeSend: function () {
            $('#notice').html('Prepare Your Card');
            // $('body').loadingModal({
            //     text: 'Please tag your Card to Card Reader!',
            //     color: '#fff',
            //     backgroundColor: 'rgb(0,0,0)',
            //     animation: 'doubleBounce'
            // });
        },          
        success: function(data) { 
            $('body').loadingModal('hide');
            $('#notice').html(data.attendanceInformation);
            window.location.href = btn.attr("url");       
        },
        error: function(error) {
            console.log(error); 
        }
    })	
});
    