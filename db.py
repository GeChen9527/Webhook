#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

def mysql(token_value, project_value, channel_value):
   db = pymysql.connect("xxx", "xxx", "xxx", "xxx", charset='utf8' )
   cursor = db.cursor()
   test = token_value
   sql = """INSERT INTO token_info(token,
            project, channel)
            VALUES ("%s","%s", "%s")""" % (token_value, project_value, channel_value)

   try:
      cursor.execute(sql)
      db.commit()
   except:
      db.rollback()


   db.close()

