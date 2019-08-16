#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import json
#def client(sql):
db = pymysql.connect("111.231.53.12", "webhookdev", "ZRPfsFfbpWEcZiTi", "webhook")
cursor = db.cursor()
sql = """SELECT token FROM token_info WHERE token LIKE '78eb8a2e15149b74a46672f9c906a9a85733d4cc'"""
try:
   cursor.execute(sql)
   db.commit()
   test = cursor.fetchall()
   print(test)
   test1 = json.dumps(test)
   test2 = json.loads(test1)
   print(test2[0][0])


except:
   db.rollback()

db.close()


