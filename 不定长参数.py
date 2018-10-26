def test(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
#test(11,22,33,44,55,66,ee=1,ff=2)
A = [1,2,3]
B = {'cc':1,'dd':2}
test(11,22,A,B)