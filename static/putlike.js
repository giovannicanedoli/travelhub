/*
javascript manda una richiesta al server

il server verifica se l'utente è loggato e se la primary key esiste

se l'utente è loggato allora si può mandare un valora a js che provvede a 
 "mettere" il like e dopo a levarlo passata na certa

se l'utente non è loggato allora non si manda un altro valora a js che 
provvede a mostrare un altro messaggio di errore
*/

$(document).ready(function() {

    $('.like.pulsante').click(function() {
        var pkey = $(this).val(); 
        
        var heart = document.getElementById('cuore' + pkey);
        
        $.ajax({
            url: "/leavealike",
            type: 'POST',
            data: {
                'primarykey': pkey, //mando la primary al server
            }, 

            dataType: 'json',
            success: function(data) {
                var code = data.code;
                if(code === '200'){
                    heart.style.visibility = "visible";
                    
                    setTimeout(function(){
                        heart.style.visibility = "hidden";
                    },300);
                }else{
                    console.log("ENSOMMA..."); //mostrare qui a schermo qualcosa che indica che deve loggarsi
                }

            },

            error: function(jqXHR, textStatus, errorThrown) { 

                console.error('Error: ' + textStatus, errorThrown);
            }
        });
    });

    $('.like.pulsante2').click(function() {
        var pkey = $(this).val(); 
        
        var bookmark = document.getElementById('segnalibro' + pkey);
        
        $.ajax({
            url: "/savephoto",
            type: 'POST',
            data: {
                'primarykey': pkey, //mando la primary al server
            }, 

            dataType: 'json',
            success: function(data) {
                var code = data.code;
                if(code === '200'){
                    bookmark.style.visibility = "visible";
                    
                    setTimeout(function(){
                        bookmark.style.visibility = "hidden";
                    },300);
                }else{
                    console.log("ENSOMMA..."); //mostrare qui a schermo qualcosa che indica che deve loggarsi
                }
                
            },

            error: function(jqXHR, textStatus, errorThrown) { 

                console.error('Error: ' + textStatus, errorThrown);
            }
        });
    });

    $(".foto").dblclick(function(){
        var pkey = $(this).data('value'); 
        //alert(pkey);

        var heart = document.getElementById('cuore' + pkey);
        
        $.ajax({
            url: "/leavealike",
            type: 'POST',
            data: {
                'primarykey': pkey, //mando la primary al server
            }, 

            dataType: 'json',
            success: function(data) {
                var code = data.code;
                if(code === '200'){
                    heart.style.visibility = "visible";
                    
                    setTimeout(function(){
                        heart.style.visibility = "hidden";
                    },300);
                }else{
                    console.log("ENSOMMA..."); //mostrare qui a schermo qualcosa che indica che deve loggarsi
                }

            },

            error: function(jqXHR, textStatus, errorThrown) { 

                console.error('Error: ' + textStatus, errorThrown);
            }
        });
    });

});
