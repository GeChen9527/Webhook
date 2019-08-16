#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import json
def client(sql):
   db = pymysql.connect("xxx", "xxx", "xxx", "xxx")
   cursor = db.cursor()
   try:
      cursor.execute(sql)
      db.commit()
      Result_value = cursor.fetchall()
      #Result = json.loads(json.dumps(Result_value))
      #return Result[0][0]
      return Result_value
   except:
      db.rollback()

   db.close()
