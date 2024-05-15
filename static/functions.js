var colore = '#7a7a7a';

document.getElementById('cinque').addEventListener('mouseover', function() {
    document.getElementById('cinque').style.backgroundColor = 'yellow';
    document.getElementById('quattro').style.backgroundColor = 'yellow';
    document.getElementById('tre').style.backgroundColor = 'yellow';
    document.getElementById('due').style.backgroundColor = 'yellow';
    document.getElementById('uno').style.backgroundColor = 'yellow';
    document.getElementById('texthere').innerText = "AWESOME!";

    document.getElementById('sendmedata').value = '5';
    
});

document.getElementById('quattro').addEventListener('mouseover', function() {   
    
    var selector4 = document.getElementById('quattro');
    var selector5 = document.getElementById('cinque');

    //se il colore è già giallo significa che è stato premuta una stella successiva
    if(selector4.style.backgroundColor == 'yellow'){
        //voglio passare da 5 stelle a 4 stelle
        selector5.style.backgroundColor = colore;
        selector4.style.backgroundColor = 'yellow';
        document.getElementById('tre').style.backgroundColor = 'yellow';
        document.getElementById('due').style.backgroundColor = 'yellow';
        document.getElementById('uno').style.backgroundColor = 'yellow';

    }else{
        selector4.style.backgroundColor = 'yellow';
        document.getElementById('tre').style.backgroundColor = 'yellow';
        document.getElementById('due').style.backgroundColor = 'yellow';
        document.getElementById('uno').style.backgroundColor = 'yellow';

    }
    document.getElementById('texthere').innerText = "Really good";

    document.getElementById('sendmedata').value = '4';


});

document.getElementById('tre').addEventListener('mouseover', function() {

    var selector3 = document.getElementById('tre');
    var selector4 = document.getElementById('quattro');
    var selector5 = document.getElementById('cinque');


    if(selector3.style.backgroundColor == 'yellow'){
        //voglio passare da 5 stelle a 4 stelle
        selector5.style.backgroundColor = colore;
        selector4.style.backgroundColor = colore;
        selector3.style.backgroundColor = 'yellow';
        document.getElementById('due').style.backgroundColor = 'yellow';
        document.getElementById('uno').style.backgroundColor = 'yellow';
    }else{
        
        document.getElementById('tre').style.backgroundColor = 'yellow';
        document.getElementById('due').style.backgroundColor = 'yellow';
        document.getElementById('uno').style.backgroundColor = 'yellow';

    }
    document.getElementById('texthere').innerText = "Overall it's good.";

    document.getElementById('sendmedata').value = '3';



});

document.getElementById('due').addEventListener('mouseover', function() {

    var selector2 = document.getElementById('due');
    var selector3 = document.getElementById('tre');
    var selector4 = document.getElementById('quattro');
    var selector5 = document.getElementById('cinque');


    if(selector2.style.backgroundColor == 'yellow'){
        //voglio passare da 5 stelle a 4 stelle
        selector5.style.backgroundColor = colore;
        selector4.style.backgroundColor = colore;
        selector3.style.backgroundColor =  colore;
        selector2.style.backgroundColor = 'yellow';
        document.getElementById('uno').style.backgroundColor = 'yellow';
    }else{
        document.getElementById('due').style.backgroundColor = 'yellow';
        document.getElementById('uno').style.backgroundColor = 'yellow';

    }
    document.getElementById('texthere').innerText = "Coul'd be better";

    document.getElementById('sendmedata').value = '2';



});

document.getElementById('uno').addEventListener('mouseover', function() {
    document.getElementById('cinque').style.backgroundColor = colore;
    document.getElementById('quattro').style.backgroundColor = colore;
    document.getElementById('tre').style.backgroundColor = colore;
    document.getElementById('due').style.backgroundColor = colore;
    document.getElementById('uno').style.backgroundColor = 'yellow';
    document.getElementById('texthere').innerText = "Meh";

    document.getElementById('sendmedata').value = '1';

});

