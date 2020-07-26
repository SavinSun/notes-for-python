#CalPiv2.py
from random import random
from time import perf_counter
DARTS = 1000*10000
hits = 0.0
start = perf_counter()
for i in range(1,DARTS+1):
    x, y = random(), random()  #生成的是0-1的随机小数，即单位正方形内计算
    dist = pow(x **2 + y ** 2 , 0.5)
    if dist <= 1.0:
        hits += 1
        pi = 4*(hits/i)
        print("\r计算进度：{:.3f}%,圆周率是:{:.5f},运行时间{:.2f}秒"\
              .format(i/DARTS*100,pi,perf_counter()-start),end="")

pi = 4*(hits/DARTS)
print("圆周率是:{}".format(pi))
print("运行时间是:{}".format(perf_counter()-start))
