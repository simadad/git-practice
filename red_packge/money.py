# -*- coding: utf-8 -*-
import random


<<<<<<< HEAD
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
=======
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
>>>>>>> 6cef7fb7a366545c48dd4b2a3872b6a7bd0695a3
            return num
        except NameError:
            continue
        except SyntaxError:
            continue
<<<<<<< HEAD


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

# 开始
while True:
    money = numb('请输入红包总金额：', False)
    count = numb('请输入红包个数: ', True)
    weight = on_aver(money, count)
    distribute(money, count, weight[0], weight[1])
    # 循环判断
    again = raw_input('输入“继续”再发红包\n').decode('utf-8')
    if again == u'继续':
        continue
    else:
        break
=======
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
>>>>>>> 6cef7fb7a366545c48dd4b2a3872b6a7bd0695a3
