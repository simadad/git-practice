# -*- coding: utf-8 -*-
import urllib2
import json


def weather_query(citys):              # 创建查询天气的函数，参数为要查询的城市
    # 从百度APIStore获取天气信息
    url = 'http://apis.baidu.com/apistore/weatherservice/cityname?cityname=%s' % citys
    # 发送天气查询请求
    req = urllib2.Request(url)
    # 提交查询秘钥
    req.add_header("apikey", "1b7f52ccc223f79eb67ab1cc25af0ab7")
    # 取回查询页面
    resp = urllib2.urlopen(req)
    # 获取查询信息
    content = resp.read()
    # 转换信息格式 str to dict
    dicts = json.loads(content)
    # 获取天气字典
    info = dicts['retData']
    # 判断城市是否溢出城市列表
    if info:
        # 输出查询结果
        print (
            u'城市： %s\n'         # 转换Unicode编码
            u'日期： %s\n'
            u'天气： %s\n'
            u'发布时间： %s\n'
            u'实时气温： %s\n'
            u'最低气温： %s\n'
            u'最高气温： %s\n'
            u'风向： %s\n'
            u'风力： %s\n'
            % (                      # 格式化字符
                   info['city'],
                   info['date'],
                   info['weather'],
                   info['time'],
                   info['temp'],
                   info['l_tmp'],
                   info['h_tmp'],
                   info['WD'],
                   info['WS']
               ))
    else:
        print ('城市“%s”天气无法查询' % citys)
# 开始
print ("您好，欢迎使用本天气查询系统")
while True:
    city = raw_input("请输入您想查询的城市名称:\n")
    weather_query(city)
    goOn = raw_input('请输入"继续查询"以查询下一个城市的天气状况，或者退出程序:\n')
    if goOn == '继续查询':
        continue
    else:
        break
