# -*- coding: utf-8 -*-
"""
Versão atual     : 0.0.1
Nome             : utils.py
Criado em        : 21/07/2020
Descrição        :
Nota             :
Justificativa    :
@criador         : francis.silva

Modificações
Autor            Data        Versão

"""

from psycopg2 import connect
from json import JSONEncoder
import datetime as dt

class Conn(object):
    def conn():
        conn = connect(user='postgres',
                       password='teste123',
                       host='ecommerce.cykkqml9ald8.us-east-2.rds.amazonaws.com',
                       port='5432',
                       database='ecommerce')

        return conn


class DateTimeEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (dt.date, dt.datetime)):
                return obj.isoformat()
