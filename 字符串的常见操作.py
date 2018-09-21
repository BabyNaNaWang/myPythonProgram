aStr = 'hello word'
a = aStr.find('l')
print(a)
fileName = ('abcde.exe.txt')
print(fileName.rfind('.'))  # 结果为9
print(fileName[9:])
name = 'i love python! python is my favourite'
print(name.find('py'))
print(len(name))
print(name.find('py',11,37))

print(name.replace('py','Py',1))
print(name)
print(name.split(' '))
