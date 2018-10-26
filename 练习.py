import os
import random
#获取部分内容
contentFrom = '错误是由于从os模块引入了所有的函数导致的，os模块下有一个open函数，接受整型的文件描述符和打开模式，from os import *引入os模块的open函数，覆盖了python内建的open函数，导致错误。删除from os import *这行，然后再根据需要，指定引入os模块下的函数'
position = ''
content = [] 
def creatFlie():
    i = 1
    while i<=3:
        name = 'a' + str(i) + '.txt'
        f = open(name,'w+')
        i += 1
def randContent():
    global position
    #获取文本长度
    conLenth = len(contentFrom)
    #获取最大起始位置
    maxStartPosition = conLenth - 20
    #随机获取起始位置
    position = random.randint(0,maxStartPosition)
    return position
def fileWrite():
    #获取列表内容
    fileList = os.listdir()
    #遍历列表内容并写入数据
    for temp in fileList:
        f = open(temp,'w')
        f.write(contentFrom[randContent():])
        f.close()
def editFileName():
    #改变目录至路径
    #获取当前路径下文件名列表
    targetList = os.listdir()
    #print(targetList)
    #循环修改文件名
    for temp in targetList:
        #获取文件后缀位置
        
        houZhui = temp.find('a')
        #通过切片分解文件名并加入修改内容
        os.rename(temp, 'b'+temp[houZhui+1:])
def getFileContent(*args):
    list_A = os.listdir()
    for temp in list_A:
        f = open(temp,'r+')
        f.seek(0,0)
        result = content.append(f.read())
    return result
#默认路径下创建文件夹A
os.mkdir('A')
#在A文件夹下生成3个txt文本
os.chdir('A')
#调用创建文件函数
creatFlie()
#调用写入函数

fileWrite()
#调取A文件夹中文件的内容并存入列表中

#将A文件夹中的文件名称复制到文件夹B并修改名称
#遍历A文件夹中的名字并将内容写入到文件夹B中的文件

fileList_A = os.listdir()
getFileContent()
#在A文件同级目录创建文件B
os.chdir('..')
os.mkdir('B')
#设置默认路径为文件夹B 
os.chdir('B')
i = 0
for temp in fileList_A:
    f = open(temp, 'w+')
    f.write(content[i])
    f.close()
    i+=1
#调用修改名字函数
editFileName()
#打印文件B中的内容
os.chdir('..')
os.chdir('B')
fileList_B = os.listdir()
for temp in fileList_B:
    f = open(temp,'r+')
    f.seek(0,0)
    contentB = f.read()
    print('%s文件夹中的内容为%s'%(temp,contentB))
