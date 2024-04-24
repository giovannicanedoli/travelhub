const div1 = document.getElementById("descrizione");

function desc() {
        if (div1.style.display() == "none") {
                div1.style.display = "block";
                console.log("pdpd");
        }
        else {
                div1.style.display = "none";
        }
}
