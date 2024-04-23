const newspaperSpinning = [
    { transform: "rotate(0) scale(1) opacity(0)"  },
    { transform: "rotate(360deg) scale(1)" },
    { transform: "rotate(360deg) opacity(1)" },
    { transform: 'translateY(0px)' },
    { transform: 'translateY(-300px)' },
  ];
const newspaperTiming = {
    duration: 2000,
    iterations: 1,
  };



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
                    heart.animate(newspaperSpinning, newspaperTiming);
                    setTimeout(function(){
                        heart.style.visibility = "hidden";
                    },2000);

                    
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
                    //ANIMAZIONE
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
                    heart.animate(newspaperSpinning, newspaperTiming);
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
