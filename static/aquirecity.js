var map = L.map('map');

// Aggiungi un layer con piastrelle da OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Usa il servizio di geocodifica Nominatim per trovare le coordinate della città
var cityName = document.getElementById("map").getAttribute("name");

fetch('https://nominatim.openstreetmap.org/search?q=' + cityName + '&format=json')
  .then(response => response.json())
  .then(data => {
    if (data.length > 0) {
      var lat = data[0].lat;
      var lon = data[0].lon;

      // Aggiungi un marker per la città
      L.marker([lat, lon]).addTo(map).bindPopup(cityName);
      
      // Imposta uno zoom più distante
      map.setView([lat, lon], 5); // Imposta un livello di zoom di 2 per una visuale più ampia
    } else {
      console.error("Nessuna città trovata");
    }
  })
  .catch(error => {
    console.error("Errore durante il recupero delle coordinate della città:", error);
  });


var map2 = L.map("map2");
  
  //da fare i controlli

  // Aggiungi un layer con piastrelle da OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map2);

// Usa il servizio di geocodifica Nominatim per trovare le coordinate della città
var cityName2 = document.getElementById("map2").getAttribute("name");
fetch('https://nominatim.openstreetmap.org/search?q=' + cityName2 + '&format=json')
  .then(response => response.json())
  .then(data => {
    if (data.length > 0) {
      var lat = data[0].lat;
      var lon = data[0].lon;
      // Imposta la vista della mappa sulle coordinate della città
      map2.setView([lat, lon], 12); // Imposta un livello di zoom (12) a tua scelta
      // Aggiungi un marker per la città
      L.marker([lat, lon]).addTo(map2)
        .bindPopup(cityName2);
      // Imposta uno zoom più distante
      map2.setView([lat, lon], 5); // Imposta un livello di zoom di 2 per una visuale più ampia
    } else {
      console.error("Nessuna città trovata");
    }
  })
  .catch(error => {
    console.error("Errore durante il recupero delle coordinate della città:", error);
  });

var map3 = L.map("map3");
  
  //da fare i controlli

  // Aggiungi un layer con piastrelle da OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map3);

// Usa il servizio di geocodifica Nominatim per trovare le coordinate della città
var cityName3 = document.getElementById("map3").getAttribute("name");
fetch('https://nominatim.openstreetmap.org/search?q=' + cityName3 + '&format=json')
  .then(response => response.json())
  .then(data => {
    if (data.length > 0) {
      var lat = data[0].lat;
      var lon = data[0].lon;
      // Imposta la vista della mappa sulle coordinate della città
      map3.setView([lat, lon], 12); // Imposta un livello di zoom (12) a tua scelta
      // Aggiungi un marker per la città
      L.marker([lat, lon]).addTo(map3)
        .bindPopup(cityName3);
      // Imposta uno zoom più distante
      map3.setView([lat, lon], 5); // Imposta un livello di zoom di 2 per una visuale più ampia
    } else {
      console.error("Nessuna città trovata");
    }
  })
  .catch(error => {
    console.error("Errore durante il recupero delle coordinate della città:", error);
  });