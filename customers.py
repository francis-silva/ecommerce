# -*- coding: utf-8 -*-
"""
Versão atual     : 0.0.1
Nome             : customers.py
Criado em        : 21/07/2020
Descrição        : 
Nota             :
Justificativa    :
@criador         : francis.silva

Modificações
Autor            Data        Versão

"""

import json
from flask import request
from flask_restful import Resource
from utils import Conn, DateTimeEncoder


sql_script = {
    'post':
        '''INSERT INTO public."TB_CLIENTES"
        ("PK_CLIE", "CLIE_NM_NOME", "CLIE_TX_ENDERECO",
         "CLIE_TX_CIDADE", "CLIE_CD_UF")
        VALUES (%s, %s, %s, %s, %s);''',
    'delete':
        '''DELETE FROM public."TB_CLIENTES" WHERE "PK_CLIE" = %s;''',
    'get':
        '''SELECT * FROM public."TB_CLIENTES" WHERE "PK_CLIE" = %s;''',
    'put':
        '''UPDATE public."TB_CLIENTES"
        SET "CLIE_TX_ENDERECO" = %s,
        "CLIE_TX_CIDADE" = %s, "CLIE_CD_UF" = %s
        WHERE "PK_CLIENTE" = %s;'''
}


class Customers(Resource):

    def __init__(self):
        self.db_connect = Conn.conn()
        self.cur = self.db_connect.cursor()


    def post(self):
        identifier = request.form.get('identifier')
        name = request.form.get('name')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')

        data = (int(identifier), name, address, city, state)

        self.cur.execute((sql_script['post']).replace('\n', ' '), data)
        self.db_connect.commit()

        self.cur.execute(
            (sql_script['get']).replace('\n', ' ') % int(identifier))

        result = self.cur.fetchall()[0]
        self.db_connect.close()
        return json.dumps(result, indent=4, cls=DateTimeEncoder)


    def delete(self, id):
        self.cur.execute((sql_script['delete']).replace('\n', ' ') % int(id))
        self.db_connect.commit()
        return {'status': 'id: ' + id + ' excluded'}
        self.db_connect.close()

    def get(self, id):
        self.cur.execute((sql_script['get']).replace('\n', ' ') % int(id))
        result = self.cur.fetchall()[0]
        self.db_connect.close()
        return json.dumps(result, indent=4, cls=DateTimeEncoder)
