'''def countNum(a,b):
    return a + b
    return a*b
    return a-b
result = countNum(11,22)
print(result)'''

#计算1到某个数字的和
def count(num):
    result = 0
    i = 1
    while i<=num:
        result = result+i
        i+=1
    return result
num = int(input('请输入一个数字：'))
result = count(num)
print('1到%d的和为：%d'%(num,result))