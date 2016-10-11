# -*- coding: utf-8 -*-
import urllib2
from urllib import urlencode
url = 'http://apis.baidu.com/turing/turing/turing'
req = urllib2.Request(url)
req.add_header('apikey', '1b7f52ccc223f79eb67ab1cc25af0ab7')
urlParam = {
    'key': '879a6cb3afb84dbf4fc84a1df2ab7319',
    'info': '你好',
    'userid': '张三'
}
urlParam = urlencode(urlParam)
resp = urllib2.urlopen(req, urlParam)
content = resp.read()
print (content)



