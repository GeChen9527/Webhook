#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
#def mysql():
db = pymysql.connect("xxx", "xxx", "xxx", "xxx", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 插入语句
sql = """INSERT INTO token_info(token,
         project, channel)
         VALUES ('0a584ea421637e6c2b5a6d762a1d26ed1a54d4a6', '1', '123')"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()