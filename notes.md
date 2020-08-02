# Python

## 解决问题6个步骤

* 分析问题
* 划分边界IPO
*Input, Process, Output*
* 设计算法
* 编写程序
* 调试测试
* 升级维护

***

## 命名

* 大小写字母\数字\下划线和汉字
* $\color{red}{大小写敏感\首字符非数字\不与保留字相同}$
![保留字](https://wx3.sinaimg.cn/mw690/6cd6e141ly1gh5duppeqzj20gy07kgp1.jpg)

| and | elif | import | $\color{red}{raise}$ | global |
|:-|:-|:-|:-|:-
|as|else|in|return|$\color{red}{nonlocal}$
|$\color{red}{assert}$|except|$\color{red}{is}$|try|True
|break|finally|lambda|while|False
|$\color{red}{class}$|fo|not|$\color{red}{with}$|None
|continue|from|or|$\color{red}{yield}$|
def|if|pass|del

***

## 缩进

* $\color{red}{语法的一部分}$
* 表达包含和层次关系的**唯一**手段
* 程序内长度一致即可

## 注释

* 单行注释 #123123
* 多行注释 '''开头 结尾'''

***

## 数据类型

* 整数类 123123
* 字符串 "123,123"
![字符串序号](http://wx2.sinaimg.cn/large/6cd6e141ly1gh5g08qtvyj20io08dmyh.jpg)
*由0个活多个字符组成
正向递增序号/反向递减序号*\
0~n　　　　/　　-n~1
  * $\color{red}{索引:<字符串>[M]第M个}$
  * $\color{red}{切片:<字符串>[M:N]第M到N-1个}$ *注意是冒号!!*
* 列表[123,123]
  * 判断元素是否在列表中 in

```python
TempStr[-1] in ['C','c']
```

***

## 分支语句

* if elif else
  * if ...: elif: else:
  * 冒号及后续缩进表示所属关系
* 紧凑形式<表达式1>if<表达式2>else<表达式3>

```python
print("猜{}了".format("对" if guess==9 else "错"))
```

***

## 函数

<函数名>(<参数>)

* input("提示信息")- 以字符串类型保存
* print()
  * print("转换后的温度是{:.2f}C".format(C))
    * {}表示槽,将后续变量C填充其中 :.2f表示取小数点后两位
    * print(,end="")👉默认最后的换行,可换成空白使不换行
    *print("\r单行刷新",end="")　　\r表将光标移至行首*

* eval():去掉参数最外层引号并执行余下语句的函数
![eval函数](http://wx1.sinaimg.cn/large/6cd6e141ly1gh5gvhy82aj20k905vmy3.jpg)
  * 如果直接输入"Hello",由于没定义过Hello,会报错
  * 只拆一层引号,eval("'Hello'")='Hello'

* str.replace(old,new[,max]) 替换函数

```python
#阿拉伯数字转汉字:将n的第c个转换为s的第c个字符,循环
n = input()
s = '零一二三四五六七八九'
for c in '0123456789':
    n = n.replace(c, s[eval(c)])
print(n)
```

* import函数
  * <库>.<函数>(<函数参数>)
  * from<库>import*
    <函数>(<函数参数>)
    *容易出现函数重名!*
  * import<库>as<库别名>

* pow(x,y) 计算x的y次幂

* round(x,d) 对x四舍五入,取d位小数

***

```python
#温度转换 TempConvert.py
TempStr = input("请输入带有符号的温度值:")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
```

***

```python
#Hello World的条件输出
'''获得用户输入的一个整数，参考该整数值，打印输出"Hello World",要求:
如果输入值是0,直接输出"Hello World"
如果输入值>0,以两个字符一行输出"Hello World"
如果输入值<0,以垂直方式输出"Hello World" '''
n = eval(input)
if n==0 :
    print("Hello World")
elif n>0:
    print("He\n''\no \nWo\nrl\nd")
else:
    for c in "Hello World":
    print(c)
```

***

## turtle库-乌龟库

* setup(宽度,高度,起始x,起始y),非必须
* goto(x,y) ![goto](http://wx4.sinaimg.cn/large/6cd6e141ly1gh5i9zj7k4j20g408baac.jpg)







* circle(r,angle) 绕着左边半径为r的圈爬angle角度,默认360 ![circle](http://wx3.sinaimg.cn/large/6cd6e141ly1gh5iasrtpxj20i4075dgm.jpg)







* seth(angle) 只改变方向,绝对角度 ![seth](http://wx4.sinaimg.cn/large/6cd6e141ly1gh5ibik479j20ez08274j.jpg)




* left/right(angle) ![l/r](http://wx1.sinaimg.cn/large/6cd6e141ly1gh5ic0p43lj20f708u3yt.jpg)







* fd/forward/bk(像素点) 向前/向前/向后多少像素点
* penup()/pu()/pendown()/pd() 停止作画/继续作画
*pd()/pendown()只是放下画笔,并不绘制任何内容!*
* colormode() 1.0:RBG小数 (默认255):RBG整数
* pencolor(RGB) ("purple") /(0.63,0.13,0,94)/(160,32,240)

|英文名称|RGB整数值|RGB小数值|中文名称|
|:-:|:-:|:-:|:-:|
|white|255,255,255|1,1,1|白色
|yellow|255,255,0|1,1,0|黄色
magenta|255,0,255|1,0,1|洋红
|cyan|0,255,255|0,1,1|青色
|blue|0,0,255|0,0,1|蓝色
|black|0,0,0|0,0,0|黑色
|seashell|255,245,238|1,0.96,0.93|海贝色
|gold|255,215,0|1,0.84,0|金色
|pink|255,192,203|1,0.75,0.80|粉红色
|brown|165,42,42|0.65,0.16,0.16|棕色
purple|160,32,240|0.63,0.13,0.94|紫色
tomato|255,99,71|1,0.39,0.28|番茄色

* pensize/width(width) 画笔宽度

* **turtle.Turtle().screen.delay(0)** 去除画画延迟
* speed()

|fastest|0|
|:-:|:-:|
|fast|10|
|normal|6|
|slow|3|
|slowest|1|

***

## 循环语句

*while:需要提前对计数器初始化,并每次累加等操作 \
for:自动在循环变量中遍历,维护也不影响*

* for<变量>in range(<次数>):
*<变量>表循环计数,从0到<次数>-1
  * $\color{red}{range(N)产生从0到N-1的整数序列,共N个}$
  * $\color{red}{range(M,N)产生M到N-1的整数序列,共N-M个}$
  * range(M,N,K) -K为步长
  * 字符串穿遍历循环 for c in s:
  * 列表遍历循环 for item in ls:(遍历元素)
  * 稳健遍历循环 for line in fi: fi是文件标识符,遍历每行

* while<条件>: (Crtl+C退出循环)
* break 和 continue
  * break:跳出并结束整个循环
  * continue: 结束当次循环

```python
for c in "PYTHON":
    if c == "T":
        continue
    print(c,end="")
----PYHON

for c in "PYTHON":
    if c == "T":
        break
    print(c,end="")
----PY
```

* else:注意是循环语句中的,非条件语句中
  * 当循环没被break退出,则执行else

***

## random库 随机数(标准库) - 梅森旋转算法

* seed() - 初始化随机种子,默认为当前系统时间
*种子相同,生成的随机数相同
* random() - 生成0.0~1.0之间的随机小数 16位
* randint(a,b) - [a,b]生成整数
* randrange(m,n[,k]) [m,n **)** 之间以k为步长的随机整数 注意不取到最右边
* getrandbits)(k) - 生成一个k比特长的随机整数
* uniform(a,b) - [a,b]之间的随机小数
* choice(seq) - 从序列中随机选择一个元素
* shuffle(seq) - 将序列中元素随机打乱排列

***

```python
#单位正方形内随机点落到圆内的概率
#CalPiV2.py
from random import random
from time import perf_counter
DARTS = 1000* 1000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS+1):
    x,y = random(),random() #生成0-1的随机小数,即单位正方形内计算
    dist = pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits += 1
pi = 4 * (hits/DARTS)
print("圆周率值是:{}".format(pi))
print("运行时间是:{:.5f}s".format(perf_counter() - start()))
```

***

```python
#turtle画画
#PythonDraw.py
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pd()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
```

## 数字类型

* 整数类型:可正可负,无取值范围限制
  * pow(x,y) 计算x的y次幂
* 浮点数类型:带小数点的小数 范围与精度存在限制,常规计算可忽略
  * $\color{red}{浮点数之间运算存在不确定位数(由于二进制来回换算引起),一般在$$10^{-16}$$位置左右产生}$
  * $\color{red}{要用round(x,d):对x四舍五入,截取d位小数}$
  * 可用科学计数法表示
    * 使用e或E作为符号,以10位基数,则$aeb$表示$a*10^{b}$

* 复数类型
  * 与数学一致,定义为$j=\sqrt{-1}$,$a+bj$为复数,a为实部,b为虚部
  *$z=1.23e-4+5.6e+89j$*
  *$z.real/imag$ 获得实部/虚部
  * 不能直接转换,可通过.real和.imag将实部和虚部分别转换

* int(x) - 将float或字符串👉(取整,不四舍五入)整数
* float(x) - 将整数或字符串👉浮点数
* complex(re[,im]) - 生成一个复数,实部为re,虚部为im,re可为整数\浮点数或字符串,im可以是整数或浮点数但不能为字符串

***

## 数值运算操作符

整数->浮点数->复数
运算结果为最宽类型
e.g.整数+浮点数=浮点数 123+4.0=127.0
* \+ \- \* \/👉除 \//👉整除
* x op= y 👉x = x op y <br/>
+=　-=　*=　/=　//=　%　**

***

## 数值运算函数

* abs(x) x的绝对值
* divmod(x,y) - 商余,(x//y,x%y) 同时输出商和榆树
* pow(x,y[,z]) - 幂余,(X**y)%z
* round(x[,d]) 四舍五入,d是保留小数位,默认为0
* max($x_1,x_2,...,x_n$) - 返回最大值
* min($x_1,x_2,...,x_n$) - 返回最小值

***

```python
#天天向上 - 工作日的力量
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i%7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print...
```

```python
#天天向上 - 工作日要多努力?
#DayDayUpQ4.py
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i%7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup
dayfactor=0.01
while dayUP(dayfactor)<37.78:
    dayfactor+=0.001
print("工作日的努力参数是:{:.3f}".format(dayfactor))
```

## 字符串

* 由''\""表示单行字符串
  * 单引号内部可用双引号,双引号内部可用单引号
* 由''' '''\ """ """表示多行字符串
  * 内部可包括单引号和双引号
* 序号![字符串序号](http://wx2.sinaimg.cn/large/6cd6e141ly1gh5g08qtvyj20io08dmyh.jpg)
* 索引:<字符串>[M]第M个字符
* 切片:<字符串>[M:N]从第M到N-1个字符
  * 无M表至开头,无N表示至结尾
  * $\color{red}{<字符串>[M:N:K],根据步长K对字符串切片}$
  *"0123456789"[1:8:2] -"1357" <br\>
  "0123456798"[::-1] - "987654321"*

```python
print(input("请输入需要反转的字符串")[::-1])
```

* 特殊字符 转义符\
  * \b回退 \n换行(光标移动到下行首) \r回车(光标移动到本行首) \t制表符(Tab)
  * \a蜂鸣 \b回退 \f换页 \v垂直制表 \0:NULL

* 字符串操作符

|操作符及使用|描述|
|:-:|:-:|
|x+y|连接两个字符串x和y|
| n\*x 或 x\*n|复制n次字符串x|
|x in s| 如果x是s的字串,返回True,否则返回False|

* 字符串处理函数

|函数及使用|描述|
|:-:|:-|
|len(x)|长度,返回字符串的长度|
|str(x)|任意类型x所对应的字符串形式
|hex(x)或oct(x)|整数x的十六进制或八进制小写形式字符串|
|chr(u)|x为Unicode编码,返回对应字符
|ord(x)|x为字符,返回其对应的Unicode编码

* 字符串处理方法

|方法及使用|描述|
|:-:|:-:|
|str.lower()或str.upper()|返回字符串的**副本**,全部字符小写/大写|
|str.split(seq=None)|返回一个**列表**,由str根据sep被分隔的部分组成
|str.count(sub)|返回字串sub在str中出现的次数|
|str.replace(old,new)|返回字符串str**副本**,所有old字串被替换为new|
|str.center(width[,fillchar])|字符串str根据宽度width剧中,fillchar可选 "python".center(20,"=")👉'=======python======='|
|str.strip(chars)|从str中去掉在其左侧和右侧chars中列出的字符 "= python= ".strp(" =np")👉"ytho"
|str.join(iter)|在iter变量除最后元素外每个元素后增加一个str ",".join("12345")👉"1,2,3,4,5" #主要用于字符串分隔等

* **str.split() 当括号内为空,则按字符串内字符中间的空格分隔,若括号内为' ',则会把开头或结尾的空格一并转为列表的一部分**

```python
>>> nums = ' 1 2 3 '
>>> nums.split()
['1', '2', '3']
>>> nums = ' 1 2 3 '
>>> nums.split(' ')
['', '1', '2', '3', '']
```


### 方法 特指\<a>,\<b>()中的\<b>()

* 字符串类型的格式化
{<参数序号>:<格式控制标记>}

|:|<填充>|<对齐>|<宽度>|<,>|<.精度>|<类型>
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|引导符号|用于填充的单个字符|<左对齐 <br/>>右对齐 <br/> ^居中对齐| 槽设定的输出宽度|数字的千位分隔符|浮点数小数精度 或 <br/> 字符串最大输出长度| 整数类型 <br/> b,c,d,o,x,X <br/> 浮点数类型 <br/> e,E,f,%|

<模板字符串>.format(<参数1>,<参数2>,...)

* 槽:字符串中的{},与format中的{}按顺序一一对应

* 大小比较时,是从左到右比较字符的ascii码大小 ※ 大写英文字母<小写英文字母

```python
#WeekNamePrintV1.py
WeekStr = "一二三四五六日"
weekID = eval(input("请输入星期数字(1-7):"))
print("星期"+WeekStr[weekID-1])
```

***

## time库 时间库

* 时间获取函数

|函数|描述|
|:-:|:-:|
|time()|获取当前时间戳,浮点数
|ctime()|获取当前时间并以易读方式表示,返回字符串 <br/> 'Fri Jan 26 12:11:16 2018'|
|gmtime()|获取当前时间,表示为计算机可处理的时间格式 <br/> time.struct_time(time_year=2018, tm_mon=1, tm_mday=26, tm_hour=4, tm_min=11, tm_sec=16, tm_wday=4, tm_yday=26, tm_isdst=0)|

*时间格式化函数

|函数|描述|
|:-:|:-:|
|strftime(tpl, ts)| tps是格式化模板字符串,用来定义输出效果,ts是计算机内部时间类型变量 <br/> t = time.gmtime() <br/> time.strftime('%Y-%m-%d %H:%M%S', t) <br/> '2020-07-28 12:15:30'|
|strptime(str,tpl)|str是字符串形式的时间值 <br/> tpl是格式化模板字符串,用来定义输入效果 <br/> \>>> t = time.gmtime() <br/> \>>> time.strftime("%Y-%m-%d",t)  <br/> '2020-07-28'  <br/> \>>> timeStr = '2020-07-28' <br/>  \>>> time.strptime(timeStr,'%Y-%m-%d')  <br/> time.struct_time <br/>  (tm_year=2020, tm_mon=7, tm_mday=28, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=210, tm_isdst=-1) |

|格式化字符串|日期/时间说明|值范围和实例
|:-:|:-:|:-:|
|%Y|年份|0000~9999
|%m|月份|01~12
|%B|月份名称|January~December
|%b|月份名称缩写|Jan~Dec
|%d|日期|01~31
|%A|星期|Monday~Sunday
|%a|星期缩写|Mon~Sun
|%H|小时(24)|00~23
|%I|小时(12)|01~12
|%p|上/下午|AM,PM
|%M|分钟|00~59
|%S|秒|00~59

* 程序计时

|函数|描述|
|:-:|:-:|
|perf_counter()|返回一个Cpu级别的精确时间计数值,单位为秒 <br> 由于这个计数值起点不确定,连续调用差值才有意义
|sleep(s)|程序休眠多少秒

***

## 进度条的不同设计函数

|设计名称|趋势|设计函数
|:-:|:-:|:-:|
|Linear|Constant|f(x)=x
|Early Pause|Speeds up|f(x)=x+(1-sin(x\*$\pi$*2+$\pi$/2)/-8
|Late Pause|Slows down|f(x)=x+(1-sin(x\*$\pi$*2+$\pi$/2)/8
|Slow Wavy|Constant|f(x)=x+sin(x\*$\pi$\*5)/20
|Fast Wavy|Constant|f(x)=x+sin(x\*$\pi$\*20)/80
|Power|Speeds up|f(x)=(x+(1-x)*0.03)$^2$
|Inverse Power|Slows down|f(x)=1+(1-x)$^{1.5*}$-1
|Fast Power|Speeds up|f(x)=(x+(1-x)/2)$^8$
|Inverse Fast Power|Slows down|f(x)=1+(1-x)$^{3*}$-1

***

## 条件判断

* 条件判断符
\< \> \<= \>= \== \!=

* 条件组合
x $\color{red}{and}$y x$\color{red}{or}u$ x$\color{red}{not}$y

***

## 异常处理

```python
try:
<>
except [<异常类型>]:#如NameError
<>
[else:] #不异常时执行
<>
[finally:] #一定会执行
<>
```

***

## math库

* 常数
  
|pi|$\pi$ 3.141 592 653 589 793
|:-:|:-:|
|e| $\e$ 2.718 281 828 459 045
|inf| infinite 正无穷大
|-math.inf| 负无穷大
|nan|非浮点数标记,NaN(Not a Number)|

* 函数

|fabs(x)|绝对值
|:-:|:-:|
|fmod(x,y)|x%y
|$\color{red}{fsum([x,y,...])}$|$\color{red}{浮点数精确求和}$
|ceil(x)|返回不小于x的最小整数,向上取整
|floor(x)|返回不大于x的最大整数,向下取整
|factorial(x)|x! 返回x 的阶乘,x为小数/负数👉ValueError
|gcd(a,b)|返回a与b的最大公约数
|frepx(x)| x=m×2e 返回(m,e),当x=0,返回(0.0,0)
|ldexp(x,i)|$x*2^i$,math.frepx(x)的反运算
|modf(x)|返回x的小数和整数部分
|trunc(x)|返回x的整数部分
|copysign(x,y)|用数值y的正负号代替数值x的正负号
|isclose(a,b)|比较a和b的相似性,返回True或False
|isfinite|当x为无穷大返回True,反之亦然
|isinf(x)|当x为正数或负无穷大,返回True,反之亦然
|isnan(x)|当x是NaN,返回True,反之亦然

*幂对数函数

|pow(x,y)|x的y次幂
|:-:|:-:|
|exp(x)|$e^x$
|sqrt(x)|$\sqrt{x}$
|log(x[,bae])|$log_{base}x$返回x的对数值,只输入x则返回ln x
|log1p(x)|$ln(1+x)$
|log2(x})|$logx$
|log10(x)|$log_{10}x$

 *可通过math.pow()间接求解x开y根  
$\sqrt[y]{x}=x^{\frac{1}{y}}$  
math.pow(10,1/3)👉$\sqrt[3]{10}$*

* 三角运算函数

|degree(x)|x的弧度值转角度值|
|:-:|:-:|
|radians(x)|角度值转弧度值|
|hypot(x,y)|(x,y)的坐标到原点的距离 $\sqrt{x^2+y^2}$
|sin(x)等|输入弧度值

* 高等特殊函数

|erf(x)|高斯误差函数$\frac{2}{\sqrt{\pi}}\int^{x}_{0}e^{-t^2}dt$
|:-:|:-:|
|erfc(x)|余补高斯误差函数$\frac{2}{\sqrt{\pi}}\int^{\infty}_{x}e^{-t^2}dt$
|gamma(x)|伽马函数,欧拉第二积分函数,可计算浮点数的阶乘 $\int^{\infty}_{0}x^{t-1}e^{-x}dx$
|lgamma(x)|伽马函数的自然对数$ln(gamma(x))$

***

## def函数 自定义函数

* 定义
  * 参数可无,括号必须有
  * 可变参数 *b:可有多个参数
  ![可变参数](http://wx4.sinaimg.cn/large/6cd6e141ly1gh6mwclgczj20gh07vaba.jpg)

```python
def <函数名>([<必选参数>][<可选参数(可默指定默认值n=1)>][,<可变参数 *b>]):
  <>
  return [<返回参数>]
```

* 参数传递可按位置或名称方式传递

```python
fact(10,5)
fact(m=5,n=10)
```

* 局部变量和全局变量
  * 函数中默认为局部变量,可与全局变量重名,不影响
  * 可用global<全局变量>声名再函数内部使用全局变量
  * **全局变量中,如果创建了组合数据类型ls,且未在局部变量中被再次创建,则局部变量ls为全局变量ls**

```python
ls = ['F','f'] #使用[]真实创建了一个全局变量列表ls
def func(a):
  ls.append(a) #此处ls为列表类型,未真实创建,则等同于全局变量
  return
func("C") #全局变量ls被修改
print(ls)
>>>['F','f','c']
```

```python
ls = ['F','f'] #通过使用[]真实创建了一个全局变量ls
def func(a):
  ls = []
  ls.append(a)#此处ls是列表类型,真实创建,ls为局部变量
  return
func("C")#修改的是局部变量的ls
print(ls)
>>>['F','f']
```

* lambda函数 *一般还是用def*
  * 匿名函数,函数名为返回结果
  * 用于定义简单的\一行内表达的函数
  * <函数名>=lambda<参数>:<表达式>

```python
>>>f = lambda x,y: x+y
>>>f(10,15)
25
>>> f = lambda : "lambda函数"
>>>print(f())
lambda函数
```

***

```python
#七段数码管 V2
#SevenDigitsDrawV2.py
import turtle,time

def drawGap():#绘制数码管间隔
    turtle.pu()
    turtle.fd(5)

def drawLine(draw):#绘制单段数码管
    drawGap()
    turtle.pd() if draw else turtle.pu()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(digit):#根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.pu()
    turtle.fd(20)

def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write("月",font=("Arial",18,"normal"))
            turtle.fd(40)
        elif i == '+':
            turtle.write("日",font=("Arial",18,"normal"))
            turtle.fd(40)
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.pu()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()
```

***

## 递归函数

* 链条
* 基例:一个或多个不需要再次递归的基例  

$$n! = \begin{cases}
   1 & n = 0  \\
   c &\text{otherwise}
\end{cases}$$

```python
def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
```

```python
#字符串反转
def rvs(s):
  if s=="":
    return s
  else:
    return rvs(s[1:])+s[0]

#input()[::-1] 同样效果
```

![汉诺塔](http://wx4.sinaimg.cn/large/6cd6e141ly1gh6ohsdcyqj206303g748.jpg)

```python
#汉诺塔
count = 0
def hanoi(n, src, dst, mid): #(多少个,源柱,目的,中转)
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst)) #(将源柱的最后一个转到目标柱)
        count += 1
    else :  
        hanoi(n-1,src,mid,dst) #先将前一个从源柱转移到中转 (原来的中转变为此时的目的柱)
        print("{}:{}->{}".format(n,src,dst))
        count +=1
        hanoi(n-1, mid , dst, src) #从中转柱移到目的柱,以源柱为中转
```

***

```python
#科赫雪花小包裹
#KochDrawV2.py
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
           turtle.left(angle)
           koch(size/3, n-1)
def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3      # 3阶科赫雪花，阶数
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
main()
```

***

## pyinstaller库

* 封装程序用
* cmd pyinstaller -F<文件名.py>
* 常用参数
  * -h 查看帮助
  * --clean 清理临时文件
  * -D, --onedir 默认值,生成dist文件
  * -F,--onefile 在dist文件夹中只生成独立的打包文件
  * -i<图标文件名.ico>指定打包程序使用的图标文件

```python
pyinstaller -i a.ico -F a.py
```

***

## datetime库

* datime方法

|now()|返回datetime类型,日期+时间,精确到微秒 <br> now = datetime.now() <br> >>>now​ <br> datetime.datetime(2020, 7, 24, 11, 11, 49, 321898)​ <br>>>>print(now) <br> 2020-07-24 11:11:49.321898|
|:-:|:-|
|utc()|返回当前日期和时间对应的UTC(世界标准时间)<br>now = datetime.utcnow()<br>>>>today<br>datetime.datetime(2020,7,24,3,13,44,11443)<br>>>>print(now><br>2020-07-24 03:13:44.0011443|
|datetime()|返回一个datetime类型,表**指定的**日期和时间,可精确到微秒 <br>datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)<br>#hour及之后的参数可全省略或部分省略，取值不能到最大值(hour<24,minute<60,etc)<br>0<=microsecond<1000000​<br>now = datetime(2020,7,24,11,20,32,7)​​<br>>>>now<br>datetime.datetime(2020, 7, 24, 11, 20, 32, 7)​​|

* datetime类属性

min|固定返回最小时间对象👉datetime(1,1,1,0,0)
:-:|:-:
max|固定返回最大时间对象👉datetime(9999,12,31,23,59,59,999999)
year|返回年份
month|返回月份
day|返回日期
hour|返回小时
minute|返回分钟
second|返回秒钟
microsecond|返回微秒

* 时间格式化方法

isoformat()|采用ISO8601标准显示时间
:-:|:-:
isoweekday()|根据日期计算,返回1-7,对应星期几
strftime(format)|根据**格式化字符串**format进行格式显示的方法

* 格式化字符串 左侧会自动补零

| 格式化字符串 | 日期/时间 | 指范围和实例 |
| --- | --- | --- |
| %Y | 年份 | 0001~9999 |
| %m | 月份 | 01~12 |
| %B | 月名 | January~December |
| %b | 月名缩写 | Jan~Dec |
| %d | 日期 | 01~31 |
| %A | 星期 | Monday~Sunday |
| %a | 星期缩写 | Mon~Sun |
| %H | 小时(24h制) | 00~23 |
| %I (注意是i)| 小时(12h制) | 01~12 |
| %p | 上/下午 | AM,PM |
| %M | 分钟 | 00~59 |
| %S | 秒 | 00~59 |
| %W | 一年的第几周 | 00~53|
| %f | 微秒 | 000000~999999|

```python
>>> now = datetime.now()
>>> now.isoformat()
'2020-07-24T13:50:31.289896'
>>> now.isoweekday()
5
>>> now.strftime("%Y-%m-%d %H:%M:%S")
'2020-07-24 13:50:31'
>>> print("今天是{0:%Y}年{0:%m}月{0:%d}日".format(now))
今天是2020年07月24日
```

```python
#5.10 请利用datetime库将当前系统时间转换为字符串
from datetime import datetime#记住，用的是datetime库里的datetime类方法
now = str(datetime.now())
print(now)
>>>2020-07-28 15:53:28.167207
```

```python
#5.11 请利用datetime库输出5种不同的日期格式
from datetime import datetime
now = datetime.now()
print("{0:%Y}-{0:%m}-{0:%d} {0:%H}:{0:%M}:{0:%S} {0:%a}".format(now))
print("{0:%Y}-{0:%B}-{0:%d} {0:%A} {0:%I}:{0:%M} {0:%p}".format(now))
#etc...
```

```python
#5.12 思考如何利用datetime库对一个程序的运行计时⏲
from datetime import datetime
then = datetime.now()
for i in range(10000):
    i += 1
now = datetime.now()
took = now - then
print("花了{}微秒".format(took.microseconds))
```

***

## Python内置函数

abs() | id() | round() | compile() | locals()|
:-:|:-:|:-:|:-:|:-:|
all()|input|set()|dir()|map()|
any()|int()|sorted()|exec()|memoryview()|
asci()|len()|str()|enumerate()|next()|
bin()|list()|tuple()|filter()|object()|bool()|max()|type()|format()|property()|
chr()|min()|zip()|frozenset()|repr()|
complex()|oct()|getattr()|setattr()|
dict()|open()||global()|slice()|
divmod()|ord()|bytes()|hasattr()|staticmethod()|
eval()|pow()|delattr()|help()|sum()|
float()|print()|byterray()|isinstance()|super()|
hash()|range()|callable()|issublass()|vars()|
hex()|eversed()|classmethod()|iter()|\_\_import()\_\_|

all(): 一般针对组合数据类型,如每个元素都True则True.**整数0\空字符串\空列表都为False**  
any(): 与all()相反,全部为False才False  
hash(): 对于能够计算哈希的类型返回哈希值  
id(): 对于每个数据返回唯一编号,可通过比较编号是否相同判断变量数据是否一致  
*Python将数据存储在内存中的地址作为唯一编号*  
reversed(): 返回输入组合数据类型的逆序形式  
sorted(): 对一个序列,默认从小到大进行排序  
type(): 返回每个数据对应的类型  

```python
>>> ls = [1, 2, 5, 0]
>>> all(ls)
False
>>> any(ls)
True
>>> hash("中国，你好")
-1904098869
>>> id(ls)
58109864
>>> id("中国，你好")
60471440
>>> list(reversed(ls))
[0, 5, 2, 1]
>>> sorted(ls) #不改变ls的值
[0, 1, 2, 5]
>>> ls
[1, 2, 5, 0]
>>> sorted(ls, reverse=True)
[5, 2, 1, 0]
>>> type(ls)
<class 'list'>
>>> type(reversed(ls))
<class 'list_reverseiterator'>
```

```python
#5.26 请使用len()函数对整数\浮点数\字符串进行类型长度计算,解释看到的结果
>>> len(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    len(a) #不可计算
TypeError: object of type 'int' has no len()
>>> len(b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    len(b)
TypeError: object of type 'float' has no len() #不可计算
>>> len(c)
0
```

![田字格](http://wx1.sinaimg.cn/large/6cd6e141ly1gh6quqh61oj20ac0a974x.jpg)

```python
#5.1 程序练习题3.5输出了一个简单的田字格,用函数简化其代码,输出如图5.12所示的更大田字格

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

```python
#实现multi()函数,参数个数不限,返回所有参数的乘积
str = input("以逗号隔开")
def multi(str):
  b = 1
  for i in (str):
    b *= int(str)
  return b
print(multi(str))
```

```python
#实现isPrime()函数,参数为整数,要有异常处理.如果整数是质数,返回True,否则返回False
def isPrime(a):
  if a<3:
    return True
  else:
    for i in range(2,a):
      if a%i !=0 and i == a-1:
        return True
      elif a%i == 0 :
        return False
try:
  a = eval(input())
  if type(a) != int or a<1:
    print("Error")
  print(isPrime(a))
except:
  print("Error1")
```

## $\color{red}{要先定义了函数,才可以使用}$

***

## 集合类型的定义

* 与数学中概念一致
* 元素之间**无序**,每个元素**唯一**,不存在相同元素
* 元素**不可更改**,不能是可变数据类型

* 用大括号{}表示,元素间用逗号分隔
* 建立集合类型用{}或set()
* **建立空集合类型,必须用set()**

```python
>>> A = {"p","y",123}
>>> B = set("pypy123")
>>> A-B
{123}
>>> A&B
{'p', 'y'}
>>> A^B
{'2', '3', 123, '1'}
>>> B-A
{'3', '2', '1'}
>>> A|B
{'3', '1', 'p', '2', 'y', 123}
```

### 集合操作符

操作符及应用|描述
:-:|:-:
S \| T|并,返回新集合
S - T|差,返回新集合
S & T|交,返回新集合
S ^ T|补,返回新集合
S <= T 或S < T|返回True/False,判断S和T的子集关系
S >= T 或 S > T|返回True/False,判断S和T的包含关系
S \|= T|并
S -= T|差
S &= T|交
S ^= T|补

### 集合处理方法

S.add(x)|如果x不在集合S中,将x增加到S
:-:|:-:
S.discard(x)|移除S中元素x,如果x不在集合S中,不报错
S.remove(x)|移除S中元素x,如果x不在集合S中,产生KeyError异常
S.clear()|移除S中所有元素
S.pop()|随机取出S的一个元素,更新S,若S为空产生KeyError异常
S.copy()|返回集合S的一个副本
len(S)|返回集合S的元素个数
x in S|判断S中元素x,x在集合S中,返回True,否则返回False
x not in S|判断S中元素x,x不在集合S中,返回True,否则返回False
set(x)|将其他类型变量x转变为集合类型

### 应用场景

包含关系比较

```python
>>> 'p' in{'p','y',123}
True
>>> {'p','y'} >= {'p','y',123}
False
```

数据去重:集合类型所有元素无重复

```python
>>> ls = ['p','p','y','y',123]
>>> s = set(ls)
>>> s
{'p', 123, 'y'}
>>> lt = list(s)
>>> s
{'p', 123, 'y'}
```

***

## 序列

* 一维元素向量,元素类型可以不同
* 类似数学元素序列,$s_0,S_1,...,S_{n-1}$
* 元素间由序号引导,通过下标访问序列的特定元素
* 序列类型定义
  * 字符串类型
  * 元组类型
  * 列表类型
* 序号定义
![序号](http://wx1.sinaimg.cn/large/6cd6e141ly1gh7y51is4nj20j207cwfc.jpg)

* **切片默认参数设置值**  
**格式：[开头：结束：步长]  
开头：当步长>0时，不写默认0。当步长<0时，不写默认-1  
结束：当步长>0时，不写默认列表长度。当步长<0时，不写默认负的列表长度减一  
步长：默认1，>0 是从左往右走，<0是从右往左走(▽)**  

### 序列类型通用操作符

操作符及应用|描述
:-:|:-:|
x in s|如果x是序列s的元素,返回True,否则返回False
x not in s|如果x是序列s的元素,返回False,否则返回True
s + t|连接两个序列s和t
s\*n或n\*s|将序列s复制n次
s[i]|索引,返回s中的第i个元素,i是序列的序号
s[i:j] 或s[i:j:k]|切片,返回序列s中第i到j以k为步长的元素子序列

```python
>>> ls = ['python',123,'.io']
>>> ls[::-1]
['.io', 123, 'python']
>>> s = 'python123.io'
>>> s[::-1]
'oi.321nohtyp'
```

### 序列类型通用函数和方法

函数和方法|描述
:-:|:-:
len(s)|返回s的长度,即元素个数
min(s)|返回最小元素,**s中元素需要可比较**
max(s)|返回最大元素,**s中元素需要可比较**
s.index(x[,i,j])|返回序列s从i到j位置中第一次出现元素x的位置
s.count(x)|返回x出现的总次数

***

### 元组

#### 元组类型定义

* 是一种序列类型,一旦创建就不能被修改
* 使用小括号()或tuple()创建,元素间用逗号,分隔
* 可以使用或不使用小括号

```python
>>> a = '1','2','3','4'
>>> a
('1', '2', '3', '4')
>>> b = ('a','b','c')
>>> b
('a', 'b', 'c')
```

### 列表

#### 列表类型定义

* 是一种序列类型,创建后**可以随意被更改**
* 使用方括号[]或list()创建,元素间用逗号,分隔
* 列表中各元素类型**可以相同**,无长度限制
* 使用[]才是真实创建列表,赋值仅表达传递引用,内存地址相同

```python
>>> a = ['cat','dog']
>>> b = a #[]才是真正创建列表,赋值仅表达传递引用
>>> b
['cat', 'dog']
>>> a.append('pussy')
>>> a
['cat', 'dog', 'pussy']
>>> b
['cat', 'dog', 'pussy']
```

***

* **将列表中的字符串转为数字**
  n = ['1','2','3'] 👉 n = [1,2,3]
  2种方法--

  ```python
  for i in len(n):
    n[i] = eval(n[i])
  ```

  ```python
  n = list(map(int, n))
  ```
  
***

#### 列表类型操作函数和方法

函数或方法|描述
:-:|:-:|
ls[i] = x|替换列表ls第i元素为x
ls[i:j:k] = lt|用列表lt替换ls切片后所对应元素子列表
del ls[i]|删除列表ls中第i元素
ls += lt|更新列表ls,将列表lt元素增加到列表ls中
ls *n= n|更新列表ls,其元素重复n次

```python
>>> ls = ['cat','dog','tiger',1024]
>>> ls[1:2] = [1,2,3,4] #将后面的列表元素替换第1个元素并继续向后插入
>>> ls
['cat', 1, 2, 3, 4, 'tiger', 1024]
>>> del ls[::3]
>>> ls
[1, 2, 4, 'tiger']
>>> ls*2
[1, 2, 4, 'tiger', 1, 2, 4, 'tiger']
>>> ls = ['cat','dog','tiger',1024]
>>> ls[1] = [1,2,3,4] #将后面的列表看作一个元素,替换第1的元素
>>> ls
['cat', [1, 2, 3, 4], 'tiger', 1024]
```

函数或方法|描述
:-:|:-:|
ls.append(x)|在列表最后增加**一个**元素x
ls.clear()|删除列表ls中所有元素
ls.copy()|生成一个新列表,赋值ls所有元素
ls.insert(i,x)|在列表ls的第i位置增加元素x
ls.pop(i)|在列表ls中第i位置元素取出并删除该元素
ls.remove(x)|将列表ls中出现的第一个元素x删除
ls.reverse()|将列表ls中的元素反转

```python
>>> ls = ['cat','dog','tiger',1024]
>>> ls.append(1234)
>>> ls
['cat', 'dog', 'tiger', 1024, 1234]
>>> ls.insert(3,'human')
>>> ls
['cat', 'dog', 'tiger', 'human', 1024, 1234]
>>> ls.reverse()
>>> ls
[1234, 1024, 'human', 'tiger', 'dog', 'cat']
```

* ls列表类型内可有多个括号,取出时按从大到小顺序排ls[][][]

```python
>>> ls = [(1,(2,3,(5,6),4),7),8]
>>> ls[0]
(1, (2, 3, (5, 6), 4), 7)
>>> ls[0][1]
(2, 3, (5, 6), 4)
>>> ls[0][1][2]
(5, 6)
>>> ls[0][1][2][1]
6
```


### 序列类型应用场景

* 元组用于元素不改变的应用场景,更多应用于固定搭配场景(可用于数据保护)
* 列表更加灵活,最为常用
* 最主要作用:表示一组有序数据,进而操作它们

***

### 基本统计值

* 总个数:len()
* 求和:for in
* 平均值:求和/总个数
* 方差:各数据与平均数差的平方和的平均数
* 中位数:排序,然后1.奇数找中间,偶数找中间2个平均

```python
#CalstatisticsV1.py
def getNum(): #获取用户不定长度的输出
  nums = []
    nums = []
    iNumStr = input("请输入数字(回车退出):")
    while iNumStr != ""
      nums.append(eval(iNumStr))
      iNumStr = input("请输入数字(回车退出):")
    return nums

def mean(numbers):#计算平均值
  s = 0.0
  for num in numbers:
    s = s + num
  return s / len(numbers)

def dev(numbers, mean): #计算方差
  sdev = 0.0
  for num in numbers:
    sdev = sdev +(num - mena)**2
  return pow(sdev / (len(numbers)-1),0.5)

def median(numbers):
  sorted(numbers)
  size = len(numbers)
  if size %2 == 0:
    med = (numbers[size//2-1] + numbers[size//2])/2
  else:
    med = numbers[size//2]
  return med

n = getNum()
m = mean(n)
print("平均值:{},反差:{:.2},中位数:{}."format(m,dev(n,m),median(n)))
```

***

### 字典

#### 字典类型定义

* 映射:一种键(索引)和值(数据)的对应 ![映射](http://wx3.sinaimg.cn/large/6cd6e141ly1gh861g893nj20fx04ywf3.jpg)
*序列类型由0~N整数作为数据的默认索引,映射类型则由用户为数据定义索引
* 键值对:键是数据索引的扩展
* 字典:键值对的集合,键值对之间**无序**
* 采用大括号{}和dict()创建,键值用冒号:表示  
*<字典变量> = {<键1>:<值1>,...<键n>:<值n>}*  
*<值> = <字典变量>[<键>] <字典变量>[<键>] = <值>*  
*[]用来向字典变量中索引或增加元素*

* 错误创建案例 d = {[1,3]:1} 原因:[1,3]为列表,列表可变,不能作为键使用

#### 字典类型操作函数和方法

函数或方法|描述
:-:|:-:
del d[k]|删除字典d中**键**k对应的数据值
k in d|判断键k是否在字典d中,如果在返回True,否则False
d.keys()|返回字典d中所有的键信息
d.values()|返回字典d中所有的值信息
d.items()|返回字典d中所有的键值对信息
$\color{red}{d.get}$(k,/<default>;)|键k存在,则返回相应值,不在则返回/<default>值
d.pop(k,<default>)|键k存在,则取出相应值,不在则返回<default>值
d.popitem()|随机从字典d中取出一个键值对,以元组形式返回
d.clear()|删除所有的键值对
len(d)|返回字典d中元素的个数

### jieba库 结巴库

* 优秀的中文分词第三方库
* 中文文本需要通过分词获得单个的词语
* 利用中文词库,确定中文字符之间的关联概率,并将概率大的组成词组
* 可添加自定义词组

#### jieba使用

* 精确模式:不存在荣誉单词
* 全模式:返回所有可能的词语,有冗余
* 搜索引擎模式:在精确模式基础上,对长词再次切分

函数|描述
:-:|:-
**jieba.lcut(s**)|精确模式,返回一个列表类型的分词结果 <br>>>>jieba.lcut("中国是一个伟大的国家") <br> ['中国','是','一个','伟大','的','国家']
jieba.lcut(s,ccut_all=True)|全模式,返回一个列表类型的分词结果,存在冗余 <br>>>>jieba.lcut("中国是一个伟大的国家",cut_all=True)<br>['中国','国是','一个','伟大','的','国家']
jieba.lcut_for_search(s)|搜索引擎模式,返回一个列表类型的分词结果,存在冗余<br>>>>jieba.lcut_for_search("中华人民共和国是伟大的")<br>['中华','华人','人民','共和','共和国','中华人民共和国','是','伟大','的']
jieba.add_word(w)|向分词词典增加新词w<br>>>>jieba.add_word("蟒蛇语言")

```python
#英文词频统计-Hamlet为例
#CalHamletV1.py
def getText():
  txt = open("hamlet.txt","r").read()#打开txt文档
  txt = txt.lower() #归一化为小写
  for ch in '!"#$&()*+,-./:;<=>?@[\\]^_{}|':
    txt = txt.replace(ch,' ') #把标点符号全部改为空格,使单词之间以空格分开
  return txt

hamletTxt = getText()
words = hamletTxt.split() #以空格把单词全部分开,返回列表
counts = {} #创建空字典
for word in words:
  counts[word] = counts.get(word,0)+1 #如果word没在字典里,则添加键值对并赋+1
items = list(counts.items())#将字典转为列表
items.sort(key=lambda x:x[1], reverse=True) #将列表以键值对的第二个元素(即出现次数)从大到小的顺序排列返回
for i in range(10):
  word, count = items[i] #输出前十的单词和频率
  print("{0:<10}{1:>5}".format(word, count))
```

```python
#中文词频统计-三国演义为例
#CalThreeKingdomsV2.py
import jieba
txt = open("threekingdoms.txt","r",encoding="utf-8").read()
excludes = {"将军","却说","荆州","二人","不可","不能","如此"}
words = jieba.lcut(txt)
counts = {}
for word in words:
  if len(word) ==1:
    continue
  elif word == '诸葛亮' or word == '孔明曰':
    rword = '孔明'
  elif word == '关公' or word == '云长':
    rword = '关羽'
  elif word == '玄德' or word == '玄德曰':
    rword = '刘备'
  elif word == '孟德' or word == '丞相':
    rword = '曹操'
  else:
    rword = word
  counts[rword] = counts.get(rword,0) + 1
for word in excludes:
  del counts[word]
items = list(counts.item())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
  word, count = items[i]
  print("{0:<10}{1:>5}".format(word, count))
```
