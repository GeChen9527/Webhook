#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import request
import json
import database.select
def test():
    Postdata = request.get_json() # 获取请求参数
    print(Postdata)

    token = request.args["token"]
    value = database.select.insert(token)
    print(value)

    return value
