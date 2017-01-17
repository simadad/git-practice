# coding: utf-8
import urllib
import urllib2
import json
import bs4
import csv
import codecs
import cStringIO
from time import sleep


class UnicodeWriter:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        _data = self.queue.getvalue()
        _data = _data.decode("utf-8")
        # ... and reencode it into the target encoding
        _data = self.encoder.encode(_data)
        # write to the target stream
        self.stream.write(_data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


def get_web(post_info, _web_url, _headers):
    data_post = urllib.urlencode(post_info)
    req = urllib2.Request(_web_url, headers=_headers, data=data_post)
    resp = urllib2.urlopen(req)
    content = resp.read()
    content_json = json.loads(content)
    return content_json['msg'][1]


def get_data_list(_web_data, _limit):
    soup = bs4.BeautifulSoup(_web_data, 'lxml')
    user_info = soup.find_all(class_="zm-profile-card zm-profile-section-item zg-clear no-hovercard")
    # ①获取每个用户的全部信息
    info_all = []
    for i in user_info:
        # 遍历每个用户的信息
        info = []
        info_all.append(info)
        try:
            print '正在抓取%s' % i.a['title'],
            info.append(i.a['title'])
            # ②获取昵称
            info.append(i.button['data-id'])
            # ⑥获取关注时需要的id
            is_hot = 'False'
            for j in i.find_all(class_="zg-link-gray-normal"):
                data = j.string
                info.append(data)
                # ③获取用户关注、提问、回答、赞同四项信息
                hot_numb = int(data[:data.index(' ')])
                if hot_numb > _limit:
                    is_hot = 'True'
            info.append(is_hot)
            # ④获取是否为活跃用户的判定结果
            print '%s抓取完毕' % i.a['title']
        except TypeError:
            # 排除无法爬取的情况，防止程序中断
            print 'miss a user data'
    return info_all


def get_csv_data(file_name, data):
    with open(file_name, 'ab') as csfile:
        to_writer = UnicodeWriter(csfile)
        for i in data:
            to_writer.writerow(i)
            print i[0], 'writer finished'
    # return csfile


def follow(file_name, web_url, headers):
    with open(file_name, 'r') as csfile:
        data = csfile.readlines()
        for i in data:
            i = i[:-1]
            # 去除尾部换行符
            if i:
                j = i.split(',')
                if j[-1] == 'True':
                    post_data = {
                        'method': 'follow_member',
                        'params': '{"hash_id": "%s"}' % j[1],
                    }
                    data_post = urllib.urlencode(post_data)
                    urllib2.Request(web_url, headers=headers, data=data_post)
                    # req = urllib2.Request(web_url, headers=headers, data=data_post)
                    # resp = urllib2.urlopen(req)
                    # content = resp.read()
                    # print content
                    sleep(5)


def main_loop(_qid, _cookie, _limit, file_name):
    offset = 0
    web_url = 'https://www.zhihu.com/question/%s/followers' % _qid
    web_url2 = 'https://www.zhihu.com/node/MemberFollowBaseV2'
    headers = {
        'cookie': _cookie,
        'Accept': '* / *',
        'Accept - Encoding': 'deflate',
        'Accept - Language': 'zh - CN, zh;q = 0.8, en;q = 0.6',
        'Connection': 'keep - alive',
        'Content - Length': '17',
        'Content - Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
        'DNT': '1',
        'Host': 'www.zhihu.com',
        'Origin': 'https://www.zhihu.com',
        'Referer': 'https://www.zhihu.com/question/26749114/followers',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Xsrftoken': 'e554b40496f16c1b1f076fa6d15b14f1',
    }
    while True:
        offset += 20
        page = {
            'start': '0',
            'offset': offset,
        }
        print offset
        web_data = get_web(page, web_url, headers)
        user_data = get_data_list(web_data, _limit)
        get_csv_data(file_name, user_data)
        sleep(5)
    follow(file_name, web_url2, headers)


if __name__ == '__main__':
    data_file = 'zhihu.csv'
    qid = '26749114'
    cookie = '_zap=9adbedc9-9e3a-4fcc-9b30-968b8e8d0522; d_c0="AEBAHGyIwwqPTn314odGFi6Yg49DvvOvWJQ=|1477700682"; _zap=64bcf9a4-c2cf-41de-8b7a-b36eec4db6fb; _xsrf=e554b40496f16c1b1f076fa6d15b14f1; aliyungf_tc=AQAAAHXqy0i3DQQAnrum30rfbzy/sG4T; q_c1=0d17007f2d6648908db9f5ec2ef9f71a|1484301131000|1484301131000; l_cap_id="NGIwY2I3NmQ4OGJjNDcxM2FkOWUzYjhlMjI1NzQ3ZWM=|1484301131|25f14861025b11a34f17ca0a4d1c7cc2b02765cc"; cap_id="NmY3NWI4ZWI0NDUzNDZhOWI1MjYzNWEzYTcxYmExNmI=|1484301131|0c3791e8d7ae865581255163d5877bd264a74162"; r_cap_id="MGYyYTg1ZGIwZGZlNGJhMmJhMzA5YWQ0MWEwOGJiMGI=|1484301167|8af7364a9361de0719870f158ef7312473bcd3b7"; login="NzU3ZjA0MTY2YWJhNGVkNDhlNDE1YmJjOGE5MmQ3YmE=|1484301178|77dd2ec942e4f8996463a5bb4794f17a3afb34c9"; n_c=1; z_c0=Mi4wQUFBQUwwUW1BQUFBUUVBY2JJakRDaGNBQUFCaEFsVk5vVENnV0FBRFhpTzJ3aW4yQTF2S1M1V3JSRXgtTmVjS2Jn|1484301226|d9a95afe2c40b9228a9933c40d427592fc16df31; __utma=51854390.2090852359.1482322847.1484284567.1484301166.15; __utmb=51854390.0.10.1484301166; __utmc=51854390; __utmz=51854390.1483974765.10.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.100-1|2=registration_date=20140217=1^3=entry_date=20140217=1'
    limit = 300
    main_loop(qid, cookie, limit, data_file)

# get_name = re.compile(r'(?<=title=").+(?=")')
# data = get_name.findall(web_data)
# data = re.findall(r'(?<=title=").+(?=")', web_data['msg'][1])
# print data
