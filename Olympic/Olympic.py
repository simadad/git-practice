# -*- coding: utf-8 -*-
import sqlite3
import re
import my_func
import chardet

tb_content = '''
id          integer     primary key,
county      text        not null,
m_gold      int         not null,
m_sliver    int         not null,
m_bronze    int         not null
'''
Database = my_func.new_database('Olympic.db', 'medals', tb_content)


class Country:
    def __init__(self, c_name, m_gold=0, m_sliver=0, m_bronze=0):
        self.name = c_name.encode('utf-8')
        self.gold = m_gold
        self.sliver = m_sliver
        self.bronze = m_bronze

    def m_add(self, rank):
        if rank == 1:
            self.gold += 1
            my_func.update(Database, 'medals', 'm_gold', self.gold, 'where county = "%s"' % self.name)
            print ('恭喜%s取得一枚金牌' % self.name)
        elif rank == 2:
            self.sliver += 1
            my_func.update(Database, 'medals', 'm_sliver', self.sliver, 'where county = "%s"' % self.name)
            print ('恭喜%s取得一枚银牌' % self.name)
        elif rank == 3:
            self.bronze += 1
            my_func.update(Database, 'medals', 'm_bronze', self.bronze, 'where county = "%s"' % self.name)
            print ('恭喜%s取得一枚铜牌' % self.name)
        else:
            print ('没有获得奖牌')
        self.m_show()
        print

    @property
    def m_all(self):
        return self.gold + self.sliver + self.bronze

    def m_show(self):
        print (
            '%s 奖牌总数为：%d; '
            '金牌数为：%d; '
            '银牌数为：%d; '
            '铜牌数为：%d '
            % (
                self.name,
                self.m_all,
                self.gold,
                self.sliver,
                self.bronze
            ))


def get_counties():
    # 得到已有国家的数据，实例化类
    data = my_func.select(Database, 'medals')
    countries_data = data.fetchall()
    all_countries = [Country(country_data[1], country_data[2], country_data[3], country_data[4])
                     for country_data in countries_data]
    return all_countries


def add_metal():
    # 添加获奖记录
    nation = raw_input('请输入获奖国家：')
    score = my_func.numb('请输入获得名次：')
    new_county = True
    for county in counties:
        if county.name == nation:
            county.m_add(score)
            new_county = False
    if new_county:
        nation = Country(nation.decode('utf-8'))
        new_info = '"%s", %d, %d, %d' % (nation.name, nation.gold, nation.sliver, nation.bronze)
        my_func.insert(Database, 'medals', new_info)
        counties.append(nation)
        nation.m_add(score)


def ranking(keys):
    # 排序
    if keys == 1:
        print ('***奥运金牌榜***')
        new_ranking = sorted(counties, key=lambda x: x.gold, reverse=True)
    else:
        print ('***奥运奖牌榜***')
        new_ranking = sorted(counties, key=lambda x: x.m_all, reverse=True)
    if counties:
        for i in new_ranking:
            i.m_show()
    else:
        print ('暂无国家获奖')
    print


# 开始
counties = get_counties()
while True:
    print ('查询金牌榜请按“1”，查询奖牌榜请按“2”，添加奖牌请按“0”，退出请回车')
    next_action = raw_input('请输入操作码：')
    if next_action == "0":
        add_metal()
    elif next_action == '1':
        ranking(1)
    elif next_action == '2':
        ranking(2)
    else:
        break
