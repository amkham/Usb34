let basket_count = 0;
async function post_basketItem(id) {

    let item = {'id': id};
    await fetch('/basket', {
        method: 'POST', // или 'PUT'
        body: JSON.stringify(item), // данные могут быть 'строкой' или {объектом}!
        headers: {
            'Content-Type': 'application/json'
        }
    });

}

function set_item_in_basket() {
    let elem = document.getElementById('basket-count');
    document.getElementById('basket-circle').style.display = 'flex';
    elem.style.display = 'flex';
    basket_count++;
    elem.innerHTML = basket_count;
}

function basket_count_set(count)
{
    basket_count = count;
    if (basket_count >0)
    {
        let elem = document.getElementById('basket-count');
        document.getElementById('basket-circle').style.display = 'flex';
        elem.style.display = 'flex';
        elem.innerHTML = basket_count;
    }
}



