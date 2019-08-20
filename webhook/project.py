#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import request
import database.select, json, project_json_alarm.grafana
def test():
    Postdata = request.get_json()         # 获取请求参数
    print(Postdata)

    post_token = request.args["token"]     # 获取url中token参数
    db = database.select
    alarm_json = project_json_alarm.grafana

    token = db.select_sql("token", post_token)
    channel = db.select_sql("channel", post_token)    # 获取数据库chanel通道
    project = db.select_sql("project", post_token)        # 获取数据库project来源

    if post_token == token:
        if project == 1:
            alarm = alarm_json.grafana_alarm(Postdata, channel)
            return alarm
    else:
        return "{\"error\":\"token校验失败\"}"
    return "123"

