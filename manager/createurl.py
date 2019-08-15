# encoding: utf-8
from webhook import hash
from database import insert
from flask import request
import json

def url():
    url="www.baidu.com"
    Post_value = request.get_json() # 获取请求参数
    Post_type = Post_value["Type"]
    Post_project = Post_value["Project"]
    Post_chanel_json = Post_value["Channel"]
    Post_chanel = json.dumps(Post_chanel_json)

    if Post_type == "Create":
        token_value = hash.hash()
        insert.insert(token_value, Post_project, Post_chanel)

    else:
        return "参数错误"
    return_url = url+"/token?"+token_value
    return_url_json = {"webhook_url":return_url}
    return return_url_json
