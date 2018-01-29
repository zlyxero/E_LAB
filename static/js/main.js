

jQuery(function() {

    $("#id_test").on('keyup', function(){

        var value = $(this).val();
        $.ajax({
            url: '/system/ajax/autocomplete/',
            data: {
              'search': value 
            },
            dataType: 'json',
            success: function (data) {
                list = data.list;
                $("#id_test").autocomplete({
                source: list,
                minLength: 1 
                });       
            }
        });        
    });

    var wrapper = $(".input_fields_wrap"); //Fields wrapper
    var add_button = $(".add_field_button"); //Add button ID

   	$(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        
        var value = $("#id_test").val();

        //  check if any value was entered
        if(value) {
        
            // check if test is available in database

            $.ajax({
                url: '/system/ajax/testvalue/',
                data: {
                  'test': value 
                },
                dataType: 'json',
                success: function (data) {
                    
                    // if the test is available, add it to form
                    if(data.exists == 1) {

                        $(wrapper).append(`<div><input type="checkbox" name="test" value="${value}" checked> ${value} <a href="#" class="remove_field">Remove</a></div>`); //add input box

                        $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
                        e.preventDefault(); $(this).parent('div').remove(); 
                        
                        });     

                      }   

                    }     
            });    
        }    


     });

 }); 