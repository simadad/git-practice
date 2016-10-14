# -*- coding: utf-8 -*-
import urllib2
import json
import chardet


def get_html():
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 's=5w1lrbt9ar; xq_a_token=eede0debf432b63396da4e0ca2e05cfb9506e1cc; '
                  'xq_r_token=9a57bb72fa5dfc3705ad8861a649e6b4d8f4b6e7; __utmt=1; '
                  '__utma=1.257174880.1476426895.1476426895.1476426895.1; __utmb=1.1.10.1476426895; '
                  '__utmc=1; __utmz=1.1476426895.1.1.utmcsr=bbs.crossincode.com|utmccn=(referral)|'
                  'utmcmd=referral|utmcct=/forum.php; Hm_lvt_1db88642e346389874251b5a1eded6e3=1476426895,'
                  '1476427015,1476427033,1476427048; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1476427048',
        'DNT': '1',
        'Host': 'xueqiu.com',
        'Referer': 'https://xueqiu.com/P/ZH010389',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/50.0.2661.102 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    res = urllib2.Request('https://xueqiu.com/P/ZH010389', headers=headers)
    resp = urllib2.urlopen(res)
    if resp:
        print ('请求成功')
    return resp.read()

html = get_html()
pos_start = html.find('SNB.cubeInfo = ') + len('SNB.cubeInfo = ')
pos_end = html.find('SNB.cubePieData')
data = html[pos_start:pos_end-2].decode('utf-8')
# print (type(data))
# print (chardet.detect(data))
dic = json.loads(data)
print ('收益率：%.2f' % dic['total_gain'])
stocks = dic['view_rebalancing']['holdings']
print ('持股id  股票名称 持股比例')
for s in stocks:
    print s['stock_id'], s['stock_name'], s['weight']
