from flask import render_template, Flask, request
from DB import query
import json
import os

app = Flask(__name__)

basket_list = []


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')


@app.route('/price', methods=['POST', 'GET'])
def price():
    result = query.select_all()
    req = request.get_json()
    item = json.loads(json.dumps(req))
    if item is not None:
        basket_list.append(item['id'])
        print(basket_list)
    return render_template('price_list/price.html', result=result, basket_list=basket_list)


@app.route('/new')
def new_product():
    return render_template('new_product/new.html')


if __name__ == '__main__':
    app.run()
