#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

def client(sql):
   db = pymysql.connect("xxx", "xxx", "xxx", "xxx")
   cursor = db.cursor()
   try:
      cursor.execute(sql)
      db.commit()
   except:
      db.rollback()

   db.close()

