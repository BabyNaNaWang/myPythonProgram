#定义一个求和函数
def countNum(a,b,c):
    return a+b+c
result = countNum(100,200,300)
print(result)


def everNum(a, b, c):
    return countNum(a, b, c)/3
result = everNum(100, 200, 300)
print(result)
