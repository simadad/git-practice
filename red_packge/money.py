# -*- coding: utf-8 -*-
import random


def numb(tip, if_int):     # ####### 确保用户输入数字甚至整数 ########
    while True:
        try:
            num = input(tip)
            if if_int:
                if num % 1 == 0:
                    pass
                else:
                    continue
            else:
                pass
            return num
        except NameError:
            continue
        except SyntaxError:
            continue
money = numb('请输入红包总金额：', False)
count = numb('请输入红包个数: ', True)
# 初始化
part = []    # 每个红包权重
inall = 0    # 总权重
excpt = 0    # 除最后一个红包外的红包总值
# 获取每红包随机权重
for i in range(count):
    every = random.random()
    part.append(every)
    # 权重累加
    inall += every
# 权重均数
average = money/inall
# 前N-1份红包按权重分配
for i in range(count-1):
    part[i] = round(average*part[i], 2)
    # 红包累加
    excpt += part[i]
    print (part[i])
# 最后一份红包
print (money-excpt)
