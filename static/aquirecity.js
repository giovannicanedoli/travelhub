var map = L.map('map');

var cityName = document.getElementById("map").getAttribute("name");
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

fetch('https://nominatim.openstreetmap.org/search?q=' + cityName + '&format=json')
  .then(response => response.json())
  .then(data => {
    if (data.length > 0) {
      var lat = data[0].lat;
      var lon = data[0].lon;
      L.marker([lat, lon]).addTo(map).bindPopup(cityName);
      map.setView([lat, lon], 5); 
    } else {
      console.error("No city found with the provided data!");
    }
  })
  .catch(error => {
    console.error("Error in fetching data!", error);
  });


var map2 = L.map("map2");
var cityName2 = document.getElementById("map2").getAttribute("name");
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map2);

fetch('https://nominatim.openstreetmap.org/search?q=' + cityName2 + '&format=json')
  .then(response => response.json())
  .then(data => {
    if (data.length > 0) {
      var lat = data[0].lat;
      var lon = data[0].lon;
      map2.setView([lat, lon], 12); 
      L.marker([lat, lon]).addTo(map2)
        .bindPopup(cityName2);
      map2.setView([lat, lon], 5);
    } else {
      console.error("No city found with the provided data!");
    }
  })
  .catch(error => {
    console.error("Error in fetching data!", error);
  });

var map3 = L.map("map3");
var cityName3 = document.getElementById("map3").getAttribute("name");
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map3);

fetch('https://nominatim.openstreetmap.org/search?q=' + cityName3 + '&format=json')
  .then(response => response.json())
  .then(data => {
    if (data.length > 0) {
      var lat = data[0].lat;
      var lon = data[0].lon;
      map3.setView([lat, lon], 12);
      
      L.marker([lat, lon]).addTo(map3)
        .bindPopup(cityName3);
      
      map3.setView([lat, lon], 5);
    } else {
      console.error("No city found with the provided data!");
    }
  })
  .catch(error => {
    console.error("Error in fetching data!", error);
  });