# -*- coding: utf-8 -*-
"""
Versão atual     : 0.0.1
Nome             : products.py
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


sql_script = sql_script = {
    'post':
        '''INSERT INTO public."TB_PRODUTOS"
        ("PROD_TX_DESCRICAO", "PROD_VL_VALOR") VALUES (%s, %s);''',
    'delete':
        '''DELETE FROM public."TB_PRODUTOS" WHERE "PK_PROD" = %d;''',
    'get':
        '''SELECT * FROM public."TB_PRODUTOS" WHERE "PK_PROD" = %s;''',
    'put':
        '''UPDATE public."TB_PRODUTOS"
        SET "PROD_TX_DESCRICAO" = %s, "PROD_VL_VALOR" = %s;'''
}


class Products(Resource):

    def __init__(self):
        self.db_connect = Conn.conn()
        self.cur = self.db_connect.cursor()

    def post(self):
        description = request.form.get('description')
        value = request.form.get('value')

        data = (description, value)

        self.cur.execute((sql_script['post']).replace('\n', ' '), data)
        self.db_connect.commit()

        self.cur.execute(
            '''SELECT * FROM public."TB_PRODUTOS"
            ORDER BY "PK_PROD" DESC LIMIT 1''')

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
