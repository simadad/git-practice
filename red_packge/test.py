# -*- coding: utf-8 -*-
import random


def on_aver(amount, quantity):
    # 获取每个红包随机权重
    part = [random.random() for i in range(quantity)]
    # 总权重
    inall = sum(part)
    # 权重均数
    average = amount/inall
    return average, part


def distribute(amount, quantity, average, part):
    # 前 N-1 人按权重分配红包
    accumulation = 0
    for i in range(quantity-1):
        part[i] = round(average*part[i], 2)
        # 红包累加
        accumulation += part[i]
        print ('第 %d 人： %.2f 元' % (i+1, part[i]))
    # 最后一份红包
    print ('第 %d 人： %.2f 元' % (quantity, amount-accumulation))
