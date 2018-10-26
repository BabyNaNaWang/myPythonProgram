'''#提示并获取要复制的文件名
name = input('请输入要复制的文件名：')
#打开要复制的文件
f_read = open('test.txt','r')
#创建一个新文件存储源文件的内容
f_write = open('test[附件].txt','w')
#复制
content = f_read.read()
f_write.write(content)
#关闭文件
f_read.close()
f_write.close()'''

#提示并获取要复制的文件名
name = input('请输入要复制的文件名：')
#获取文件后缀
num = name.rfind('.')
newName = name[:num] + '[附件]'+ name[num:]
#打开要复制的文件
f_read = open(name, 'r')
#创建一个新文件存储源文件的内容
f_write = open(newName, 'w')
#复制
#第一种复制方式
'''content = f_read.read()
f_write.write(content)'''
#第二种复制方式
'''for lineContent in f_read.readlines():
    f_write.write(lineContent)'''
#第三种复制方式
while True:
    content = f_read.readline()
    if len(content)>0:
        f_write.write(content)
    else:
        break
#关闭文件
f_read.close()
f_write.close()
