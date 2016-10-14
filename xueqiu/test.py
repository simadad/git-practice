# -*- coding: utf-8 -*-
import urllib2
import json


def combo_name_segment_weight(url):
    # url = 'https://xueqiu.com/P/ZH254351'

    send_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'xueqiu.com',
        'Cookie': r's=8c120yerwd; xq_a_token=5847f5d7be111b16555dde6dd7bd9008fa25cb2a; xqat=5847f5d7be111b16555dde6dd7bd9008fa25cb2a; xq_r_token=d3c6423c44402e4675d9da9a2df2049ace32ab06; xq_is_login=1; u=1258338326; xq_token_expire=Thu%20Nov%2003%202016%2014%3A55%3A43%20GMT%2B0800%20(CST); bid=b65b218e29af9b35acdd1489434718f3_iu29zzh4; Hm_lvt_1db88642e346389874251b5a1eded6e3=1475996063; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1475996161',
    }

    req = urllib2.Request(url, headers=send_headers)
    resp = urllib2.urlopen(req)
    content1 = resp.read()

    # 这里是找到SNB.cubeInfo最开始的位置
    start = content1.find('SNB.cubeInfo = ') + len('SNB.cubeInfo = ')
    end = content1.find('SNB.cubePieData')
    data1 = content1[start:end - 2]
    data = json.loads(data1)

    holdings = data.get('view_rebalancing').get('holdings')
    # 　print holdings

    for i in holdings:
        stock_name = i.get('stock_name')
        segment = i.get('segment_name')
        weight = i.get('weight')
        print '股票名称：', stock_name, '股票类别：', segment, '权重：', weight


combo_name_segment_weight('https://xueqiu.com/p/ZH805323')
