a = []
n = eval(input()) #共n个整数
a = input().split() 
counts = []
c = 1 #计数初始化
for i in range(n-1): #只循环到第n-2个整数
    if eval(a[i]) +1 == eval(a[i+1]): #如果是连号
        c += 1 
        #print('{}和{}连号!本次连号{}个!'.format(a[i],a[i+1],c))
        if i == n-2 : #如果最后一个也是连号
            counts.append(c) #不然会被直接跳出循环,白记数了
        else:
            continue #c累积起来不重置
    counts.append(c) #单次计数添加进列表中
    c = 1 #重置记数
print(max(counts))
