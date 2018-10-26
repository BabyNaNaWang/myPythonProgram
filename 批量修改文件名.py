import os
#os.mkdir('old')
#改变目录至路径
os.chdir('old')
#获取当前路径下文件名列表
targetList = os.listdir()
#print(targetList)
#循环修改文件名
for temp in targetList:
    #获取文件后缀位置
    houZhui = temp.rfind('.')
    #通过切片分解文件名并加入修改内容
    os.rename(temp,temp[:houZhui] +'haha'+temp[houZhui:])