import re
result = {}
a = open('score.txt')
lines = a.readlines()
a.close()
print lines
for i in lines:
    name = re.findall(r'[^\W\d]*', i)
    if result.has_key(name[0]):
        pass
    else:
        result[name[0]] = []
        result[name[0]].append(0)
        result[name[0]].append(0)
        result[name[0]].append(0)
    score = re.findall(r'\d+', i)
    result[name[0]][0] += int(score[0])
    result[name[0]][1] += 1
    result[name[0]].append(score[0])
    # print result
statistics = ''
for i in result:
    # print i
    # print result[i]
    result[i][2] = str(round(float(result[i][0])/result[i][1], 1))
    result[i][1] = str(result[i][1])
    result[i][0] = str(result[i][0])
    # global statistics
    statistics += i + ' ' + ' '.join(result[i][0:3]) + '\n'
# print statistics
b = open('result.txt', 'w')
b.write(statistics)
b.close()
