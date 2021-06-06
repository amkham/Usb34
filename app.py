from flask import render_template, Flask
from DB import query
import os

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')


@app.route('/price')
def price():
    result = query.select_all()
    print(result)
    return render_template('price_list/price.html', result=result)


@app.route('/new')
def new_product():
    return render_template('new_product/new.html')


@app.route('/add', methods=['GET', 'POST'])
def add_in_basket():
    print('work')


if __name__ == '__main__':
    app.run()
