#!/usr/bin/python
# -*- coding: UTF-8 -*-

import database.connect_db


def select_sql(search_filed, token_value):
    sql = """SELECT %s FROM token_info WHERE token LIKE '%s'""" % (search_filed, token_value)
    value = database.connect_db.client(sql)
    return value
