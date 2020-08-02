#接收列表作为参数,如果元素在列表中出现不止一次,则返回True,但不改变列表值
#意思是接收多次列表!
'''def cf(ls):
    s = {}
    for ch in ls:
        s[ch] = s.get(ch,0)+1
    for ch in s:
        if s[ch] > 1:
            return True
ls = input("以空格隔开,回车结束:").split()
print(cf(ls))'''

'''标准答案'''
def main():
    num=[]
    n = input("请输入一组数字(或者直接按回车结束程序):")
    while n!='':
        num.append(eval(n))
        n = input("请输入一组数字(或者直接按回车结束程序):")
    else:
        print("正在处理,请稍等")
        judge(num)

def judge(n):
    if len(n) == len(set(n)):
        print("鉴定完毕,没有重复的元素")
    else:
        print("有重复的元素,总共有{}个".format(len(n) - len(set(n))))
main()