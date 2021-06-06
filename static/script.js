let basket_count = 0;
function script() {


    let elem = document.getElementById('basket-count');
    document.getElementById('basket-circle').style.display = 'flex';
    elem.style.display = 'flex';
    elem.innerHTML = basket_count + 1;
    basket_count++;

}



