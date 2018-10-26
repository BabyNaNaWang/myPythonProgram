myInfo = {'name': 'wang', 'sex': 'f', 'wife': 'eeee'}
for temp in myInfo.keys():
    print(temp)
for valuesList in myInfo.values():
    print(valuesList)
for itemList in myInfo.items():
    print(itemList)
for a,b in myInfo.items():
    print('key值为%s，value值为%s'%(a,b))
for i,d in enumerate(myInfo):
    print(i,d)

a = [1,2,3,4]
b = [5,6,7,8]
print(a + b)
print(a*3)