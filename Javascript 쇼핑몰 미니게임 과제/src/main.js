function loadItems() {
    return fetch('./data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

// Updata the list with the givin items
function displayItems(items) {
    const container = document.querySelector('.items');
    // const html = items = items.map(item => createHTMLString(item));
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

// Create HTML list item form the given item
function createHTMLString(item){
    return `
    <li class="item">
      <img src="${item.image}" alt="${item.type}" class="item__thumbnail" />
      <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

function onButtonClick(event, items) {
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;

    if(key == null || value == null){
        return;
    }

    const filtered = items.filter(item => item[key] === value);
    displayItems(filtered);
}

// // invisible로 해결하는 힌트
// function onButtonClick(event, items) {
//     const target = event.target;
//     const key = target.dataset.key;
//     const value = target.dataset.value;
//     if(key == null || value == null){
//         return;
//     }
//     updateItems(items, key, value);
// }

// function updateItems(items, key, value) {
//     items.forEach(item => {
//         if(item.dataset[key] === value){
//             item.classList.remove('invisible');
//         } else {
//             item.classList.add('invisible');
//         }
//     });
// }



function setEventListeners(items) {
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click', () => displayItems(items));
    buttons.addEventListener('click', event => onButtonClick(event, items));
}

//main
loadItems()
.then(items => {
    console.log(items)
    displayItems(items);
    setEventListeners(items)
})
.catch(console.log)