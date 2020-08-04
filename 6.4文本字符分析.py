def cp():
    n = input("请输入一段文字:").lower()
    b = input("中文请输入c,英文请输入e:")
    d = {}
    c = []
    if b == 'e': #英文模式
        for ch in n:
            if ch in '!"#$&()*+,-./:;<=>?@[\\]^_{}|':
                n = n.replace(ch,' ')
        n = n.split()
        for word in n:
            d[word] = d.get(word,0)+1
        c = list(d.items())
        c.sort(key=lambda x:x[1],reverse=True)
        for i in range(len(c)):
            word,times = c[i]
            print('{}一词出现了{}次'.format(word,times))
    else:
        for ch in n:
            if ch in ',！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.':
                n = n.replace(ch,' ')
        import jieba
        n = jieba.lcut(n)
        for word in n:
            d[word] = d.get(word,0)+1
        c = list(d.items())
        c.sort(key=lambda x:x[1],reverse=True)
        for i in range(len(c)):
            word,times = c[i]
            print('{}一词出现了{}次'.format(word,times))

cp()