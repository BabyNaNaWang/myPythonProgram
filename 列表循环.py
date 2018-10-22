names = ['gaga','didi','gana']
'''print(names[0])
print(names[1])
print(names[2])
for x in names:
    print(x)'''

#查询是否数字在列表内
findFlag = 0
insertName = input('请输入名字：')
for temp in names:
    if temp == insertName:
        findFlag = 1
        break
if findFlag ==1 :
    print('yes')
else:
    print('no')
    