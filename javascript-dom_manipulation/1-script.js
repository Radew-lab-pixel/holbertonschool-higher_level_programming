function setHeaderColor(){
    const header = document.querySelector("header");
    header.style.color = "#FF0000";
    }
document.addEventListener("DOMContentLoaded", function() {
    const redHeaderBtn = document.getElementById("red_header");
    redHeaderBtn.addEventListener("click", setHeaderColor);
});