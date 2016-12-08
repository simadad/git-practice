# coding: utf-8
import re
file_root = 'words.txt'
txt = open(file_root, 'r')
# 以只读方式打开文件
words = txt.read()
# 读取文件内容
txt.close()
# 关闭文件
word_list = re.findall(r'\b\w+\b', words)
# 匹配所有单词
word_numb = len(word_list)
# 统计匹配单词数
print('There are %d words in %s.' % (word_numb, file_root))
# 格式化输出
