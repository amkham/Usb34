import mysql
from mysql.connector import Error
from DB import config


def __connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(**config.settings)
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn

    except Error as e:
        print(e)


def select_all():
    try:
        con = __connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM product_table")
        print('запрос к БД')
        rows = cursor.fetchall()
        result = []

        for row in rows:
            product = {'id': row[0],
                       'name': row[1],
                       'description': row[2],
                       'price': row[3],
                       'img': row[4]}

            result.append(product)

        return result

    except Error as e:
        print(e)


def select_by_id(value):
    try:
        con = __connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM product_table WHERE id = '{}'".format(value))

        rows = cursor.fetchall()
        product = {}
        for row in rows:
            product = {'id': row[0],
                       'name': row[1],
                       'description': row[2],
                       'price': row[3],
                       'img': row[4]}

        return product

    except Error as e:
        print(e)
