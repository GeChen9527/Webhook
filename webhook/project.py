#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import request
import json, channel
import database.select
def test():
    Postdata = request.get_json() # 获取请求参数

    post_token = request.args["token"]
    db = database.select
    #token = db.select_sql("token", post_token)
    #channel = db.select_sql("channel", post_token)
    project = db.select_sql("project", post_token)        //connectdb.py中返回数据后格式格式化
    print(project)
    #if post_token == token:
    #    print(project)
    #else:
     #   return "{\"error\":\"token校验失败\"}"
    return "123"

