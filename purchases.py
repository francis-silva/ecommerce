# -*- coding: utf-8 -*-
"""
Versão atual     : 0.0.1
Nome             : purchases.py
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
from datetime import datetime, timedelta
from utils import Conn, DateTimeEncoder

sql_script = sql_script = {
    'post':
        '''INSERT INTO public."TB_PEDIDOS"
        ("FK_CLIE_PEDI", "PEDI_DT_ENTREGA") VALUES (%s, %s);''',
    'delete':
        '''DELETE FROM public."TB_PEDIDOS" WHERE "PK_PEDI" = %d;''',
    'get':
        '''SELECT * FROM public."TB_PEDIDOS" WHERE "PK_PEDI" = %s;''',
    'put':
        '''UPDATE public."TB_PEDIDOS"
        SET "PEDI_DT_ENTREGA" = %s;'''
}


class Purchases(Resource):

    def __init__(self):
        self.db_connect = Conn.conn()
        self.cur = self.db_connect.cursor()

    def post(self):
        identifier = request.form.get('identifier')
        delivery_dt = datetime.now() + timedelta(days=7)

        data = (int(identifier), delivery_dt)

        self.cur.execute((sql_script['post']).replace('\n', ' '), data)
        self.db_connect.commit()

        self.cur.execute(
            '''SELECT * FROM public."TB_PEDIDOS"
            ORDER BY "PK_PEDI" DESC LIMIT 1''')

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
