def testB():
    print('b')
def testA():
    print('a')
    testB()
    print('c')
testA()