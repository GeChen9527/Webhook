#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import urllib.request

def Dingtalk_alerting(value,metric,image,name,url,status):
    text = """### 【Grafana告警】%s\n告警机器：%s\n###### 当前值：%s [图表](%s)\n###### 告警状态：%s [详细信息](%s)\n@13399550668""" % (name, metric, value, image, status, url)
    print(name)  # url为机器人的webhook
    url = "https://oapi.dingtalk.com/robot/send?access_token=9c5832afffb3acc1c522c44ddfd60f68265042293eae4b39090b0b38ad2f9fe3"

    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }

    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "Grafana告警",
            "text": text
        },
        "at": {
            "atMobiles": [
                "13399550668"
            ],
            "isAtAll": "false"
        }
    }

    sendData = json.dumps(data)  # 将字典类型数据转化为json格式
    sendData = sendData.encode("utf-8")  # python3的Request要求data为byte类型

    request = urllib.request.Request(url=url, data=sendData, headers=header)

    opener = urllib.request.urlopen(request)

    return opener.read()

def Dingtalk_ok(image,name,url,status):
    text = """### 【Grafana告警】%s\n##### 告警状态：(%s) \n###### 告警图表：[图表](%s)\n###### 告警详细信息：[详细信息](%s)\n @13399550668""" % (name, status, image, url)
    print(name)  # url为机器人的webhook
    url = "https://oapi.dingtalk.com/robot/send?access_token=9c5832afffb3acc1c522c44ddfd60f68265042293eae4bx"

    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }

    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "Grafana告警",
            "text": text
        },
        "at": {
            "atMobiles": [
                "13399550668"
            ],
            "isAtAll": "false"
        }
    }

    sendData = json.dumps(data)  # 将字典类型数据转化为json格式
    sendData = sendData.encode("utf-8")  # python3的Request要求data为byte类型

    request = urllib.request.Request(url=url, data=sendData, headers=header)

    opener = urllib.request.urlopen(request)

    return opener.read()
