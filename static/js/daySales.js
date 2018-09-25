/*
    daySale javascript
*/


$('#sales-write-div').on("click", "#sales-write-btn", function(){
    var btn = $(this);
    $.ajax({
        url: btn.attr("url"), 
        type: 'get', 
        datatype: 'json', 
        beforeSend: function() {
            $.showLoading({name: 'line-scale',allowHide: false});  
        },        
        success: function(data) {
            $.hideLoading();
            Lobibox.notify('success', {
                sound: false,
                delay: 900,
                msg: 'Successfully completed'
            });            
        },
        error: function(error) {
            alert(error);
        }
    })
});