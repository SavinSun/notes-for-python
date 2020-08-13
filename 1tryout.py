def printIntro():
    print("「三国演义」词云分析开始")

def fenci():
    import jieba
    words = []
    print("开始分词处理")
    txt = open('threekingdoms.txt',encoding='UTF-8').read()
    words = ' '.join(jieba.lcut(txt))
    print("分词处理完毕")
    return words
def wordcloud():
    print("开始词云处理")
    import wordcloud
    w = wordcloud.WordCloud(font_path = 'MSYH.TTC',\
         width = 1000, height = 700, background_color= 'white')
    w.generate(fenci())
    w.to_file('「三国演义」词云分析.png')
    print("词云处理完毕")
def main():
    printIntro()#介绍信息
    wordcloud()#词云
main()