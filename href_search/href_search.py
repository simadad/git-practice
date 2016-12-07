# coding: utf-8
import re
# 只读模式、utf-8 编码打开文件
web = open('web.html', 'r', encoding='utf-8')
# 读取文件
content = web.read()
# 关闭文件
web.close()
# 正则匹配
href_list = re.findall(r'(?<=href=["\'])http\S+(?=["\'])|(?<=value=["\'])http\S+(?=["\'])', content)
print(href_list)
