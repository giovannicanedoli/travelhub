/*
javascript manda una richiesta al server

il server verifica se l'utente è loggato e se la primary key esiste

se l'utente è loggato allora si può mandare un valora a js che provvede a 
 "mettere" il like e dopo a levarlo passata na certa

se l'utente non è loggato allora non si manda un altro valora a js che 
provvede a mostrare un altro messaggio di errore
    
PD

*/

$(document).ready(function() {

    $('.like.pulsante').click(function() {
        var pkey = $(this).val(); 
        
        var heart = document.getElementById('cuore' + pkey);
        heart.style.visibility = "visible";
        
        $.ajax({
            url: "/update_data",
            type: 'POST',
            data: {
                'primarykey': pkey, //mando la primary al server
            }, 

            dataType: 'json',
            success: function(data) { 
                heart.style.visibility = "hidden";
            },

            error: function(jqXHR, textStatus, errorThrown) { 

                console.error('Error: ' + textStatus, errorThrown);
            }
        });
    });
});
