# coding: utf-8
import urllib2
import ssl
import json
import time

# 取消 https 证书验证
ssl._create_default_https_context = ssl._create_unverified_context


def get_resp():
    # 设置网页请求地址
    res = urllib2.Request('https://kyfw.12306.cn/otn/lcxxcx/query'
                          '?purpose_codes=ADULT&queryDate=2016-12-31&from_station=SHH&to_station=BJP')
    # 打开网页
    resp = urllib2.urlopen(res)
    if resp:
        print ('请求成功')
    # 读取网页内容
    return resp.read()


def get_data(resp_info):
    # 定位所需网页信息
    info_start = resp_info.find('"datas":')
    info_end = resp_info.find('"flag":') - 1
    info = resp_info[info_start:info_end]
    # 将字典形式的字符串转化为字典
    info_json = json.loads('{'+info+'}')
    return info_json


def show(info, numb):
    # 遍历每车次信息
    for train in info['datas']:
        # 判断并获取需要查询的车次信息
        if train['station_train_code'] == numb:
            print '商务座：', train['swz_num']
            print '特等座', train['tz_num']
            print '一等座', train['zy_num']
            print '二等座', train['ze_num']
            print '高级软卧', train['gr_num']
            print '软卧', train['rw_num']
            print '硬卧', train['yw_num']
            print '软座', train['rz_num']
            print '硬座', train['yz_num']
            print '无座', train['wz_num']
            print '其它', train['qt_num']


train_numb = raw_input('请输入查询车次（大写）：')
delay_time = input('请输入循环间隔时间（秒）：')
# 循环查询
while True:
    html_info = get_resp()
    info_data = get_data(html_info)
    show(info_data, train_numb)
    print('------------------------------')
    # 延时设定
    time.sleep(delay_time)
