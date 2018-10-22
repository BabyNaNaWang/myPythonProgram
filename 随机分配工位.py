import random
#1、定义一个嵌套的列表
rooms = [[], [], []]
#2、列表保存8名老师的名字
names = ['a', 'b', 'c', 'd', 'e','f','g','h']
#3、随机添加8分老师添加至第一个列表
for name in names:
    randomNumber = random.randint(0,2)
    rooms[randomNumber].append(name)
i = 1
for room in rooms:
    c = len(room)
    print('办公室%d的共%d名老师，名称是'%(i,c))
    for name in room:
        print(name,end=' ')
    print('')
    i+=1