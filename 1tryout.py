fo = open('1.csv',encoding='utf-8')
ls = []
for line in fo:
    #line = line.replace('\n','') #把换行去掉
    ls.append(line.split(','))#以逗号隔开写入列表
fo.close()
print(ls)