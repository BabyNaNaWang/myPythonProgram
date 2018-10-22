import random
a = 'i love python forever'
'''#find
print(a.find('py'))
print(a.find('e',11,20))

#rfind
print(a.rfind('e'))

#index 
print(a.index('e'))

#rindex
print(a.rindex('e'))

#count
print(a.count('e'))

#replace
print(a.replace('e','E'))

#split
print(a.split())

#splitlines
print(a.splitlines())

#首字母大写capitalize
print(a.capitalize())

#title 字符首字母大写
print(a.title())

#startwith
print(a.startswith('i'))

#endwith 
print(a.endswith('j'))

#lower
print(a.lower())

#upper
print(a.upper())'''

b = 'hahahahahha'
'''c = b.ljust(100)
print(len(c))
print(c)
d = b.rjust(200)
print(len(d))
print(d)
print(b.center(100))
print(b.ljust(100))
print(b.rjust(100))'''
#strip
e = 'hello world'
'''print(e.strip())
print(len(e.strip()))
print(e.rstrip())
print(len(e.rstrip()))
print(e.lstrip())
print(len(e.lstrip()))'''
#partition
'''print(e.partition(' '))
print(e.split())
#以换行符拆分splitlines
f = 'hello\nworld\nhaha'
print(f.splitlines())

#isalpha
print(f.isalpha())

#isdigit
print(f.isdigit())

#isspace
print(f.isspace())

#isalnum
print(f.isalnum())'''
# join
'''g = ' '
h = ['i','love','python']
print(g.join(h))'''

#list循环
'''for x in h :
    print(x)'''
#while 打印列表
'''i = 0 
while i < len(h):
    print(h[i])
    i += 1'''
#判断名字是否在列表中
'''name = ['a','b','c','d']
insertName = input('请输入姓名：')
findFlag = 0
for temp in name:
    if insertName ==temp:
        findFlag = 1
        break
if findFlag == 1:
    print('找到了')
else:
    print('没找到')

fileName = 'hello.txt.exe'
print(fileName.rfind('.'))
print(len(fileName))
print(fileName[9:13])
name = ['a', 'b', 'c', 'd']
print(random.choices(name,k=3))

coba = 'hello'
print(random.choice(coba))
#随机整数 randint
print(random.randint(1,10))
#随机小数 random
print(random.random())
#随机浮点数 uniform
print(random.uniform(1.1,10))
#randrange
print(random.randrange(1,100,4))'''
'''#打乱数组
name = ['a', 'b', 'c', 'd']
random.shuffle(name)
print(name)
print(random.sample(name,2))
print(random.sample(range(1,33),6))'''

#乘法表

i = 1
while i<=9:
    j = 1
    while j<=i:
        print('%d*%d=%-2d '%(i, j, i*j), end='')
        j+=1
    print('')
    i += 1
