# -*- coding: utf-8 -*-
# import chardet


class Country:
    def __init__(self, name, m_gold=0, m_sliver=0, m_bronze=0):
        self.name = name
        self.gold = m_gold
        self.sliver = m_sliver
        self.bronze = m_bronze
        # self.medal = m_bronze + m_sliver + m_gold

    def m_add(self, rank):
        if rank == 1:
            self.gold += 1
            print ('恭喜%s取得一枚金牌' % self.name)
        elif rank == 2:
            self.sliver += 1
            print ('恭喜%s取得一枚银牌' % self.name)
        elif rank == 3:
            self.bronze += 1
            print ('恭喜%s取得一枚铜牌' % self.name)
        else:
            print ('没有获得奖牌')

    def m_all(self):
        return self.gold+self.sliver+self.bronze

    def m_show(self):
        print (
            '%s 奖牌总数为：%d; '
            '金牌数为：%d; '
            '银牌数为：%d; '
            '铜牌数为：%d '
            % (
                self.name,
                self.m_all(),
                self.gold,
                self.sliver,
                self.bronze
            ))

'''
def sort(countries, metal):
    if metal in ['G', 'S', 'B', 'T']:
        sorted(countries, key=lambda x: countries[metal])
    else:
        print ('无效输入！')
'''
# 开始
olympic_file = open('olympic.txt')
olympic_content = olympic_file.readlines()
li_country = [i.split() for i in olympic_content]                # .中国？？？？
# 对象集
countries = [(Country(i[0], int(i[2]), int(i[3]), int(i[4]))) for i in li_country]
while True:
    # li_metal = sorted([i.m_all for i in countries], key=lambda x: x[1], reverse=True)
    # li_gold = sorted([i.gold for i in countries], key=lambda x: x[2], reverse=True)
    li_metal = sorted(countries, key=lambda x: x.m_all, reverse=False)
    li_gold = sorted(countries, key=lambda x: x.gold, reverse=True)
    print ('奖牌榜：')
    for i in li_metal:
        # new_country[i[0]] = (Country(i[0], int(i[2]), int(i[3]), int(i[4])))
        # new_country[i[0]].m_show()
        i.m_show()
    print ('金牌榜：')
    for i in li_gold:
        # new_country = Country(i[0], int(i[2]), int(i[3]), int(i[4]))
        # new_country.m_show()
        i.m_show()

    end = raw_input('输入“继续”添加奖牌，否则退出程序').decode('utf-8')
    if end == u'继续':
        pass
    else:
        break
    # 新增奖牌

    country_name = raw_input('新增奖牌\n国家：')
    new_rank = int(raw_input('名次'))
    country = Country(country_name)
    country.m_add(new_rank)
    country.m_show()
    li_country.append([country.name, country.gold, country.sliver, country.bronze])


'''
def new_metal():
    country_name = raw_input('新增奖牌\n国家：').decode('uft-8')
    new_rank = int(raw_input('名次'))
    if country_name in [j.name for j in countries]:
'''




