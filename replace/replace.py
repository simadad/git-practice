# -*- coding:utf-8 -*-
# 获取屏蔽词库
testfile = open('shieldWords.txt', 'r')
testwords = testfile.readlines()
# 输入待屏蔽语句
log = raw_input('press something\n')
# 待屏蔽词解码
testlog = log.decode('utf-8')
# 逐词比对
for i in testwords:
    # 屏蔽词解码
    testword = i.strip().decode('utf-8')
    if testword in testlog:
        # 屏蔽词替换
        testlog = testlog.replace(testword, '*' * len(testword))
print (testlog)
