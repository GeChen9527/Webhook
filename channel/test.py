#coding:utf-8
import json
import urllib.request
url = 123   #url为机器人的webhook

text = """## 【Grafana告警】%s\n
9度，西北风1级,空气良89\n
![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n
###### 10点20分发布 [天气](http://www.thinkpage.cn/)\n
@13399550668""" % (url)
print(text)
#1、构建url
url = "https://oapi.dingtalk.com/robot/send?access_token=9c5832afffb3acc1c192.168.10.181:3000/webhook?token=9806a96b494af3c5009199a74c1b772666c56568522c44ddfd60f68265042293eae4b39090b0b38ad2f9fe3"   #url为机器人的webhook

#2、构建一下请求头部
header = {
    "Content-Type": "application/json",
    "Charset": "UTF-8"
}
#3、构建请求数据
data = {
     "msgtype": "markdown",
     "markdown": {
         "title":"Grafana告警",
         "text": text
     },
     "at": {
        "atMobiles": [
            "13399550668"
        ],
        "isAtAll": "false"
    }
 }

#4、对请求的数据进行json封装
sendData = json.dumps(data)#将字典类型数据转化为json格式
sendData = sendData.encode("utf-8") # python3的Request要求data为byte类型

#5、发送请求
request = urllib.request.Request(url=url, data=sendData, headers=header)

#6、将请求发回的数据构建成为文件格式

opener = urllib.request.urlopen(request)
#7、打印返回的结果
print(opener.read())
