'''def printhelp():
    print('hello world')
printhelp()

#定义一个名片
def card():
    '定义一个名片内容'
    print('name:kevin')
    print('sex:male')
    print('add:第五大道')
    print('email:10086@qq.com')
    print('phone:10086')
card()
help(card)

def num(num1,num2,numb3):
    print(num1 + num2 + numb3)
num(11,22,33)'''

# 键盘获取数字并相加
def countNumb(n1,n2):
    print(n1 + n2)
n1 = int(input('请输入一个数字'))
n2 = int(input('请输入第二个数字'))
countNumb(n1,n2)
