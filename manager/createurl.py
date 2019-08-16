#!/usr/bin/python
# -*- coding: UTF-8 -*-
from webhook import hash
from database import insert
from flask import request
import json

def url():
    url="http://webhook.zvcms.cn"
    Post_value = request.get_json()  # 获取请求参数
    print(Post_value)
    Post_type = Post_value["Type"]
    Post_project = Post_value["Project"]
    Post_chanel_json = Post_value["Channel"]
    Post_chanel = json.dumps(Post_chanel_json)

    if Post_type == "Create":
        token_value = hash.hash()
        insert.insert(token_value, Post_project, Post_chanel)

    else:
        return "参数错误"
    return_url = url+"/webhook?token="+token_value
    return_url_json = {"webhook_url":return_url}
    return return_url_json
