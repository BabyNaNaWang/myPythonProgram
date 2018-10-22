import random
#单行注释
#def funcname(parameter_list)pass
#多行注释
'''if condition:
    pass
else:
    pass'''


'''#变量
a = 100
print(a)
b = 'i love python'
print(b)

# 输入
c = input('请输入：')
print(c)
# 运算符
d = 1
d +=1
print(d)

e = 3
f = e * 3
f = e%3
print(f)
# if 判断
g = 10
h = 100
if g>10 and h<200:
    print('大了')
if not(g>=10 and h<100):
    print('2')

# elif
i = int(input('请输入一个数字：'))
if i > 0 and i <100:
    print('1')
elif i>100 and i <999:
    print('2')
elif i > 1000:
    print('3')

# if 嵌套
myFile = int(input('请输入文件大小:'))
if myFile < 100:
    if myFile <50:
        print('hh')'''
'''# random
#取整
print(random.randint(1,10))
# 取0-1之间的浮点数
print(random.random())
# 取范围内的小数
print(random.uniform(1.1,2.0))
#随机选择一个元素
print(random.choice('1,2,3,4,6'))
# 随机选择一个范围内的数字
print(random.randrange(1,100,3))
# 讲表中的内容顺序打乱
numList = [1,2,3,4,5,6]
random.shuffle(numList)
a = numList
print(a)
e = '别问我爱你有多深'
print(random.sample(e,3))
haha = [10, 20, 30, 40, 50, 60]
random.shuffle(haha)
print(haha)
print(random.sample(range(1,33),6))'''
'''# while 
count = 0
while True:
    print('有没有人曾告诉你')
    count += 1
    if count == 5:
        continue
    if count > 10:
        break
# for 
sing = ['仍然倚在失眠夜','望天边星宿我的牵挂','我的渴望','直至以后']
for x in sing:
    print(x)
else:
    pass

myStr = 'beach'
for tmp in myStr:
    print(tmp)
else:
    pass
myStr = 'hello'
newMyStr = [1,2,3,4,5,6]
print(random.choice(myStr))
print(random.randrange(0,100,4))'''

'''#while
count = 1
myStr = 'hahahaha'
while count <= 3:
    print(myStr[::-1])
    count+=1
else:
    pass
i = 0
newStr = 'hello'
while i < 5:
    print(newStr[i])
    i += 1

for tmp in newStr:
    print(tmp)
# 字符串的常见操作
myStr = 'hello python'
print(myStr.find('he'))
print(len(myStr))
print(myStr.find('h'))
print(myStr.rfind('h'))
print(myStr.rindex('h'))
print(myStr.index('h'))

# 查找文件后缀
fileName = 'zhuxian.txt.exe'
print(fileName.rfind('.'))
print(fileName[11:])
print(fileName.find('hello'))
fileName = 'zhuxian.txt.exe'
print(fileName.count('t'))
print(fileName.find('t',9,15))
#替换
print(fileName.replace('t','h'))
print(fileName)
#切割
name = '我 爱 python'
print(name.split(' '))
# 首字母大写
name = 'i love python'
print(name.split(' '))
print(name.title())

# 以xxx开头/结尾
name = 'i love python'
print(name.startswith('i'))
print(name.endswith('on'))
name = 'I LOVE PYTHON'
print(name.lower())

name1 = 'i love python'
print(name1.upper())
#ljust
name = 'hello world'
print(name.rjust(100))
myStr  = '           hello   world                                    '
print(myStr)
print(myStr.lstrip(' '))
print(myStr.rstrip(' '))
print(myStr.strip(' '))
print(myStr.center(300))