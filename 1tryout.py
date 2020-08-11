'''dict = {}
digits = '0123456789'
path = 'dict.txt'
def readFile(path, arg):
    try:
        file = open(path,arg,encoding = 'UTF-8')
    except:
        file = open(path,'w',encoding = 'UTF-8')
    return file
def readWords():
    file = readFile(path, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        word = line.split(' ',2)
        dict[word[0]] = word[1][:-1]
    file.close()
def writeFile(word,dsp):
    file = readFile(path, 'a')
    file.write('{} {}\n'.format(word, dsp))
    file.close()
def modifyFile(word, dsp):
    file = readFile(path, 'r')
    line = file.readlines()
    flen = len(line) - 1
    for i in range(flen):
        if word in line[i]:
            file.close()
            line[i] = '{} {}\n'.format(word, dsp)
            file = readFile(path, 'w')
            file.writelines(line)
            break
    file.close()
def editMode():
    print('*'*50)
    print('*'*50)
    while True:
        word = input("(按数字键退出)请输入您想添加或修改的单词:")
        if word in digits:
            print('*'*50)
            print('*'*50)
            return
        try:
            print('该单词已存在于单词库,当前解释是:{}'.format(dict[word]))
        except:
            print('您添加的是一个新单词')
        print('---------------------------------')
        description = input('请输入您的解释:\n')
        try:
            dict[word] += ',%s'%description
            modifyFile(word, dict[word])
        except KeyError:
            dict[word] = '%s'%description
            writeFile(word, dict[word])
        print('----------添加完成--------------')
def searchMode():
    print('*'*50)
    print('*'*50)
    while True:
        word = input("(按数字键退出)想查的单词:")
        if word in digits:
            print('*'*50)
            print('*'*50)
            return
        print('---------------------------------')
        try:
            print(dict[word])
        except KeyError:
            print('对不起，这个单词没有收录')
        print('---------------------------------')
def interface():
    readWords()
    def switch(option):
        funcdic = {
            1:lambda: searchMode(),
            2:lambda: editMode(),
            3:lambda: exit()
        }
        return funcdic[option]()
    while True:
        print('----------欢迎使用英汉词典----------')
        print('1.查询单词\n2.添加单词\n3.退出\n')
        option = int(input('请输入您的选择：'))
        switch(option)
interface()
'''

dict = {}
file = None
digits = '0123456789'
def readWords():
    global file
    file = open('dict.txt','r',encoding = 'GBK')
    string = file.read()
def editMode():
    print('*'*50)
    print('*'*50)
    while True:
        word = input("(按数字键退出)请输入您想添加或修改的单词:")
        if word in digits:
            print('*'*50)
            print('*'*50)
            return
        print('---------------------------------')
        description = input('请输入您的解释:\n')
        try:
            dict[word] += ',%s'%description
        except KeyError:
            dict[word] = '%s'%description
        print('------------添加完成--------------')
def searchMode():
    print('*'*50)
    print('*'*50)
    while True:
        word = input("(按数字键退出)想查的单词:")
        if word in digits:
            print('*'*50)
            print('*'*50)
            return
        print('---------------------------------')
        try:
            print(dict[word])
        except KeyError:
            print('对不起，这个单词没有收录')
        print('---------------------------------')
def interface():
    readWords()
    def switch(option):
        funcdic = {
            1:lambda: searchMode(),
            2:lambda: editMode(),
            3:lambda: exit()
        }
        return funcdic[option]()
    while True:
        print('----------欢迎使用英汉词典----------')
        print('1.查询单词\n2.添加单词\n3.退出\n')
        option = int(input('请输入您的选择：'))
        switch(option)
interface()