document.addEventListener('DOMContentLoaded', function() {
    const addItemButton = document.getElementById('add_item');
    const myList = document.querySelector('ul.my_list');
  
    addItemButton.addEventListener('click', function() {
      const newItem = document.createElement('li');
      newItem.textContent = 'Item';
      myList.appendChild(newItem);
    });
  });