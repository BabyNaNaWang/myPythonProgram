#添加名字
'''names = ['xiaohong','xiaoming','xiaozhang']
insertName = input('请输入姓名：')
findFlag = 0
for name in names:
    if name == insertName:
        findFlag = 1
if findFlag == 1:
    print('名字存在,无序添加')
else:
    print('没有找到')
    names.append(insertName)
print(names)'''
#修改
'''names = ['xiaohong', 'xiaoming', 'xiaozhang']
names[1] = 'Xiaoming'
print(names)

#查
names = ['xiaohong', 'xiaoming', 'xiaozhang']
insertName = input('请输入姓名：')
if insertName in names:
    print('在')
else:
    print('不在')'''
# count
names = ['xiaohong', 'xiaoming', 'xiaozhang']
print(names.count('xiaohong'))
print(names.count('jhah'))

#index
print(names.index('xiaohong'))

#del 
names = ['xiaohong', 'xiaoming', 'xiaozhang']
del names[1]
print(names)

# pop
names = ['xiaohong', 'xiaoming', 'xiaozhang']
names.pop()
print(names)

#remove
names = ['xiaohong', 'xiaoming', 'xiaozhang']
names.remove('xiaohong')
print(names)