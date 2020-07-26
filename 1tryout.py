def top():
    t = ('+' + '--'*4)
    return t*4 + '+'


def body():
    b = ('|' + ' '*8 )
    return b*5

 #拼接起来即可
for i in range(4):
    print(top())
    for i in range(4):
    	print(body())
print(top())
#————————————————
#版权声明：本文为CSDN博主「UndeFIned丶」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/weixin_46313446/article/details/105510984
#edit 1st time
#分支测试
