# coding: utf-8
import urllib2
import re

res = urllib2.Request('http://www.sjtu.edu.cn/')
resp = urllib2.urlopen(res)
web_code = resp.read()
href_list = re.findall(r'(?<=href=")http\S+(?=")', web_code)
print href_list
