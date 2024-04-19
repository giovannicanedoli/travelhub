function showHeart(cuore) {
    var heart = document.getElementById(cuore);
    
    heart.style.visibility = "visible";
    
    setTimeout(function() {
        heart.style.visibility = "hidden";
    }, 300); // This is a delay of 1000000 milliseconds, or approximately 16.67 minutes.
}
