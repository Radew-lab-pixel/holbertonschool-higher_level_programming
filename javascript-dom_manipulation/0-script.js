function setHeaderColor() {
    // const urlParams = new URLSearchParams(window.location.search);
    // const source = urlParams.get('source');
    // const header = document.getElementById('pageHeader');
    const header = document.querySelector('header');  // using querySelctor
    
    header.style.color = '#FF0000';  // For invalid/unknown sources
    }

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', setHeaderColor);