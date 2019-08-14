# encoding: utf-8
import json
import hash
import db
from flask import request


def url():
    url="www.baidu.com"
    Post_value = request.get_json() # 获取请求参数
    Post_type = Post_value["Type"]
    Post_project = Post_value["Project"]
    Post_chanel_num = len(Post_value["Channel"])
    ListNum = 0
    Post_chanel = str('')
    for i in range(Post_chanel_num):
        test = str(Post_value["Channel"][ListNum])
        ListNum = ListNum + 1
        Post_chanel = Post_chanel+test
    if Post_type == "Create":
        token_value = hash.hash()
        db.mysql(token_value, Post_project, Post_chanel)
    else:
        return "参数错误"
    return_url = url+"/token?"+token_value
    return return_url
