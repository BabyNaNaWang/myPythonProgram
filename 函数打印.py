def printLine():
    print('__________________________________')
printLine()
#打印随机数量
def printRodLine():
    #获取需要打印的行数
    rows = int(input('请输入打印的行数：'))
    i = 1
    while i<=rows :
        print('_______')
        i += 1
printRodLine()

def printNewLine(n):
    i = 0
    while i<=n:
        print('_____')
        i+= 1
printNewLine(4)