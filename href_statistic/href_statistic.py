# coding: utf-8
import urllib2
import re

# 设置请求地址
res = urllib2.Request('http://www.sjtu.edu.cn/')
# 打开请求回复
resp = urllib2.urlopen(res)
# 读取返回的源代码
web_code = resp.read()
# 匹配超链接
href_list = re.findall(r'(?<=href=")http\S+(?=")', web_code)
print href_list
