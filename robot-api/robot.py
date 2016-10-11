# -*- coding: utf-8 -*-
import json
import urllib2
from urllib import urlencode
# 准备提交网址和密码
url = 'http://apis.baidu.com/turing/turing/turing'
req = urllib2.Request(url)
req.add_header('apikey', '1b7f52ccc223f79eb67ab1cc25af0ab7')


def dialogue(msg):       # 发送请求，获取返回值
    info = {
        'key': '879a6cb3afb84dbf4fc84a1df2ab7319',
        'info': msg,
        'userid': 'name'
    }
    resp = urllib2.urlopen(req, urlencode(info))
    return resp.read()


def json_to_str(js, key):        # 解构json 获取AI回话
    information = json.loads(js)
    return information[key]

name = raw_input("你的名字是： ")
while True:                         # 循环对话
    message = raw_input('说点什么吧： ')
    if message == 'QUIT':
        break
    else:
        pass
    dialog = dialogue(message)
    respond = json_to_str(dialog, 'text')
    print ('AI: ' + respond)
    print ('***退出请输入：“QUIT”***')
