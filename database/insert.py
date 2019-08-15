#!/usr/bin/python
# -*- coding: UTF-8 -*-


import database.connect_db

def insert(token_value, project_value, channel_value):
    sql = """INSERT INTO token_info(token,
             project, channel)
             VALUES ("%s","%s", "%s")""" % (token_value, project_value, channel_value)
    database.connect_db.client(sql)

