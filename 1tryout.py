import jieba
f = open('沉默的羔羊.txt','r',encoding='UTF-8').read()
words = jieba.lcut(f) #jieba分词
dict = {}
for word in words:
    if len(word) < 3:
        continue#把长度低于3的全部清洗
    else:
        dict[word] = dict.get(word,0)+1
counts = list(dict.items())#转换成列表
counts.sort(key= lambda x:x[1],reverse=True)#按频率从大到小排列
max = [] #新建一个空白列表记录同频率的单词
for i in range(len(counts)):
    if counts[i][1] == counts[0][1]:#如果第i个词频等于最大的词频
        max.append(counts[i][0])
for word in max:
    max.sort(key = unicode(word))
