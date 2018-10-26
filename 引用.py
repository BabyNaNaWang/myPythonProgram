a = 100
b = a
'''print(id(a))
print(id(b))'''
a +=1
print(a)
print(b)

def test(a,b):
    print(id(a))
    print(id(b))
A= 100
B=200
print(id(A))
print(id(B))
test(A,B)

def test1(a):
    #a = a + a
    a += a
A = [11,22]
test1(A)
print(A) 