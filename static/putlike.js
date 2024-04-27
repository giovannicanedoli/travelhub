const animKeyframe = [
    { transform: "rotate(0) scale(1) opacity(0)"  },
    { transform: "rotate(360deg) scale(1)" },
    { transform: "rotate(360deg) opacity(1)" },
    { transform: 'translateY(0px)' },
    { transform: 'translateY(-300px)' },
  ];
const animTiming = {
    duration: 2000,
    iterations: 1,
  };



$(document).ready(function() {

    $('.like.pulsante').click(function() {
        var pkey = $(this).val(); 
        
        var heart = document.getElementById('cuore' + pkey);
        var but = document.getElementById('likebtn' + pkey);
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
                    
                    // heart.style.visibility = "visible";
                    // heart.animate(animKeyframe, animTiming);
                    
                    but.style.backgroundColor = "red";
                    but.style.fontSize = "clamp(1.2rem ,2.8vw, 3.5rem)";
                    setTimeout(function(){
                        heart.style.visibility = "hidden";
                    },2000);

                }
                else if (code === '201') {
                    but.style.backgroundColor = "#efff14";
                    but.style.fontSize = "clamp(0.7rem, 1.3vw, 2rem)";


                }
                else{
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
        
        // var bookmark = document.getElementById('segnalibro' + pkey);
        var sav = document.getElementById('savebtn' + pkey);
        
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
                    // bookmark.style.visibility = "visible";
                    sav.style.backgroundColor = "black";
                    sav.style.color = "white";
                    sav.style.fontSize = "clamp(1.2rem ,2.8vw, 3.5rem)";

                    //ANIMAZIONE
                    setTimeout(function(){
                        bookmark.style.visibility = "hidden";
                    },300);
                }
                else if (code === '202') {
                    sav.style.backgroundColor = "#efff14";
                    sav.style.color = "black";
                    sav.style.fontSize = "clamp(0.7rem, 1.3vw, 2rem)";

                }
                else{
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

        var heart = document.getElementById('cuore' + pkey);
        var but = document.getElementById('likebtn' + pkey);
        
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
                    // heart.style.visibility = "visible";
                    // heart.animate(animKeyframe, animTiming);
 
                    but.style.backgroundColor = "red";
                    but.style.fontSize = "clamp(1.2rem ,2.8vw, 3.5rem)";


                    setTimeout(function(){
                        heart.style.visibility = "hidden";
                    },2000);

                }
                else if (code === '201') {
                    but.style.backgroundColor = "#efff14";
                    but.style.fontSize = "clamp(0.7rem, 1.3vw, 2rem)";

                }
                else
                {
                    console.log("ENSOMMA..."); //mostrare qui a schermo qualcosa che indica che deve loggarsi
                }

            },

            error: function(jqXHR, textStatus, errorThrown) { 

                console.error('Error: ' + textStatus, errorThrown);
            }
        });
    });

});

//pulsante on top
function onTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' }); // Scorri verso l'inizio della pagina con animazione
}

window.onscroll = function() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("top").style.display = "block";
    } else {
        document.getElementById("top").style.display = "none";
    }
};

