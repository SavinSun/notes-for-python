n = eval(input())
for i in range(1,n+1,2):  #2是步长
    print("{0:^{1}}".format('*'*i, n))  #{1}是宽度
