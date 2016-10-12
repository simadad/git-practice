# -*- coding: utf-8 -*-
import random


def numb(tip, if_int):
    # ####### 确保用户输入正数甚至正整数 ########
    while True:
        try:
            num = input(tip)
            if num > 0:
                if if_int:
                    if num % 1 == 0:
                        pass
                    else:
                        continue
                else:
                    pass
            else:
                continue
            return num
        except NameError:
            continue
        except SyntaxError:
            continue


def on_aver(amount, quantity):
    # 获取每个红包随机权重
    part = [random.random() for i in range(quantity)]
    # 总权重
    inall = sum(part)
    # 权重均数
    average = amount/inall
    return average, part


def distribute(amount, quantity, average, part):
    # 分配红包
    accumulation = 0
    for i in range(quantity-1):
        # 前N-1人红包分配
        part[i] = round(average*part[i], 2)
        # 确保当前红包至少为0.01
        if part[i] > 0:
            pass
        else:
            part[i] = 0.01
            # 从下一个红包中削减0.01的份额
            part[i+1] -= 0.01/average
        # 红包累加
        accumulation += part[i]
        # 确保剩下的金额足够
        if money-accumulation < 0.01*(quantity-1-i):
            # 削减当前红包金额
            part[i] -= 0.01*(quantity-1-i)-(money-accumulation)
            accumulation -= 0.01*(quantity-1-i)-(money-accumulation)
        print ('第 %d 人： %.2f 元' % (i + 1, part[i]))
    # 最后一份红包
    print ('第 %d 人： %.2f 元' % (quantity, amount-accumulation))

# 开始
while True:
    money = numb('请输入红包总金额：', False)
    count = numb('请输入红包个数: ', True)
    if count*0.01 <= money:
        pass
    else:
        print ('单个红包不能低于0.01元\n')
        continue
    weight = on_aver(money, count)
    distribute(money, count, weight[0], weight[1])
    # 循环判断
    again = raw_input('输入“继续”再发红包\n').decode('utf-8')
    if again == u'继续':
        continue
    else:
        break
