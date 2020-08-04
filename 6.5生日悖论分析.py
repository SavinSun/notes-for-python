def bir():
    from random import randint
    mon = randint(1,12) #随机月份
    if mon in [1,3,5,7,8,10,12]:
        day = randint(1,31)
    elif mon == 2:
        day = randint(1,28)
    else:
        day = randint(1,30)
    return mon*100+day #方便比较是否重复

def cp(n):
    ls = []
    for i in range(n): #随机出每人的生日
        ls.append(bir())
    if len(ls) == len(set(ls)):
        return False
    else:
        return True

try:
    personnum = eval(input("请输入房间人数:"))
    poss = 0
    mean = 0.0
    for n in range(1000,20000,1000): #从1000次开始,每次多测1000次,共测20000次
        for i in range(n):
            if cp(personnum) == True:
                poss +=1
        mean += poss*100/n
        poss = 0
    print("当房间内的人数为{}时,至少有两个人生日相同的概率是{:.2f}%.".format(personnum,mean/10))
except:
    print("输入有误")