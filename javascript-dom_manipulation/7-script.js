document.addEventListener('DOMContentLoaded', function(){
    const listElement = document.getElementById("list_movies");
    const url = "https://swapi-api.hbtn.io/api/films/?format=json";

    fetch(url)
    .then(response => response.json())
    .then(data => {
        // listElement.childNodes = data.
        const films = data.results;
        // films,this.scripts.forEach(film => {
            films.forEach(film => {
            const new_li = document.createElement('li'); 
            new_li.textContent = film.title;
            listElement.append(new_li);
        });

    });
});