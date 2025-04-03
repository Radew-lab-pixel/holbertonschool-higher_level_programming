document.addEventListener("DOMContentLoaded", function() {
    const redHeaderBtn = document.getElementById("red_header");
    
    redHeaderBtn.addEventListener("click", function() {
      const header = document.querySelector("header");
      header.classList.add("red");
    });
  });