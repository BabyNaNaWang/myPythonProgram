'''aa = lambda a: a + 1
print(aa(8))

def test(a,b,xxx):
    return xxx(a,b)
result = test(11,22,lambda x,y: x+y)
print(result)

#匿名函数在sort中的应用
a = [1,3,4,555,44,663,23]
a.sort(reverse=True)
print(a)
b = [{'ID':1,'age':20},{'ID':2,'age':19},{'ID':3,'age':23}]
b.sort(key=lambda x:x['age'],reverse=True)
print(b)'''

def a():
    print('a')

#def a():
#    print('b')
print(a())
