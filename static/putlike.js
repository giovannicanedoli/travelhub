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

    $('likebtn').click(function() {
        alert("btn prssed!");
        // var param = $(this).val(); // This will get the value "myValue"
        // console.log(param); //situazione, non so perché non mi fa l'animazione del bottone il resto dovrebbe essere tutto più o meno risolto
        // var heart = document.getElementById('cuore' + param);
        // heart.style.visibility = "visible";
        // $.ajax({
        //     url: 'https://api.example.com/data', // The URL to the API. You can replace this with your own API path.
        //     type: 'GET', // The type of request you want to make (POST, GET, etc.)
        //     data: { myParam: param }, // Data to send in the request.
        //     dataType: 'json', // The type of data you're expecting back from the server.
        //     success: function(data) { // Function to call if the request succeeds.
        //         console.log(data);
        //     },
        //     error: function(jqXHR, textStatus, errorThrown) { // Function to call if the request fails.
        //         console.error('Error: ' + textStatus, errorThrown);
        //     }
        // });
    });
});
