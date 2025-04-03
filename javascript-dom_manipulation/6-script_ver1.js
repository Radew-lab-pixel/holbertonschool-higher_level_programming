document.addEventListener('DOMContentLoaded', function() {
    const characterElement = document.getElementById('character');
    const uel =  "https://swapi-api.hbtn.io/api/people/5/?format=json";

    fetch(url)
    // .then(response => response.json())
    //.then(data=> { 
    .then(response=> {
        if (!response.ok){
            throw new Error("Network response was not ok");
    }
        return response.json();    
    })
    .then(data => {
        characterElement.textContent = data.name;
    }) 
    .catch(error => {
        console.error('error fetching data: ', error);
        characterElement.textContent= "Error fetching data";
    });
});