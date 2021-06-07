let basket_count = 0;
async function script(id) {

    let product = {'id': id}

    let elem = document.getElementById('basket-count');
    document.getElementById('basket-circle').style.display = 'flex';
    elem.style.display = 'flex';
    elem.innerHTML = basket_count + 1;
    basket_count++;


    await fetch('/price', {
            method: 'POST', // или 'PUT'
            body: JSON.stringify(product), // данные могут быть 'строкой' или {объектом}!
            headers: {
                'Content-Type': 'application/json'
            }
        });


}



