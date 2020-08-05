#GovRptWordCloudv1.py
import jieba
import wordcloud
import imageio
mk = imageio.imread('1.jpg')
f = open("新时代中国特色社会主义.txt", 'r',encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud( mask=mk, font_path = 'MSYH.TTC', width = 1000, \
    height = 700, background_color = 'white',stopwords=['发展'] )
w.generate(txt)
w.to_file("grwordcloud.png")