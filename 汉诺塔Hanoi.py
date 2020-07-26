count = 0
def hanoi(n,a,c,b):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,a,c))
        count +=1
    else:
        hanoi(n-1,a,b,c)
        print("{}:{}->{}".format(n,a,c))
        count +=1
        hanoi(n-1,b,c,a)
hanoi(3,'a','c','b')
print(count)
