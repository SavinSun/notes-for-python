#实例1温度转换
#TempConvert.py
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
    
''' 注释1
注释第二行'''
'''eval("") 将()内的字符串变成程序语句并运行(脱去引号)
e.g. eval("print("1")") 的输出结果为1
'''
