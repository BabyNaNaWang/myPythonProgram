import os
#获取用户需要修改文件的文件夹
getTargetFloder = input('请输入需要修改的文件夹：')
#改变默认路径至文件夹
os.chdir(getTargetFloder)
#获取目标路径的文件列表
targetList = os.listdir()
#遍历文件名
#获取需要删除的内容
getTargetCon = input('请输入需要删除的名称内容：')
for temp in targetList:
    #获取需要删除的内容长度
    delLenth = len(getTargetCon)
    #获取删除内容起始位置
    startPosion = temp.find(getTargetCon)
    #删除内容
    os.rename(temp,temp[0:startPosion]+temp[startPosion+delLenth:])