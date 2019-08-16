#!/usr/bin/python
# -*- coding: UTF-8 -*-


import database.connect_db

def insert(token_value):
    sql = """SELECT token FROM token_info WHERE token LIKE '%s'""" % (token_value)

    value = database.connect_db.client(sql)
    return value