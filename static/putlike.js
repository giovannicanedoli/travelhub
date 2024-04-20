// function showHeart(cuore, cityname, citydescription) {
//     var heart = document.getElementById(cuore);
    
//     heart.style.visibility = "visible";
    
//     // setTimeout(function() {
//     //     heart.style.visibility = "hidden";
//     // }, 300);

//     $.ajax({
//         //qui devo mandare altri dati, utente e città a cui o messo
//         // mi piace con relativi dati annessi

//         url: "update_data",
//         type: "POST",

//         data: {
//             cityid:cityid,
//             cityname:cityname,
//             citydescription:citydescription
//         },
        
//         success: function(resp){
//             $('div#response').append(resp.data);
//         }
//     });

// }

$(document).ready(function() {

    $('.like.pulsante').click(function() {
        //alert("btn prssed!" + $(this).val());
        var param = $(this).val(); 
        
        var heart = document.getElementById('cuore' + param);
        heart.style.visibility = "visible";
        
        $.ajax({
            url: 'update_data/',
            type: 'POST',
            data: {
                cityid: param, //mando la primary al server
            }, // Data to send in the request.

            dataType: 'json', // The type of data you're expecting back from the server.
            success: function(data) { // Function to call if the request succeeds.
                console.log(data);
                alert("ao ho ricevuto");
            },
            error: function(jqXHR, textStatus, errorThrown) { // Function to call if the request fails.
                console.error('Error: ' + textStatus, errorThrown);
            }
        });
    });
});
