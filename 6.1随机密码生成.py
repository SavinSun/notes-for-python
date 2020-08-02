import random
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
for i in range(8):
    print('第{}次生成的密码是:'.format(i+1),end='')
    for c in range(10):
        print(a[random.randint(0,35)],end='')
    print('')


'''标准答案
from random import randint
def rancre():
mi=''
for i in range(8):
u = randint(0,62)
if u>=10:
if 90<(u+55)<97:
 mi+=chr(u+62)
else:
mi+=chr(u+55)
print("{} ".format(u+55),end="") 
else:
 mi+='%d'%u
return mi
def main():
for i in range(1,11):
print("生成的第{}个密码是：{}".format(i,rancre()))
main()
'''
