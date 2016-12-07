# coding: utf-8
import os
import re
# 设定统计代码所在目录
program_dir = r'd:\temporary\programs'
# 设定程序当前目录为统计代码所在目录
os.chdir(program_dir)
# 获取目录下所有文件
file_list = os.listdir(program_dir)
print(file_list)
# 初始化统计数据
blank_lines = 0
remark_lines = 0
affect_lines = 0
total_lines = 0
for eve_file in file_list:
    # 组合当前目录与文件名，得到文件完整路径
    file_root = os.path.abspath(eve_file)
    # 只读模式 utf-8 编码打开文件
    open_file = open(file_root, 'r', encoding='utf-8')
    # 按行读取文件
    file_content = open_file.readlines()
    # 关闭文件
    open_file.close()
    print('正在统计：', file_root)
    for line in file_content:
        try:
            # 匹配每行首个非空字符
            first_char = re.search(r'(?<=\s)*\S', line).group()
            # 空行匹配不到，跳过报错
        except AttributeError:
            # 空行则设定字符为空
            first_char = ''
        print(first_char)
        # 判断与统计
        if first_char == '#':
            remark_lines += 1
        elif first_char == '':
            blank_lines += 1
        else:
            affect_lines += 1
        total_lines += 1
print('remark_lines: ', remark_lines)
print('blank_lines: ', blank_lines)
print('affect_lines: ', affect_lines)
print('total_lines: ', total_lines)
