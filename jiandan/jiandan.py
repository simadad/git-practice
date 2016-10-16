# -*- coding: utf-8 -*-
import requests
import re


def resp(address):
    uag = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    header = {'User-Agent': uag}
    return requests.get(address, headers=header)


def get_pic(page):
    address = 'http://jandan.net/ooxx/page-%d' % page
    info = resp(address).text
    pre_pic_href = re.findall(r'img src="h\S*\.jpg', info)
    pic_href = [j[9:] for j in pre_pic_href]
    return pic_href


def save_pic(address):
    name = address.split('/')[-1]
    print (u'正在下载 %s' % name)
    pic = resp(address).content
    print (u'%s 下载完成' % name)
    with open('pics\ %s' % name, 'wb') as f:
        f.write(pic)
        print (u'%s 已保存\n' % name)

for pages in range(2000, 2001):
    pics_href = get_pic(pages)
    for i in pics_href:
        try:
            save_pic(i)
        except requests.exceptions.ConnectionError:
            continue
