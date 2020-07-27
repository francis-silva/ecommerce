# -*- coding: utf-8 -*-
"""
Versão atual     : 0.0.1
Nome             : server.py
Criado em        : 21/07/2020
Descrição        : Main
Nota             :
Justificativa    :
@criador         : francis.silva

Modificações
Autor            Data        Versão

"""

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from json import dumps
import json
from customers import Customers
from products import Products
from purchases import Purchases
from itenspurchases import ItensPurchases
from psycopg2 import connect

app = Flask(__name__)
api = Api(app)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}))

api.add_resource(Customers, '/customers', endpoint='postCustomers')
api.add_resource(Customers, '/customers/<id>', endpoint='idCustomers')

api.add_resource(Products, '/products', endpoint='postProducts')
api.add_resource(Products, '/products/<id>', endpoint='idProducts')

api.add_resource(Purchases, '/purchases', endpoint='postPurchases')
api.add_resource(Purchases, '/purchases/<id>', endpoint='idPurchases')

api.add_resource(Purchases, '/itenspurchases', endpoint='postItensPurchases')
api.add_resource(Purchases, '/itenspurchases/<id>', endpoint='idItensPurchases')

if __name__ == '__main__':
    app.run(debug=True)
