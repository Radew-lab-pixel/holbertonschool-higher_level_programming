document.addEventListener('DOMContentLoaded', function()
{
    const updateHeader = document.getElementById('update_header');
    const header = document.querySelector('header');

    updateHeader.addEventListener("click", function(){
        //header.replaceWith
        header.textContent= "New Header!!!";

    })

})