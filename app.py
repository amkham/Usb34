from flask import render_template, Flask, request
from DB import query

app = Flask(__name__)

basket_list = []


@app.route('/')
@app.route('/index')
def hello_world():
    print('Длина корзины: ', len(basket_list))
    return render_template('index.html', basket_count=len(basket_list))


@app.route('/price')
def price():
    result = query.select_all()
    print('Длина корзины: ', len(basket_list))
    return render_template('price_list/price.html',
                           result=result,
                           basket_count=len(basket_list))


@app.route('/new')
def new_product():
    return render_template('new_product/new.html', basket_count=len(basket_list))


@app.route('/support')
def support():
    return render_template('support/support.html')


@app.route('/basket', methods=['POST', 'GET'])
def basket():
    req = request.get_json()
    if req is not None:
        basket_list.append(query.select_by_id(req['id']))

    if len(basket_list):
        return render_template('basket/basket.html', basket_count=len(basket_list), basket_list=basket_list)
    else:
        return render_template('basket/basket_empty.html')


if __name__ == '__main__':
    app.run()
