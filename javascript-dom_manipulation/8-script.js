document.addEventListener('DOMContentLoaded', function(){
    const helloElement = document.getElementById('hello');
    const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";

    fetch(url)
    .then (response=>response.json())
    .then (data=> {
        helloElement.textContent=data.hello;
    });

});