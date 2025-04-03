document.addEventListener('DOMContentLoaded', function() {
    const characterElement = document.getElementById('character');
    const url =  "https://swapi-api.hbtn.io/api/people/5/?format=json";

    fetch(url)
    .then(response => response.json())
    .then(data=> {
        characterElement.textContent = data.name;
    });
});