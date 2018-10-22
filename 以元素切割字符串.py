
'''#time:2018-9-29
#introduction: partition学习
myStr = 'i love python python is my favourite'
print(myStr.partition('is'))
print(myStr.split('is'))
print(myStr.partition('python'))

#introduction:splitlines 学习
name = 'i \nlove\npython'
print(name.splitlines())

#判断是否为字母
name = 'ilovepython'
print(name.isalpha())
#判断是否全为数字
myStr = '123456'
print(myStr.isdigit())

#判断是否为数字、字母或组合
print(myStr.isalnum())
print(name.isalnum())

#判断是否包含空格
name = 'i love python'
print(name.isspace())

myStr = '   '
print(myStr.isspace())'''
#join 插入
myStr = ' '
li = ['1','2','3']
print(myStr.join(li))

aStr = 'i \n love \t python'
bStr = aStr.split()
cStr = ','
dStr = cStr.join(bStr)
print(bStr)
print(dStr)
print(dStr.rfind(',',2))
