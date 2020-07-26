s = input()
t = ""
for c in s: #字符串循环？
    if 'a' <= c <= 'z': #原来可以这样吗
        t += chr( ord('a') + ((ord(c)-ord('a')) + 3 )%26 )
        #注意看括号！先减法，后加法，后模运算，再加a再转成字母
    elif 'A' <= c <= 'Z':
        t += chr( ord('A') + ((ord(c)-ord('A')) + 3 )%26 )
    else:
        t += c #本来是字符串，所以也是字符串连接
print(t)
