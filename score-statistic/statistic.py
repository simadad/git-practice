# -*- coding: utf-8 -*-
import re
import chardet
# 预设成绩统计字典   人名：成绩
result = {}
# 提取成绩文件
a = open('score.txt')
lines = a.readlines()
a.close()
# print lines                      # 检测

# 各人成绩统计
# 遍历成绩条
for i in lines:
    # 匹配人名：非空白符、非数字
    name = re.findall(r'[^\s\d]*', i)
    # 非重复添加人名至成绩统计字典
    if name[0] in result:
        pass
    else:
        # 添加新成员
        result[name[0]] = []
        # 预留统计数据
        # 预留总分数据
        result[name[0]].append(0)
        # 预留考试次数数据
        result[name[0]].append(0)
        # 预留平局成绩
        result[name[0]].append(0)
    # 匹配成绩：至少一位数字
    score = re.findall(r'\d+', i)
    # print (score)                     # 检测
    # 统计总分
    result[name[0]][0] += int(score[0])
    # 统计考试次数
    result[name[0]][1] += 1
    # 添加历次考试成绩
    result[name[0]].append(score[0])
    # print (result)                    # 检测

# 最终统计结果记录
statistics = ''
# 遍历各人统计成绩
for i in result:
    # 字符转换
    # 统计平均成绩
    result[i][2] = str(round(float(result[i][0])/result[i][1], 1))
    result[i][1] = str(result[i][1])
    result[i][0] = str(result[i][0])
    # 最终结果组合
    statistics += i + '：' + ' '.join(result[i][0:3]) + '\n'
# print (statistics)                    # 检测

# 结果保存
b = open('result.txt', 'w')
b.write(statistics)
b.close()
