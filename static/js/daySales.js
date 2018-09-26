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
            if(data.is_valid){
                $('#sheet-select').html(data.sheets);
                Lobibox.notify('success', {
                    sound: false,
                    delay: 900,
                    msg: 'Successfully completed'
                }); 
            }
            else{
                $('#sheet-select').html(data.sheets);
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

$('#sales-inquire-div').on("click", "#sales-inquire-btn", function(){
    var btn = $(this);
    $.ajax({
        url: btn.attr("url"), 
        type: 'post', 
        datatype: 'json',
        data: {
            'sheet': $('#sheet-select').val(),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
        },     
        success: function(data) {
            $('#payment-card-h4').html(data.paymentCard);
            $('#payment-cash-h4').html(data.paymentCash);
            $('#refund-card-h4').html(data.refundCard);
            $('#refund-cash-h4').html(data.refundCash);
            $('#total-sale-h4').html(data.total);
            $('#sheet-select').html(data.sheets);
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