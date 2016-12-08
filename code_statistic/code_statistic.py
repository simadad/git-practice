# coding: utf-8
import os
import re
# 设定统计代码所在目录
program_dir = r'd:\temporary\programs'
# 初始化统计数据
blank_lines = 0
remark_lines = 0
affect_lines = 0
total_lines = 0
for root, dirs, files in os.walk(program_dir):
    for every_file in files:
        file_root = os.path.join(root, every_file)
        # 只读模式 utf-8 编码打开文件
        open_file = open(file_root, 'r')
        # 按行读取文件
        file_content = open_file.readlines()
        # 关闭文件
        open_file.close()
        print u'正在统计：', file_root
        for line in file_content:
            # 匹配每行首个非空字符
            first_char = re.search(r'(?<=\s)*\S', line)
            # 判断与统计
            if not first_char:
                blank_lines += 1
            elif first_char.group() == '#':
                remark_lines += 1
            else:
                affect_lines += 1
            total_lines += 1
print '注释行: ', remark_lines
print '空白行: ', blank_lines
print '有效行: ', affect_lines
print '总代码行: ', total_lines
